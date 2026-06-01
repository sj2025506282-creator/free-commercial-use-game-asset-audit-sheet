# Benchmark Mimic Playbook

Last refreshed: 2026-06-01.

## Primary Benchmark To Copy

Primary benchmark for packaging discipline: `RunebitDice` on `r/gameassets`.

Why:

- Repeatable small-pack publishing cadence.
- Titles are formulaic and easy to imitate.
- Each post has exact count, format, sizes, commercial-use, no-attribution.
- Uses gallery/visual proof.
- Body has predictable sections: contents, license, creation method, download, related packs.
- Scores are not huge, but the pattern is sustainable and subreddit-native.

Primary business direction: curated information products.

This project should not become a raw asset factory. The core product is useful reviewed material: source lists, audit sheets, templates, checklists, trackers, and directories. Raw asset packs are side experiments for attention and subreddit access.

Secondary benchmark: `SignatureLabel` on `r/gamedev`.

Why:

- Strong trust framing: long-running free resource archive.
- Clear CC0/no-signup promise.
- Broad cross-subreddit distribution by adapting the same resource to each audience.
- Works better for bigger periodic updates, not every small release.

## RunebitDice Pattern

### Posting Cadence

Observed cadence in May 2026:

- 2026-05-03: r/gameassets free D20 result sprites.
- 2026-05-05: r/gameassets free Ember Runes D20 result sprites.
- 2026-05-13: r/gameassets free Nightfall Marble D20 result sprites.
- 2026-05-15: r/gameassets free Black Opal D20 result sprites.
- 2026-05-17: r/gameassets free Gold Glitter D20 result sprites.
- 2026-05-19: r/gameassets free Starforged Cobalt D20 result sprites.
- 2026-05-27: r/gameassets free Cathedral Window D20 result sprites.

Copyable cadence:

- One focused free pack every 2-7 days.
- Reuse the same structure.
- Change the theme/content, not the format.

### Title Formula

RunebitDice title formula:

`[Free] [2D] 20 photoreal <theme> D20 result sprites | transparent PNGs | 3 sizes | commercial-use | no attribution`

Our copyable title formulas:

For actual asset packs:

`[Free] [Audio] 20 <theme> UI/SFX sounds | WAV | commercial-use | no signup`

`[Free] [CSV/XLSX] 50 <theme> asset sources | commercial-use signals | no attribution filter | no signup`

`[Free] [Checklist] 7 <theme> traps for game devs | CSV + Markdown | no signup`

For `r/gameassets`, only use this when the post is an actual game asset submission. Templates/checklists should go to `r/gamedev`, not `r/gameassets`.

### Body Formula

Use this structure:

1. One-line intro: exact pack number and use case.
2. Contents:
   - exact count
   - formats
   - sizes/sample rate/columns
   - what files are included
3. License short version:
   - commercial use allowed
   - attribution required or not
   - modification allowed or not
   - raw redistribution rule
   - full terms in LICENSE or README
4. How it was made:
   - original/procedural/hand-edited/source-audited
   - no unclear-rights source material
   - no redistribution of third-party assets
5. Download link:
   - GitHub Release or no-email direct download first
6. Related packs:
   - link previous free packs or repo index
7. One feedback question.

### RunebitDice-Style Body Template

```markdown
<Ordinal> free <asset/source/checklist> pack from <brand/project>.

<Exact count> <format> files for <specific use case>. Theme is <theme>: <short visual/audio/workflow description>.

Contents:

- <count> <asset/source/checklist rows>
- <formats>
- <sizes/sample rate/columns/tabs>
- <support files>

License / use notes:

- Commercial use allowed.
- Attribution: <required/not required/track separately>.
- Modification allowed: <yes/no/depends>.
- Redistribution as standalone raw assets: <allowed/not allowed/not applicable>.
- Full notes in README/LICENSE/AUDIT_NOTES.

How it was made:

- <original/procedural/hand-edited/source-audited method>.
- <evidence/provenance/audit statement>.
- No redistributed third-party asset files.

Download:
<GitHub Release or no-email link>

Related free packs:
- <previous pack 1>
- <previous pack 2>

What should I make/check next: <specific feedback question>?
```

