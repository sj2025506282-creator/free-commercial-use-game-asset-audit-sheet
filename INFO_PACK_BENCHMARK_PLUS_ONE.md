# Information Pack Benchmark +1 Standard

Last refreshed: 2026-06-01.

## Benchmarks Checked

### SignatureLabel / SignatureSounds

Observed package:

- Reddit post in `r/gamedev`: 100+ packs, 1000s of sounds, years-long archive, free download, CC0/no credit framing.
- Website: 130+ sample packs, thousands of WAV files, hours of recordings, clear free-pack sections, paid all-in-one bundle downstream.
- Trust source: personal creator identity, long-running archive, real recordings, update cadence, external comments.

Strengths:

- Very strong scale signal.
- Strong friction promise: free, no signup/ads/newsletter framing in Reddit post.
- Strong use-case copy per pack: what it is, key features, perfect for, format/license/size.
- Paid offer is downstream and feels like support/convenience, not a hard pitch.

Weak spots we can beat:

- License proof is usually page-level copy, not row-level evidence.
- No machine-readable audit fields for each item.
- No risk notes or limitations per source.
- Harder for users to compare and filter.

### Game Bizdev Spreadsheet Post

Observed package:

- Reddit post in `r/gamedev`: Google Sheet with 170+ publishers, platforms covered, submission emails/forms where found.
- Trust source: personal long-term working doc cleaned for public use; practical bizdev context.

Strengths:

- High count and specific niche.
- Practical fields: publisher, platforms, published games, pitch submission links.
- Clear user action: make a copy, filter, modify.

Weak spots we can beat:

- Verification freshness may be unclear.
- Row-level evidence and last-checked fields are not emphasized in the Reddit copy.
- Risk/fit scoring is not the main promise.

### r/gamedev Font-License Pain Threads

Observed demand:

- Developers repeatedly ask whether fonts can be used in games, whether embedding/distributing font files changes the answer, and whether OFL/Google Fonts are safe.
- High-value pain is not "give me many fonts"; it is "help me avoid licensing mistakes before shipping."

Implication:

- Our font pack should not compete on raw count first.
- It should compete on audit usefulness: source, evidence, embedding note, redistribution note, reserved-name risk, logo/trademark warning, engine-specific handling.

## Benchmark +1 Rule

We copy benchmark packaging, but beat them with verification.

Every serious information pack should have:

- Exact verified count in the title.
- Source URL per row.
- Evidence URL per row.
- Last checked date per row.
- Audit status per row.
- Practical risk note per row.
- Best-use case per row.
- Download friction field.
- Redistribution/embedding/attribution field where relevant.
- README with audit method, limitations, and what the pack is not.
- Local audit report proving the public claim.

## What "Stronger Than Benchmark" Means

Not always bigger.

Stronger means:

- More honest title.
- More verifiable rows.
- More useful columns.
- Easier filtering.
- Clearer limitations.
- Better update path.
- A paid downstream product that saves more time instead of hiding the useful part.

## Current Gap In Our Font Pack

Current v0.1:

- 17 verified rows.
- 8 shipping questions.
- Evidence URL per verified row.
- Audit script passed.

Good enough to be honest and publish.

Not yet stronger enough for monetization:

- Too few rows for a strong "library" claim.
- No XLSX with filters/formatting yet.
- No engine-specific columns.
- No update history/changelog beyond v0.1.
- No community feedback incorporated yet.

## v0.2 Upgrade Target

Build `game-font-license-source-pack-v0.2` as the first real Benchmark+1 pack.

Target:

- 40+ verified rows, not counting discovery rows.
- 5 categories:
  - pixel/retro
  - readable UI/body
  - multilingual/fallback
  - terminal/monospace
  - display/title
- Add columns:
  - `engine_note_unity`
  - `engine_note_godot`
  - `engine_note_unreal`
  - `license_file_required`
  - `reserved_font_name_risk`
  - `logo_use_warning`
  - `glyph_coverage_note`
  - `recommended_for`
  - `avoid_for`
- Add `CHANGELOG.md`.
- Add `AUDIT_METHOD.md`.
- Add XLSX version with filters.
- Add a one-page Markdown buyer/user guide.

Reddit title should stay honest:

`I expanded my free game font license starter pack to 40 verified sources with evidence links and engine notes`

Do not use `50` unless the audit report proves 50 verified rows.

## Monetization Bridge

Free:

- verified starter rows
- checklist
- audit method

Paid later:

- larger maintained database
- XLSX/Notion/Airtable-ready version
- engine-specific license bundling checklist
- attribution/license notice generator
- done-for-you audit of a game's asset/font list

The paid product should save time, not remove the essential free value.
