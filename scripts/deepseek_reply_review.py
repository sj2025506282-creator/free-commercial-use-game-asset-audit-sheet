#!/usr/bin/env python3
"""Review answer-first Reddit drafts with DeepSeek.

Reads a JSON payload from stdin or --input:
{
  "thread": "summary of original thread",
  "existing_replies": "summary of existing replies, or None",
  "draft": "reply draft"
}

Prints strict JSON from the reviewer. Requires DEEPSEEK_API_KEY.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from pathlib import Path

import requests


API_URL = "https://api.deepseek.com/chat/completions"
MODEL = os.environ.get("DEEPSEEK_MODEL", "deepseek-v4-flash")

SCORE_FIELDS = (
    "usefulness_score",
    "subreddit_tone_score",
    "promotion_risk_score",
    "brevity_score",
    "redundancy_risk_score",
)


SYSTEM_PROMPT = """You review Reddit replies in two separate passes.

First pass: strict, nitpicky ordinary Reddit user.
Second pass: moderator-adjacent rules and self-promotion risk reviewer.

Your most important question:
Is this reply genuinely useful to the original poster?

If the link is removed, the reply must still solve part of the problem.

Return strict JSON only. Do not include markdown."""


USER_PROMPT_TEMPLATE = """Review the Reddit reply draft below.

Review in two passes.

Pass 1, ordinary Reddit user:
1. Does it directly answer the original question?
2. Does it give concrete, actionable steps?
3. Is it adapted to this exact thread instead of sounding like a generic template?
4. Does it add a specific useful point that the existing replies have not already covered?
5. Is the direct answer and first action visible immediately, without an unnecessarily long tutorial?
6. Does the tone fit the subreddit: human, concise, non-corporate, and not like support-script text?

Pass 2, moderator-adjacent risk:
7. Does the reply remain useful if every link is removed?
8. Are any links minor supplements rather than the core value?
9. Does it contain or imply promotion, funneling, self-serving language, AI-template tone, paid/Gumroad/coupon/discount/Pro/upgrade/sales language, or likely self-promotion risk?

Return strict JSON only:
{{
  "usefulness_score": 0-10,
  "subreddit_tone_score": 0-10,
  "promotion_risk_score": 0-10,
  "brevity_score": 0-10,
  "redundancy_risk_score": 0-10,
  "recommendation": "Yes" | "No" | "Revise",
  "link_dependency": "None" | "Minor" | "High",
  "largest_usefulness_problem": "...",
  "largest_tone_problem": "...",
  "largest_promotion_or_rules_risk": "...",
  "sentence_to_delete_first": "...",
  "link_decision": "keep" | "remove" | "no_link_present",
  "revision_brief": "..."
}}

Original thread:
{thread}

Existing replies:
{existing_replies}

Draft reply:
{draft}
"""


def load_payload(path: str | None) -> dict:
    raw = Path(path).read_text(encoding="utf-8") if path else sys.stdin.read()
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Input must be JSON: {exc}") from exc

    if not isinstance(payload, dict):
        raise SystemExit("Input JSON must be an object.")
    if not payload.get("thread") or not payload.get("draft"):
        raise SystemExit('Input JSON must include non-empty "thread" and "draft".')
    return payload


def extract_json(text: str) -> dict:
    text = text.strip()
    if text.startswith("```"):
        text = text.strip("`")
        if text.startswith("json"):
            text = text[4:].strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"DeepSeek did not return valid JSON: {exc}\n{text}") from exc


def validate_review(review: dict) -> dict:
    if review.get("link_dependency") == "no_link_present":
        review["link_dependency"] = "None"

    for field in SCORE_FIELDS:
        value = review.get(field)
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise SystemExit(f"DeepSeek review field {field!r} must be numeric.")
        if not 0 <= value <= 10:
            raise SystemExit(f"DeepSeek review field {field!r} must be 0-10.")

    allowed_values = {
        "recommendation": {"Yes", "No", "Revise"},
        "link_dependency": {"None", "Minor", "High"},
        "link_decision": {"keep", "remove", "no_link_present"},
    }
    for field, allowed in allowed_values.items():
        if review.get(field) not in allowed:
            choices = ", ".join(sorted(allowed))
            raise SystemExit(
                f"DeepSeek review field {field!r} must be one of: {choices}."
            )
    return review


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help="Path to JSON payload. Defaults to stdin.")
    args = parser.parse_args()

    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        raise SystemExit("DEEPSEEK_API_KEY is not set.")

    payload = load_payload(args.input)
    user_prompt = USER_PROMPT_TEMPLATE.format(
        thread=payload["thread"].strip(),
        existing_replies=(
            payload.get("existing_replies", "None supplied") or "None supplied"
        ).strip(),
        draft=payload["draft"].strip(),
    )

    response = requests.post(
        API_URL,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json={
            "model": MODEL,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt},
            ],
            "temperature": 0.1,
            "response_format": {"type": "json_object"},
        },
        timeout=60,
    )
    response.raise_for_status()
    content = response.json()["choices"][0]["message"]["content"]
    review = validate_review(extract_json(content))
    review["draft_sha256"] = hashlib.sha256(
        payload["draft"].strip().encode("utf-8")
    ).hexdigest()
    print(json.dumps(review, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
