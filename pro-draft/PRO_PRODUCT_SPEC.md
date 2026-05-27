# Game Asset License Tracker Pro - Product Spec

## Goal

Create a paid product that can earn at least one sale within 30 days.

Minimum viable paid product:

- Useful beyond the free GitHub version
- Honest about license uncertainty
- Does not redistribute third-party assets
- Can be delivered as XLSX/CSV through Gumroad

## Version

Pro v0.1 draft

## Price

- Launch price: USD $9
- Later optional tier: USD $19

## Differentiation From Free Version

| Feature | Free v0.2 | Pro v0.1 Target |
|---|---:|---:|
| Direct asset rows | 42 | 150+ |
| Font tracker rows | 6 | 30+ |
| CC0-only tab | No | Yes |
| Attribution tracker | Basic columns | Dedicated tab |
| Game-jam starter tab | No | Yes |
| Source/provenance notes | Basic | Expanded |
| Update log | Basic | Included |

## Required Tabs

1. `Summary`
2. `Asset License Tracker`
3. `Font License Tracker`
4. `CC0 Only`
5. `Attribution Required`
6. `Game Jam Starter`
7. `Field Guide`
8. `Changelog`

## Required Fields

General asset rows:

- id
- name
- creator/platform
- url
- asset type
- license family
- license signal
- commercial use
- attribution required
- redistribution risk
- signup friction
- evidence level
- evidence URL
- last checked
- best for
- risk notes
- public claim

Font rows:

- id
- name
- creator/platform
- url
- font type
- license family
- license signal
- commercial use
- attribution required
- embedding in game/app
- modification allowed
- logo/brand use
- editorial vs commercial
- redistribution risk
- evidence level
- evidence URL
- last checked
- risk notes

## Quality Gate

Before publishing:

- No row should imply legal certainty.
- No product copy should say "legally safe" or "guaranteed".
- Directory-only rows must be marked as discovery, not verified assets.
- Every Pro row should have an evidence URL.
- A random 10-row spot check should pass.
- DeepSeek review should return `publish_ready` or equivalent.

## Publishing Path

1. Keep free GitHub Release as public trust surface.
2. Create Gumroad paid product draft.
3. Add Gumroad link to GitHub README only after Pro package passes review.
4. Do not direct-link Gumroad on Reddit as the first link.
5. Use Reddit to share the free GitHub tool and mention Pro only lightly if relevant.
