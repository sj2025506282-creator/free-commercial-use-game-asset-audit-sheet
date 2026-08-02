#!/usr/bin/env python3
"""Summarize answer-first Markdown log rows for a review window."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from datetime import date
from pathlib import Path


FIELDS = (
    "date",
    "platform",
    "community",
    "thread",
    "url",
    "decision",
    "risk",
    "resource",
    "reply_posted",
    "result",
)


def parse_rows(text: str) -> list[dict[str, str]]:
    rows = []
    for line in text.splitlines():
        if not line.startswith("| 20"):
            continue
        values = [value.strip() for value in line.strip().strip("|").split("|")]
        if len(values) != len(FIELDS):
            continue
        try:
            date.fromisoformat(values[0])
        except ValueError:
            continue
        rows.append(dict(zip(FIELDS, values, strict=True)))
    return rows


def summarize(rows: list[dict[str, str]]) -> dict:
    dates = sorted({row["date"] for row in rows})
    return {
        "dates": dates,
        "candidate_count": len(rows),
        "decisions": dict(sorted(Counter(row["decision"] for row in rows).items())),
        "risks": dict(sorted(Counter(row["risk"] for row in rows).items())),
        "communities": dict(
            sorted(Counter(row["community"] for row in rows).items())
        ),
        "reply_posted_count": sum(row["reply_posted"] == "Yes" for row in rows),
        "linked_candidate_count": sum(row["resource"] != "None" for row in rows),
        "direct_fit_count": sum(row["result"].startswith("Score 2/") for row in rows),
        "mature_outcome_readback_count": sum(
            "48-72h readback:" in row["result"].lower() for row in rows
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--log", default="ANSWER_LOG.md")
    parser.add_argument("--start", required=True, type=date.fromisoformat)
    parser.add_argument("--end", required=True, type=date.fromisoformat)
    args = parser.parse_args()
    if args.start > args.end:
        parser.error("--start must not be after --end")

    rows = parse_rows(Path(args.log).read_text(encoding="utf-8"))
    selected = [
        row
        for row in rows
        if args.start <= date.fromisoformat(row["date"]) <= args.end
    ]
    print(json.dumps(summarize(selected), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
