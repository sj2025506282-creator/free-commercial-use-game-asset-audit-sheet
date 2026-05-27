# Free Game Asset License Tracker

This is a starter license tracker for indie game developers who need free game assets with clearer commercial-use, attribution, redistribution, and font-embedding signals.

## What This Is

- 42 direct asset pages with commercial-use/CC0 license signals.
- 8 additional rows are license/reference/discovery sources, not direct asset packs.
- Each row records source URL, asset type, license signal, attribution requirement, redistribution risk, signup friction, and audit status.
- The `row_type` column marks whether a row is an `asset_page`, `license_or_source_reference`, or `discovery_pool`.
- This sheet links to original creator/source pages. It does not redistribute third-party asset files.
- Current strict audit status: `conditional_pass`. See `AUDIT_REPORT.md`.

## v0.2 Files

- `game_asset_license_tracker_v0.2.csv`: Google Sheet-friendly general asset tracker with `license_family`, `evidence_level`, `last_checked`, and `public_claim`.
- `font_license_tracker_v0.2.csv`: font-specific tracker with fields for embedding, modification, logo/brand use, editorial vs commercial use, and redistribution risk.

## Audit Status Meaning

- `verified_collection_policy`: the creator or platform states a broad license policy that covers its listed asset pages.
- `verified_page_signal`: the page title or listing includes an explicit license signal such as CC0.
- `directory_signal_only`: the asset was found through a CC0/free directory filter, but the individual page should be checked again before recommending it as final.
- `source_reference_only`: useful license/profile/reference page, but not a direct asset-pack row.
- `discovery_pool_only`: useful place to find future rows, but not a verified asset row.

## Commercial-Use Notes

- CC0/public domain sources are usually the cleanest for game jams and commercial prototypes.
- CC BY sources can be useful but need attribution tracking.
- Font licensing needs its own checks: embedding in a game/app, modification, logo/brand usage, and editorial vs commercial use are separate questions.
- Avoid NC, ND, unclear custom licenses, and pages that do not explicitly state whether commercial use is allowed.
- Even with CC0, keep a source log for provenance and future takedown/dispute handling.

## Files

- `commercial_use_game_asset_sources_audit_v0.1.csv`: the original v0.1 audit sheet.
- `game_asset_license_tracker_v0.2.csv`: the v0.2 general tracker.
- `font_license_tracker_v0.2.csv`: the v0.2 font licensing tracker.
- `reddit_post_draft.md`: a draft Reddit post for feedback/testing.
- `AUDIT_REPORT.md`: strict audit notes and public-claim limits.