## SignatureLabel Pattern

### Title Formula

SignatureLabel title formula:

`Hi guys, I created a website about 7 years ago in which I host all my field recordings and foley sounds which are all free to download and use CC0. There is currently 100+ packs with 1000's of sounds and hours of recordings and foley all perfect for game SFX.`

Our copyable version:

`Hi guys, I am building a free game-asset license/provenance library. It currently has <count> source rows, <count> checklists, and <count> downloadable workflow files for game jams and indie releases. No asset redistribution, no signup, not legal advice.`

Use this only after we have a stronger archive, such as:

- 100+ source rows
- 5+ checklist packs
- several release pages
- visible download/comment history

## Current Mimic Decision

Do not imitate one-off "I made money" posts yet.

Imitate:

- RunebitDice for repeatable small free releases.
- SignatureLabel for periodic archive updates.
- Dumivid for strong CC0/no-attribution/full-pack wording and feedback CTA.

But keep product priority clear:

- P0: curated information packs that can lead to Gumroad purchases.
- P1: free asset packs only when they create useful Reddit attention or trust.
- P2: broad archive-update posts after the information library is large enough.

## Our Next Copycat Release Type

Best next pack to build:

`[Free] [CSV/XLSX] 50 game font sources/checks | commercial-use signals | font embedding questions | no signup`

Why:

- Existing Reddit comments specifically mentioned font licensing.
- Risk-warning posts about fonts perform strongly in `r/gamedev`.
- It connects naturally to the paid Starter Asset Audit Template Pack.
- It fits the user's main positioning as a materials curator instead of an asset maker.

## Execution Lock

We will fully imitate the benchmark system, not the exact content.

Primary operating rule:

- Every new Reddit release starts as a small free pack with a narrow use case.
- The title must state exact count, format, use case, license/commercial-use signal, and no-signup/no-email access.
- The body must reuse the same section order every time: intro, contents, license notes, how it was made or audited, download, related packs, one feedback question.
- The first link should be GitHub or another no-email download surface. Gumroad stays downstream in README/profile/product links.
- For the core lane, "pack" means a curated information pack: rows, sources, checklists, trackers, templates, or audit notes.
- For `r/gameassets`, only post real game assets, with visual/audio proof.
- For `r/gamedev`, post resource/checklist/workflow packs as Feedback Request or Resource style.

## 7-Day Copycat Schedule

Day 1:

- Publish/prepare one RunebitDice-style free pack draft.
- If the pack is a checklist/source sheet, target `r/gamedev`, not `r/gameassets`.
- If the pack is SFX/sprites/code assets, target `r/gameassets` with proof media.

Day 2:

- Monitor score, comments, removals, GitHub release downloads, and Gumroad clicks/sales if available.
- Reply only when useful; do not bump with empty comments.

Day 3-4:

- Build the next adjacent free pack using the same format.
- Add one related-pack link back to the previous release.

Day 5-7:

- If there is comment/download signal, create a downstream paid offer or improve the existing $9 pack CTA.
- If there is no signal, change the theme/use case, not the whole strategy.

## Next Two Packs

P0 for `r/gamedev`:

`[Free] [CSV/XLSX] 50 game font sources/checks | commercial-use signals | font embedding questions | no signup`

P0 for `r/gameassets`:

`[Free] [Audio] 20 clean UI confirmation/error SFX | WAV | game-ready | commercial-use | no signup`

Decision:

- Build the font/license pack first if the goal is to sell the $9 template pack.
- Build the UI SFX pack first if the goal is to enter `r/gameassets` with the closest RunebitDice mimic.

## Hard Boundaries

- Copy structure, not content.
- Do not claim CC0/no-attribution unless verified.
- Do not post templates/checklists to `r/gameassets` unless rules allow them as assets.
- Do not direct-link Gumroad first.
- Always include preview/cover assets for Gumroad products.
