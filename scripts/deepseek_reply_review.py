#!/usr/bin/env python3
"""Review answer-first Reddit drafts with DeepSeek.

Reads a JSON payload from stdin or --input:
{
  "thread": "summary of original thread",
  "draft": "reply draft"
}

Prints strict JSON from the reviewer. Requires DEEPSEEK_API_KEY.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

import requests


API_URL = "https://api.deepseek.com/chat/completions"
MODEL = os.environ.get("DEEPSEEK_MODEL", "deepseek-chat")


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
4. Does the tone fit the subreddit: human, concise, non-corporate, and not like support-script text?

Pass 2, moderator-adjacent risk:
5. Does the reply remain useful if every link is removed?
6. Are any links minor supplements rather than the core value?
7. Does it contain or imply promotion, funneling, self-serving language, AI-template tone, paid/Gumroad/coupon/discount/Pro/upgrade/sales language, or likely self-promotion risk?

Return strict JSON only:
{{
  "usefulness_score": 0-10,
  "subreddit_tone_score": 0-10,
  "promotion_risk_score": 0-10,
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
    review = extract_json(content)
    print(json.dumps(review, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
