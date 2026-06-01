#!/usr/bin/env python3
"""Strict audit for curated information packs."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from urllib.parse import urlparse


REQUIRED_COLUMNS = {
    "id",
    "row_type",
    "name",
    "creator_or_platform",
    "url",
    "license_signal",
    "evidence_url",
    "commercial_use",
    "attribution_required",
    "redistribution_note",
    "download_requires_signup",
    "audit_status",
    "risk_notes",
    "best_for",
    "last_checked",
}

VERIFIED_STATUSES = {
    "verified_page_signal",
    "verified_collection_policy",
    "verified_license_file",
    "verified_official_docs",
}

DISCOVERY_STATUSES = {
    "discovery_only",
    "discovery_pool_only",
    "source_reference_only",
}


def valid_url(value: str) -> bool:
    parsed = urlparse(value.strip())
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_file", type=Path)
    parser.add_argument("--min-verified", type=int, default=1)
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args()

    failures: list[str] = []
    warnings: list[str] = []

    with args.csv_file.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
        columns = set(rows[0].keys()) if rows else set()

    missing = sorted(REQUIRED_COLUMNS - columns)
    if missing:
        failures.append(f"missing required columns: {missing}")

    verified_rows = [row for row in rows if row.get("audit_status") in VERIFIED_STATUSES]
    discovery_rows = [row for row in rows if row.get("audit_status") in DISCOVERY_STATUSES]
    unknown_status_rows = [
        row
        for row in rows
        if row.get("audit_status") not in VERIFIED_STATUSES | DISCOVERY_STATUSES
    ]

    if len(verified_rows) < args.min_verified:
        failures.append(f"too few verified rows: {len(verified_rows)} < {args.min_verified}")
    if unknown_status_rows:
        failures.append(f"unknown audit_status rows: {[row.get('id') for row in unknown_status_rows]}")

    seen_urls: dict[str, str] = {}
    duplicate_urls: list[tuple[str, str, str]] = []
    bad_url_rows: list[str] = []
    blank_field_rows: dict[str, list[str]] = {}

    for row in rows:
        row_id = row.get("id", "")
        url = row.get("url", "").strip()
        evidence_url = row.get("evidence_url", "").strip()
        if not valid_url(url):
            bad_url_rows.append(row_id)
        if not valid_url(evidence_url):
            bad_url_rows.append(f"{row_id}:evidence_url")
        if url in seen_urls:
            duplicate_urls.append((row_id, seen_urls[url], url))
        else:
            seen_urls[url] = row_id

        for field in REQUIRED_COLUMNS:
            if not row.get(field, "").strip():
                blank_field_rows.setdefault(field, []).append(row_id)

    if bad_url_rows:
        failures.append(f"invalid URLs in rows: {bad_url_rows}")
    if duplicate_urls:
        failures.append(f"duplicate URLs: {duplicate_urls}")
    if blank_field_rows:
        failures.append(f"blank required fields: {blank_field_rows}")

    verified_without_evidence = [
        row.get("id", "")
        for row in verified_rows
        if row.get("audit_status") == "verified_page_signal"
        and row.get("license_signal", "").lower() in {"", "unknown", "unclear"}
    ]
    if verified_without_evidence:
        failures.append(f"verified rows without license evidence: {verified_without_evidence}")

    if len(discovery_rows) > len(verified_rows):
        warnings.append("more discovery/source-reference rows than verified rows")

    report = {
        "csv_file": str(args.csv_file),
        "status": "pass" if not failures else "fail",
        "failures": failures,
        "warnings": warnings,
        "summary": {
            "row_count": len(rows),
            "verified_count": len(verified_rows),
            "discovery_or_reference_count": len(discovery_rows),
            "min_verified": args.min_verified,
        },
    }
    print(json.dumps(report, ensure_ascii=False, indent=2 if args.pretty else None))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
