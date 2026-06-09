# Metrics Log - 2026-06-04

## Scope

Project: Reddit -> GitHub -> Gumroad game-asset license workflow.

Goal: first real cash transaction within the 30-day validation window.

This log uses confirmed CLI data only. Reddit live post metrics are marked pending because `rdt read` did not return reliably and Reddit public JSON was blocked by network security.

## Confirmed GitHub Metrics

Repository:

https://github.com/sj2025506282-creator/free-commercial-use-game-asset-audit-sheet

Traffic API:

- Views: 124 total / 70 unique.
- Clones: 370 total / 187 unique.
- Notable view dates:
  - 2026-05-26: 50 views / 25 unique.
  - 2026-06-01: 47 views / 29 unique.
- Notable clone dates:
  - 2026-05-27: 91 clones / 53 unique.
  - 2026-05-31: 89 clones / 39 unique.
  - 2026-06-01: 69 clones / 37 unique.
  - 2026-06-02: 37 clones / 14 unique.

Release download counts:

| Release | Asset | Downloads |
| --- | --- | ---: |
| ui-sfx-v0.1.0 | ui-confirmation-error-sfx-pack-v0.1.zip | 28 |
| workflow-kit-v0.1.0 | game_jam_asset_license_workflow_kit_v0.1.zip | 8 |
| game-font-license-pack-v0.1.0 | game-font-license-source-pack-v0.1.zip | 6 |
| game-font-license-pack-v0.2.0 | game-font-license-source-pack-v0.2.zip | 2 |
| v0.2.0 | free_game_asset_license_tracker_v0.2.xlsx | 0 |
| v0.2.0 | game_asset_license_tracker_v0.2.csv | 0 |
| v0.2.0 | font_license_tracker_v0.2.csv | 0 |
| v0.2.0 | preview_license_tracker_v0.2.png | 0 |

## Confirmed Gumroad Metrics

Main paid product:

- Name: Game Asset Audit Template Pack for Indie Developers.
- URL: https://3813941972097.gumroad.com/l/isavr
- Price: USD $9.
- Published: yes.
- File attached: `starter_asset_audit_template_pack_v0.2.zip`.
- Cover exists: yes.
- `thumbnail_url`: present.
- Sales: 0.
- Revenue: 0.
- Offer code: `REDDIT40`, 40% off, max 10 uses.
- Offer code usage: 0.

Older paid preview:

- Name: Game Asset License Tracker Pro Preview.
- URL: https://3813941972097.gumroad.com/l/grjtiq
- Price: SGD$7.
- Published: yes.
- File attached: `game_asset_license_tracker_pro_preview_v0.1.zip`.
- Cover exists: yes.
- `thumbnail_url`: present.
- Sales: 0.
- Revenue: 0.

## Reddit Metrics

Active watch items:

- `1tnz9hk`: original r/gamedev asset audit sheet.
- `1tssd1i`: benchmark-style r/gamedev workflow kit post.
- `1ttesqj`: font license starter pack.
- `1ttc3tr`: r/gameassets UI SFX side experiment.

Status:

- Live Reddit metrics pending.
- `rdt read` did not return reliable output in this run.
- Public Reddit JSON returned a network-security block.

Do not use old Reddit scores as current data until checked through a valid login/API path.

## Interpretation

Strongest confirmed pull:

- GitHub clones are much stronger than release downloads, which means users may be cloning the repo as a resource rather than clicking individual assets.
- UI SFX has the strongest release-download signal at 28 downloads, but this is a side experiment and does not directly prove the paid audit-template path.

Weakest confirmed pull:

- The first v0.2 release files still show 0 downloads each.
- Gumroad sales and `REDDIT40` usage are both 0.
- The main paid product is technically complete, including cover and thumbnail, but has no conversion signal yet.

Likely issue:

- The free GitHub surface is attracting some utility behavior, but the paid upgrade path is not yet obvious or compelling enough to produce a first transaction.
- Building another paid product now would add inventory without evidence of buyer intent.

## Decision

Status: strengthen CTA, do not publish a new Reddit thread yet.

Reason:

- Free activity exists: views, clones, and some release downloads.
- Paid conversion is zero.
- The current Level 4 threshold says to strengthen CTA when free downloads increase but Gumroad sales and offer-code use remain 0.

## Next Actions

1. Improve the GitHub README paid section so it clearly explains when the free releases are enough and when the $9 workflow pack saves time.
2. Add a short `Start here` block near the top of the README pointing users to:
   - free font/source pack,
   - free workflow kit ZIP,
   - paid audit template pack only as the downstream workflow layer.
3. Prepare but do not post a narrow Reddit update until live Reddit metrics are refreshed.
4. Fix or replace the Reddit metrics path:
   - retry `rdt status`,
   - use a logged-in API route,
   - or use browser/Chrome only for read-only metric verification if CLI remains blocked.
5. Re-check Gumroad sales and `REDDIT40` usage after the README CTA update.

## Hold

Do not:

- Change Gumroad price.
- Publish a new paid product.
- Direct-link Gumroad first on Reddit.
- Post another Reddit thread just to bump visibility.
- Claim legal safety or guaranteed commercial-use clearance.
