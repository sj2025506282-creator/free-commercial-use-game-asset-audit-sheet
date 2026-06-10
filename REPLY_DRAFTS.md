# Reply Drafts

Use these as patterns, not copy-paste replies.

Rules:

- Adapt every reply to the actual question.
- Answer first; link only when the free resource directly matches.
- Use at most one free GitHub link.
- Do not mention paid products, Gumroad, coupons, discounts, or upgrades.
- If no human can review, do not publish the reply automatically.

## Font From Mirror Site

Use when someone asks whether a font from a free-font/mirror site can be used in
a game.

```text
Short version: I would not rely on the mirror page alone.

I would:
- find the original creator, foundry, or platform page
- save the source URL and the license evidence URL or bundled license file
- check embedding, raw-file redistribution, modification, reserved font name, logo/title use, and glyph coverage
- replace the font if the original source chain is unclear

Not legal advice, but "free download" is weaker evidence than an original source page or license file.
```

Optional link line:

```text
I also keep a free font provenance log kit for this source-chain check: https://github.com/sj2025506282-creator/free-commercial-use-game-asset-audit-sheet/releases/tag/font-provenance-log-kit-v0.1.0
```

## Asset Licenses Before Shipping

Use when someone asks how to organize asset licenses before release.

```text
Short version: start with a source/provenance log, not a license label.

I would track:
- asset name and local file path
- original source URL
- license evidence URL or bundled license file
- attribution text if needed
- whether raw files are redistributed with the build
- last checked date
- final status: keep, recheck, replace, or block

The main risk is relying on memory near release.
```

Optional link line:

```text
I also keep a free workflow kit with a provenance log, attribution tracker, font checklist, and before-shipping checklist here: https://github.com/sj2025506282-creator/free-commercial-use-game-asset-audit-sheet/releases/tag/workflow-kit-v0.1.0
```

## CC0 vs Attribution

Use when someone asks whether CC0 and attribution-required assets can be mixed.

```text
Short version: yes, but keep them in separate buckets.

I would:
- keep CC0/no-attribution assets separate from CC BY or attribution-required assets
- record the exact source and evidence URL for each asset
- prepare attribution text as soon as the asset enters the project
- re-check the source before release
- avoid using directory tags as final proof

The practical problem is not usually one asset. It is losing track of which assets require credit.
```

## Jam Build Pre-Release Check

Use when someone asks what to check before publishing a jam build or demo.

```text
Short version: check the things that are easy to forget under deadline pressure.

I would review:
- where each asset came from
- whether attribution is required
- whether any raw third-party files are redistributed
- font embedding and license-file handling
- logos, screenshots, marketplace assets, and unclear custom licenses
- whether the team can re-open the evidence later

Not legal advice, but a small source log is better than trying to reconstruct everything after release.
```

Optional link line:

```text
I also keep a free pre-shipping asset-license traps checklist here: https://github.com/sj2025506282-creator/free-commercial-use-game-asset-audit-sheet/releases/tag/asset-license-traps-checklist-v0.1.0
```

## Simple UI SFX

Use only in asset-specific communities where actual asset links are appropriate.

```text
Short version: for menu/HUD sounds, I would keep the pack small and consistent.

I would look for:
- mono WAV files
- consistent loudness
- short confirmation/select/error variants
- clear license notes
- no attribution surprises
- no third-party samples if you need clean redistribution
```

Optional link line:

```text
I made a small free UI confirmation/error SFX pack here if it fits your menu/HUD use case: https://github.com/sj2025506282-creator/free-commercial-use-game-asset-audit-sheet/releases/tag/ui-sfx-v0.1.0
```

## Solo Dev SFX Workflow

Use when someone asks how to make or source sound effects while avoiding licensing
surprises.

```text
Short version: I would use a mix, but keep the workflow boring and traceable.

For a solo horror project I would:
- record simple foley yourself when possible: cloth, doors, taps, mouth sounds, vegetables, paper, keys
- use free libraries only when the license page is clear and you can save the source URL
- keep bought packs in a separate folder with their license or receipt
- avoid sounds ripped from games, films, YouTube videos, or unclear reupload sites
- make a small spreadsheet with file name, source URL, license evidence, attribution text, and whether you modified it
- export final in-game sounds separately from raw downloaded files

For horror specifically, pitch shifting, EQ, reverb, layering, reverse tails, and volume automation usually get you farther than hunting for one perfect scary sound.
```

Optional link line, only when UI/menu sounds are directly relevant:

```text
I made a small free UI confirmation/error SFX pack here if it fits the menu/HUD part of your project: https://github.com/sj2025506282-creator/free-commercial-use-game-asset-audit-sheet/releases/tag/ui-sfx-v0.1.0
```
