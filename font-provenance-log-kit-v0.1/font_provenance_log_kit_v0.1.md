# Font Provenance Log Kit v0.1

This kit is for tracking the source chain of fonts used in games.

The goal is not to prove that a font is legally safe. The goal is to avoid shipping with mystery font files, mirror-only evidence, missing license files, or unclear embedding/redistribution status.

## Why Font Provenance Matters

Font problems often appear late because the file looks small and harmless. A team may grab a `.ttf` from a "free fonts" site, a zip bundle, a tutorial project, or an old prototype folder, then forget where it came from.

Before shipping, record the source chain:

1. Where did the file come from?
2. Is that source official, creator-owned, platform-hosted, mirror-only, or unknown?
3. Where is the visible license evidence?
4. Does the license allow commercial use, embedding, modification, and redistribution?
5. Is a license file or copyright notice bundled with the game?
6. Has the source been re-checked near the release date?

## Minimum Useful Font Log

For each font file, record:

- project font name
- local file name
- original source URL
- evidence URL or exact license-file location
- source type
- creator/foundry/platform
- license signal
- commercial-use signal
- attribution or notice requirement
- embedding status
- raw-file redistribution status
- modification status
- reserved font name risk
- logo/title-use warning
- glyph coverage note
- last checked date
- final re-check status

## Mirror Risk Review

Treat mirror-only sources as a warning sign.

Common risk signals:

- The mirror does not link to the creator, foundry, or official project.
- The license text is missing, generic, or different from the official source.
- The upload name, author name, or copyright notice does not match the font metadata.
- The mirror says "free" but not "commercial use allowed."
- The zip file has no license file.
- Multiple sites list conflicting licenses for the same font.

Action: find the original source or replace the font.

## Engine Packaging Reminder

Unity, Godot, Unreal, and custom engines can package font files differently. Keep the source URL and license evidence with your project audit notes, not only inside the engine import folder.

If the game build includes a raw font file, record whether the license file or copyright notice must ship with it.

## Final Pre-Shipping Recheck

Before public or commercial release:

- Re-open important source URLs.
- Confirm the evidence URL still exists.
- Confirm the local file name matches the reviewed font.
- Confirm attribution/notice text is ready if needed.
- Confirm modified fonts do not violate reserved-name rules.
- Confirm glyph coverage and fallback behavior for target languages.

Do this close to release, not only at prototype start.
