#!/usr/bin/env python3
"""Deterministically evaluate the Reddit unattended comment publish gate."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse


BANNED_COMMUNITIES = {"gamedev"}
BANNED_LANGUAGE = (
    "paid",
    "gumroad",
    "coupon",
    "discount",
    "pro",
    "upgrade",
    "sales",
    "付费",
    "优惠码",
    "折扣",
    "升级",
)
SCORE_FIELDS = ("thread_fit", "helpfulness", "risk", "link_fit", "originality")
URL_RE = re.compile(r"https?://[^\s<>()\]]+", re.IGNORECASE)


class InvalidPayload(ValueError):
    """Raised when a gate payload is malformed."""


def load_payload(path: str | None) -> dict:
    raw = Path(path).read_text(encoding="utf-8") if path else sys.stdin.read()
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise InvalidPayload(f"Input must be JSON: {exc}") from exc
    if not isinstance(payload, dict):
        raise InvalidPayload("Input JSON must be an object.")
    return payload


def require_bool(payload: dict, field: str) -> bool:
    value = payload.get(field)
    if not isinstance(value, bool):
        raise InvalidPayload(f"{field!r} must be boolean.")
    return value


def require_int(payload: dict, field: str) -> int:
    value = payload.get(field)
    if not isinstance(value, int) or isinstance(value, bool):
        raise InvalidPayload(f"{field!r} must be an integer.")
    return value


def require_string_list(payload: dict, field: str) -> list[str]:
    value = payload.get(field)
    if not isinstance(value, list) or any(
        not isinstance(item, str) or not item.strip() for item in value
    ):
        raise InvalidPayload(f"{field!r} must be a list of non-empty strings.")
    normalized = [item.strip() for item in value]
    if len(normalized) != len(set(normalized)):
        raise InvalidPayload(f"{field!r} must not contain duplicate ids.")
    return sorted(normalized)


def normalized_community(value: object) -> str:
    if not isinstance(value, str) or not value.strip():
        raise InvalidPayload("'community' must be a non-empty string.")
    return value.strip().lower().removeprefix("r/")


def validate_scores(payload: dict) -> tuple[dict, int]:
    scores = payload.get("scores")
    if not isinstance(scores, dict):
        raise InvalidPayload("'scores' must be an object.")
    for field in SCORE_FIELDS:
        value = scores.get(field)
        if not isinstance(value, int) or isinstance(value, bool):
            raise InvalidPayload(f"scores.{field} must be an integer.")
        if value not in {0, 1, 2}:
            raise InvalidPayload(f"scores.{field} must be 0, 1, or 2.")
    return scores, sum(scores[field] for field in SCORE_FIELDS)


def validate_deepseek(payload: dict) -> dict:
    review = payload.get("deepseek")
    if not isinstance(review, dict):
        raise InvalidPayload("'deepseek' must be an object.")
    for field in (
        "usefulness_score",
        "subreddit_tone_score",
        "promotion_risk_score",
        "brevity_score",
        "redundancy_risk_score",
    ):
        value = review.get(field)
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise InvalidPayload(f"deepseek.{field} must be numeric.")
        if not 0 <= value <= 10:
            raise InvalidPayload(f"deepseek.{field} must be 0-10.")
    return review


def find_banned_language(draft: str) -> list[str]:
    found = []
    lowered = draft.lower()
    for term in BANNED_LANGUAGE:
        if term.isascii():
            if re.search(rf"\b{re.escape(term)}\b", lowered):
                found.append(term)
        elif term in draft:
            found.append(term)
    return found


def evaluate(payload: dict) -> dict:
    community = normalized_community(payload.get("community"))
    draft = payload.get("draft")
    if not isinstance(draft, str) or not draft.strip():
        raise InvalidPayload("'draft' must be a non-empty string.")
    draft = draft.strip()

    scores, total = validate_scores(payload)
    review = validate_deepseek(payload)
    failures = []

    live_reply_ids = require_string_list(payload, "live_reply_ids")
    reviewed_reply_ids = review.get("reviewed_reply_ids")
    if not isinstance(reviewed_reply_ids, list) or any(
        not isinstance(item, str) or not item.strip() for item in reviewed_reply_ids
    ):
        raise InvalidPayload(
            "'deepseek.reviewed_reply_ids' must be a list of non-empty strings."
        )
    reviewed_reply_ids = sorted({item.strip() for item in reviewed_reply_ids})
    if live_reply_ids != reviewed_reply_ids:
        failures.append(
            "live reply ids changed after DeepSeek review; re-read and re-review"
        )

    boolean_gates = {
        "community_status_verified": "community status was not verified",
        "rules_allow_ordinary_help": "rules do not clearly allow ordinary help",
        "thread_open": "thread is not open for an ordinary reply",
        "existing_replies_reviewed": "existing replies were not reviewed",
        "useful_without_link_verified": "standalone usefulness was not verified",
        "opening_answer_verified": "opening answer and first action were not verified",
    }
    for field, reason in boolean_gates.items():
        if not require_bool(payload, field):
            failures.append(reason)

    if require_bool(payload, "moderator_sensitive"):
        failures.append("community or thread is moderator-sensitive")
    if require_bool(payload, "legal_or_commercial_dispute"):
        failures.append("thread is legal-conclusion or commercial-dispute adjacent")
    if community in BANNED_COMMUNITIES:
        failures.append(f"r/{community} is read-only")

    concrete_gap = payload.get("concrete_gap")
    if not isinstance(concrete_gap, str) or not concrete_gap.strip():
        failures.append("no concrete gap beyond existing replies was recorded")

    today_count = require_int(payload, "today_public_comment_count")
    if today_count != 0:
        failures.append("a public comment was already posted today")
    if total < 8:
        failures.append(f"candidate total is {total}, below 8")
    if scores["risk"] != 2:
        failures.append(f"risk score is {scores['risk']}, not 2")

    deepseek_gates = (
        (review["usefulness_score"] >= 8, "DeepSeek usefulness is below 8"),
        (review["subreddit_tone_score"] >= 7, "DeepSeek tone is below 7"),
        (review["promotion_risk_score"] <= 3, "DeepSeek promotion risk exceeds 3"),
        (review["brevity_score"] >= 7, "DeepSeek brevity is below 7"),
        (review["redundancy_risk_score"] <= 3, "DeepSeek redundancy risk exceeds 3"),
        (
            review.get("recommendation") == "Yes",
            "DeepSeek recommendation is not Yes",
        ),
        (
            review.get("link_dependency") in {"None", "Minor"},
            "DeepSeek link dependency is not None or Minor",
        ),
    )
    failures.extend(reason for passed, reason in deepseek_gates if not passed)

    draft_sha256 = hashlib.sha256(draft.encode("utf-8")).hexdigest()
    if review.get("draft_sha256") != draft_sha256:
        failures.append("draft body does not match the DeepSeek-reviewed hash")

    banned = find_banned_language(draft)
    if banned:
        failures.append(f"banned public language found: {', '.join(banned)}")

    urls = [url.rstrip(".,;:!?") for url in URL_RE.findall(draft)]
    if len(urls) > 1:
        failures.append("draft contains more than one link")
    if urls:
        host = (urlparse(urls[0]).hostname or "").lower()
        if host not in {"github.com", "www.github.com"}:
            failures.append("public link is not on github.com")
        if review.get("link_decision") != "keep":
            failures.append("DeepSeek did not explicitly keep the link")
    elif review.get("link_decision") not in {"no_link_present", "remove"}:
        failures.append("no-link draft has an inconsistent DeepSeek link decision")

    return {
        "passed": not failures,
        "community": f"r/{community}",
        "candidate_total": total,
        "risk_score": scores["risk"],
        "link_count": len(urls),
        "live_reply_ids": live_reply_ids,
        "draft_sha256": draft_sha256,
        "failures": failures,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="Path to JSON payload. Defaults to stdin.")
    args = parser.parse_args()
    try:
        result = evaluate(load_payload(args.input))
    except InvalidPayload as exc:
        print(json.dumps({"passed": False, "invalid": True, "error": str(exc)}))
        return 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
