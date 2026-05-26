# Strict Audit Report - v0.1

Audit date: 2026-05-26

## Verdict

Status: **conditional_pass**

The sheet is useful as a Reddit feedback/freebie artifact, but it should not be marketed as "50 verified asset packs" yet.

Safer public positioning:

> 42 verified commercial-use asset pages + 8 license/reference/discovery sources, with risk flags.

## What Passed

- The sheet links to original creator/source pages and does not redistribute third-party files.
- The strongest rows come from creators/platforms with clear CC0/public-domain signals:
  - Kenney asset pages and Kenney support/license reference.
  - Screaming Brain Studios profile/official site stating public-domain CC0 policy.
  - GGBotNet rows where listing/title explicitly says CC0.
- CSV structure is valid: 50 rows, 13 fields, no missing URLs.
- The revised CSV includes a `row_type` column so asset pages are clearly separated from reference and discovery rows.

## What Needs Fixing Before Strong Marketing

1. **Do not count directory/reference pages as asset packs.**
   - Rows 1, 2, 21, 22, 41, 48, 49, 50 are useful evidence or discovery pages, but not direct asset-pack rows.

2. **Downgrade broad policy rows in public copy.**
   - Some rows rely on creator-wide policy rather than page-level evidence captured in the sheet.
   - That is acceptable for a v0.1 free audit sheet, but the public copy must say "license signal" rather than "legal guarantee".

3. **Avoid legal certainty.**
   - Use wording like "commercial-use signal", "license note", "risk flag", and "verify before shipping".
   - Do not say "legally safe" or "guaranteed safe".

4. **OpenGameArt and itch.io directory rows are discovery pools only.**
   - They are excellent sources for future rows, but each item must be individually checked.

## Row Classification

| Classification | Rows | Count | Publish Use |
|---|---:|---:|---|
| Asset pages with strong CC0/commercial-use signal | 3-20, 23-40, 42-47 | 42 | Can stay in the public sheet |
| License/reference/source pages | 1, 2, 21, 22, 41 | 5 | Keep as evidence, not asset-pack count |
| Discovery directories | 48, 49, 50 | 3 | Keep as discovery pools, not verified entries |

## Final Public Claim

Allowed:

- "I made a free audit sheet of commercial-use game asset sources."
- "It includes 42 direct asset pages plus license/reference/discovery sources."
- "Each row has license signals, attribution notes, signup friction, and risk flags."

Avoid:

- "50 legally safe assets."
- "50 fully verified asset packs."
- "You can use everything commercially without checking."

## Recommended v0.2

- Replace 8 non-asset/reference rows with 8 additional page-level verified asset rows.
- Add fields:
  - `evidence_url`
  - `evidence_type`
  - `last_checked`
  - `public_claim`
  - `legal_confidence`
- Add a separate `sources_and_license_references.md` for directory/profile/license reference pages.
