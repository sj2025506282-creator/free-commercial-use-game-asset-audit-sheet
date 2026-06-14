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
Short version: use a mix of self-recorded foley, clearly licensed libraries, and light editing, but keep a source log from day one.

For a solo horror game, I would handle it like this:
- record easy foley yourself first: footsteps on different surfaces, cloth movement, door taps, keys, breathing, mouth clicks, paper, water, vegetables, and small impacts
- use libraries only when each sound has a clear license page; save the exact source URL, license URL, author name, and download date
- treat Pixabay/Freesound/etc. as sources to verify per file, not as one safe bucket
- avoid sounds ripped from games, movies, YouTube videos, trailers, or random reupload packs
- keep raw downloads separate from edited in-game exports
- name exports by use case, like `ui_confirm_01.wav` or `monster_breath_close_02.wav`, so you can replace one later without losing the project

For horror specifically, make ordinary sounds do more work: pitch down, layer two or three quiet sounds, reverse a tail, add a short reverb, automate volume, and cut aggressively so the sound starts fast.

For UI sounds specifically, keep them short, mono, consistent in loudness, and less dramatic than the creature/jumpscare sounds so they do not fatigue the player.
```

Optional link line, only when UI/menu sounds are directly relevant:

```text
I made a small free UI confirmation/error SFX pack here if it fits the menu/HUD part of your project: https://github.com/sj2025506282-creator/free-commercial-use-game-asset-audit-sheet/releases/tag/ui-sfx-v0.1.0
```

Strict review note:

Default to answer-only for broad solo-dev SFX workflow questions. Add the UI SFX
link only when the original question specifically asks for UI/menu/HUD sounds and
the answer already has enough concrete value without the link.

DeepSeek pass example:

- usefulness score: 9
- promotion risk score: 0
- recommendation: Yes
- link decision: no_link_present

## Beginner State Machine Timer

Use when a beginner understands the idea of a state machine but needs a concrete
GDScript starting point for waiting, advancing, or locking interaction.

````text
Short version: make the character logic a tiny state machine, and let a timer decide when the state is allowed to move on.

For a first version, I would keep it very plain:

```gdscript
enum State { IDLE, TALKING, WAITING, DONE }

var state: State = State.IDLE

func interact() -> void:
    if state != State.IDLE:
        return
    state = State.TALKING
    play_dialogue_or_animation()

func play_dialogue_or_animation() -> void:
    $AnimatedSprite2D.play("talk")
    state = State.WAITING
    await get_tree().create_timer(1.5).timeout
    advance_to_next_stage()

func advance_to_next_stage() -> void:
    state = State.DONE
    $AnimatedSprite2D.play("idle")
```

The important part is not the exact names; it is that each state has one job.
`IDLE` can accept interaction, `TALKING` starts the animation/dialogue, `WAITING`
prevents the player from triggering it again, and `DONE` means the interaction
has finished.

Once that works, you can replace `advance_to_next_stage()` with whatever your
arcade character needs next: change dialogue text, enable another object, play a
different animation, or emit a signal to another node. I would avoid singletons
for this at first; keep the logic on the character until you have two or three
characters that clearly need shared behavior.
````

DeepSeek pass example:

- usefulness score: 8
- subreddit tone score: 9
- promotion risk score: 0
- recommendation: Yes
- link dependency: None
- link decision: no_link_present

## Simple Random TileMap Path

Use when a beginner wants a randomly generated path and needs a tiny first
algorithm rather than a full maze/dungeon generator.

````text
For a first version, don't start with a maze algorithm. Make a random walk that
moves mostly forward, then draw one tile at each position.

The simplest shape is:

1. Pick a start cell.
2. Place a path tile there.
3. Move one cell to the right.
4. Sometimes move up or down by 1.
5. Repeat until the path is long enough.

Something like this for Godot 4 TileMap:

```gdscript
@onready var tile_map: TileMap = $TileMap

const LAYER := 0
const SOURCE_ID := 0
const PATH_TILE := Vector2i(0, 0) # change this to your path tile's atlas coords

func _ready() -> void:
    generate_path()

func generate_path() -> void:
    var pos := Vector2i(0, 5)
    var length := 40

    for i in range(length):
        tile_map.set_cell(LAYER, pos, SOURCE_ID, PATH_TILE)

        pos.x += 1
        pos.y += randi_range(-1, 1)
        pos.y = clampi(pos.y, 2, 10)
```

That will give you a simple left-to-right path that wiggles up and down. If
nothing appears, the usual thing to check is whether `SOURCE_ID` and `PATH_TILE`
match the tile in your TileSet.

The values to change first are `length`, the starting `pos`, and the clamp range
for `pos.y`.

If you want the path to be less jagged, only change `y` sometimes:

```gdscript
if randf() < 0.35:
    pos.y += randi_range(-1, 1)
```

Once that works, you can add extra rules: avoid going outside the map, add wider
path tiles around the center tile, or store every path cell in an array so
enemies/items can spawn on it later.
````

DeepSeek pass example:

- usefulness score: 9
- subreddit tone score: 9
- promotion risk score: 0
- recommendation: Yes
- link dependency: None
- link decision: no_link_present
