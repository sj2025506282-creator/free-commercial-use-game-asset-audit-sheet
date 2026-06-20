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

## CC0 Starter Sources For A Jam

Use when someone wants quick no-signup CC0 starting points instead of a full
workflow.

```text
Short version: start from a small CC0/no-signup source list, but treat it as a starter pool, not final proof.

I would:
- pick likely sources first so the team can prototype fast
- save the exact asset page you actually used, not just the starter row
- keep a separate provenance log for anything that survives into the final build
- re-check the page one more time before release in case the listing changed

The main risk is assuming "it was on my safe starter sheet" is enough evidence later.
```

Optional link line:

```text
I also keep a free CC0-only starter sheet for quick jam prototypes here: https://github.com/sj2025506282-creator/free-commercial-use-game-asset-audit-sheet/tree/main/cc0-game-jam-starter-v0.1
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

## Unity Time-Scaled SFX

Use when a Unity user wants already-playing sound effects to speed up or slow
down with a time manipulation mechanic.

````text
Yes, if the sound is playing through an `AudioSource`, you can change
`AudioSource.pitch` while it is already playing. The catch is that
`PlayOneShot()` is awkward here because you do not get a separate handle for each
one-shot voice.

I would make every important SFX come from a small pooled prefab instead:

```csharp
public class TimeScaledSfx : MonoBehaviour
{
    [SerializeField] private AudioSource source;

    public void Play(AudioClip clip, float timeScale)
    {
        source.clip = clip;
        source.pitch = timeScale;
        source.Play();
    }

    public void SetTimeScale(float timeScale)
    {
        source.pitch = timeScale;
    }

    private void Update()
    {
        if (!source.isPlaying)
            gameObject.SetActive(false); // or return to pool
    }
}
```

Then have one central time/audio manager notify active SFX when the clock changes:

```csharp
public class TimeAudioController : MonoBehaviour
{
    private readonly List<TimeScaledSfx> active = new();
    private float currentTimeScale = 1f;

    public void SetTimeScale(float scale)
    {
        currentTimeScale = scale;

        foreach (var sfx in active)
            sfx.SetTimeScale(scale);
    }

    public void Register(TimeScaledSfx sfx)
    {
        active.Add(sfx);
        sfx.SetTimeScale(currentTimeScale);
    }
}
```

For short impacts, this is usually enough: pitch `2.0` sounds faster and higher,
pitch `0.5` sounds slower and lower.

For looping ambience or music, I would handle those separately through an
AudioMixer snapshot or middleware, because raw pitch changes can get ugly fast.
But for instantiated SFX like hits, UI sounds, whooshes, reloads, etc., pooled
`AudioSource` instances with live `pitch` updates are the simple version.
````

DeepSeek pass example:

- usefulness score: 9
- subreddit tone score: 9
- promotion risk score: 0
- recommendation: Yes
- link dependency: None
- link decision: no_link_present

## Godot Reverse Resource Owners

Use when a Godot user asks whether the FileSystem dock's View Owners behavior is
available from script. The safe public route is to scan editor resources and
invert `ResourceLoader.get_dependencies()`.

````text
I do not think the FileSystem dock's `View Owners` action is exposed as a nice
one-call API. The stable public route is usually to invert the dependency list
yourself: walk the editor filesystem, call `ResourceLoader.get_dependencies()`
for each resource/scene, and collect the files that depend on your target.

Something like this is the shape I would start with:

```gdscript
@tool
extends EditorScript

const TARGET := "res://path/to/your_resource.tres"

func _run() -> void:
    var owners: Array[String] = []
    var fs := EditorInterface.get_resource_filesystem()
    _scan_dir(fs.get_filesystem(), TARGET, owners)

    for owner in owners:
        print(owner)

func _scan_dir(dir: EditorFileSystemDirectory, target_path: String, owners: Array[String]) -> void:
    for i in range(dir.get_file_count()):
        var path := dir.get_file_path(i)
        if path == target_path:
            continue

        for dep in ResourceLoader.get_dependencies(path):
            if _dependency_matches(dep, target_path):
                owners.append(path)
                break

    for i in range(dir.get_subdir_count()):
        _scan_dir(dir.get_subdir(i), target_path, owners)

func _dependency_matches(dep: String, target_path: String) -> bool:
    if dep == target_path:
        return true

    # Godot 4 dependency strings may include UID/fallback path info.
    if dep.contains("::"):
        return dep.get_slice("::", 2) == target_path

    return false
```

That is still not a raw project-file parser. You are asking Godot's resource
loaders for dependency information, which is safer than regexing `.tscn` /
`.tres` yourself.

The main caveat is that this finds serialized resource dependencies. It will not
reliably catch paths built dynamically in code, strings inside scripts, or
resources loaded from custom logic unless those references are actually
serialized as dependencies. It also scans the project, so I would keep it as an
editor-only tool rather than something that runs during normal gameplay.
````

DeepSeek pass example:

- usefulness score: 8
- subreddit tone score: 9
- promotion risk score: 0
- recommendation: Yes
- link dependency: None
- link decision: no_link_present

## Unity IK Tip Target With Local Offset

Use when a Unity user needs `OnAnimatorIK` to place a hand so a held object's tip
or hook lands on a target point. The common bug is subtracting an unrotated
world-space offset.

````text
The part that is probably breaking is that your offset is being treated like a
world-space offset. The offset from the hand to the rod tip has to be rotated by
the hand's final IK rotation before you subtract it from the zipline point.

I would set this up with two reference transforms on the held object:

```text
HeldRod
  GripPose      # where the hand should be, orientation included
  AttachPoint   # the rod tip / hook point that must land on the zipline
```

At equip time, cache the attach point relative to the grip pose:

```csharp
Vector3 attachLocalPos = gripPose.InverseTransformPoint(attachPoint.position);
Quaternion attachLocalRot = Quaternion.Inverse(gripPose.rotation) * attachPoint.rotation;
```

Then in `OnAnimatorIK`, solve rotation first, then position:

```csharp
void OnAnimatorIK(int layerIndex)
{
    Vector3 zipPoint = _zipPosition;

    // Pick whatever direction the rod tip should face while hanging.
    Vector3 rodForward = (_zipForward.sqrMagnitude > 0.001f)
        ? _zipForward.normalized
        : transform.forward;

    Quaternion desiredAttachRotation = Quaternion.LookRotation(rodForward, transform.up);

    // Convert desired attach/tip rotation into the hand rotation needed to produce it.
    Quaternion desiredHandRotation = desiredAttachRotation * Quaternion.Inverse(attachLocalRot);

    // This is the important bit: rotate the local hand->tip offset by the desired hand rotation.
    Vector3 desiredHandPosition = zipPoint - (desiredHandRotation * attachLocalPos);

    _animator.SetIKPositionWeight(AvatarIKGoal.LeftHand, 1f);
    _animator.SetIKRotationWeight(AvatarIKGoal.LeftHand, 1f);
    _animator.SetIKPosition(AvatarIKGoal.LeftHand, desiredHandPosition);
    _animator.SetIKRotation(AvatarIKGoal.LeftHand, desiredHandRotation);
}
```

The key idea is:

```csharp
handPosition = targetTipPosition - handRotation * localHandToTipOffset;
```

Your current version is close, but it subtracts an offset that does not change
when the hand/rod rotates. That is why it only works in the one pose where the
rod happens to match the original offset.
````

DeepSeek pass example:

- usefulness score: 9
- subreddit tone score: 8
- promotion risk score: 0
- recommendation: Yes
- link dependency: None
- link decision: no_link_present

## TMP Styles With Localization

Use when a Unity user asks whether TMP style tags or sprite tags should live
inside localization tables.

````text
I would split this by whether the styling is part of the language or just
presentation.

If the style/icon is fixed UI decoration, keep it out of the translation table
and compose it in code:

```csharp
label.text = $"<style=Cost>{localizedCostText}</style> <sprite name=coin>";
```

That is safer because translators do not have to preserve TMP tags or sprite
names.

If the style needs to move with the sentence, then put a semantic placeholder in
the localized string instead of raw TMP markup, then replace it after
localization. For example, the table can contain something like:

```text
You need {coin_icon} {amount} more coins.
```

Then your UI code maps `{coin_icon}` to `<sprite name=coin>` and maybe wraps
`{amount}` in a style. That keeps the localization entry readable while still
letting word order change per language.

I would only put raw TMP tags directly in the localization table when the
translators/localization pipeline can validate them. It works, but one missing
closing tag or renamed sprite can break the rendered text.

A practical rule:
- color/size/icon that always appears in the same place: compose outside the
  localized string
- tags/icons whose position depends on grammar: use placeholders in the
  localized string
- raw `<style>` / `<sprite>` tags in tables: only if your loc process checks them
````

DeepSeek pass example:

- usefulness score: 9
- subreddit tone score: 9
- promotion risk score: 0
- recommendation: Yes
- link dependency: None
- link decision: no_link_present

## Projectile Mods As Resources

Use when a Godot user is scaling projectile modifiers and has started using
string IDs, global dictionaries, or exported Callables.

````text
I would move the data into Resources, but not by trying to export a `Callable`.
Treat each mod as a small Resource with normal methods. The editor can assign
the Resource; the code can call its methods.

For example, make a base mod resource:

```gdscript
# projectile_mod.gd
class_name ProjectileMod
extends Resource

func apply(projectile: Blast) -> void:
    pass

func tick(projectile: Blast, delta: float) -> void:
    pass
```

Then make concrete mods as separate Resource scripts:

```gdscript
# ice_mod.gd
class_name IceMod
extends ProjectileMod

@export var speed := 200.0
@export var color := Color(0.056, 0.093, 0.8, 1.0)

func apply(projectile: Blast) -> void:
    projectile.speed = speed
    projectile.modulate = color
```

```gdscript
# wave_mod.gd
class_name WaveMod
extends ProjectileMod

@export var frequency := 5.0
@export var amplitude := 150.0

func apply(projectile: Blast) -> void:
    projectile.dynamicVars["wave_time"] = 0.0

func tick(projectile: Blast, delta: float) -> void:
    projectile.dynamicVars["wave_time"] += delta
    projectile.position += projectile.transform.y * cos(projectile.dynamicVars["wave_time"] * frequency) * amplitude * delta
```

Then your projectile keeps an array of mod resources:

```gdscript
@export var mods: Array[ProjectileMod] = []

func constructor(selected_mods: Array[ProjectileMod]) -> void:
    mods = selected_mods.duplicate()
    for mod in mods:
        mod.apply(self)

func _process(delta: float) -> void:
    basic_movement(self, delta)
    for mod in mods:
        mod.tick(self, delta)
```

That removes the global string dictionary for most cases. Your weapon/spell
Resource can simply export `Array[ProjectileMod]`, so you build combinations in
the inspector instead of remembering string keys.

I would keep a dictionary only if you need lookup by save-file ID, like
`"stat_ice" -> preload("res://mods/ice_mod.tres")`. For gameplay code, passing
actual Resource instances around is cleaner than passing strings and resolving
them later.
````

DeepSeek pass example:

- usefulness score: 9
- subreddit tone score: 9
- promotion risk score: 0
- recommendation: Yes
- link dependency: None
- link decision: no_link_present

## Marker3D Spawnpoints By Upgrade Level

Use when a Godot user wants editor-friendly projectile spawn points grouped by
weapon upgrade level and is fighting nested exported arrays.

````text
I would not fight the inspector with `Array[Array[Marker3D]]` for this. For Godot, I would make the weapon scene hierarchy express the upgrade levels, then build the arrays in `_ready()`.

Example structure:

```text
Weapon
  Level1
    SpawnA
    SpawnB
  Level2
    SpawnA
    SpawnB
    SpawnC
  Level3
    SpawnA
    SpawnB
    SpawnC
    SpawnD
```

Then export the level containers, not every marker:

```gdscript
@export var level_containers: Array[Node3D] = []

var spawn_points_by_level: Array[Array] = []

func _ready() -> void:
    for container in level_containers:
        var points: Array[Marker3D] = []
        for child in container.get_children():
            if child is Marker3D:
                points.append(child)
        spawn_points_by_level.append(points)
```

In the editor, drag `Level1`, `Level2`, etc. into `level_containers`. The markers
can be direct children of those level nodes.

When firing, pick the current upgrade level and use each marker's transform:

```gdscript
func fire(level: int) -> void:
    var points: Array = spawn_points_by_level[level]
    for marker: Marker3D in points:
        var projectile := projectile_scene.instantiate()
        get_tree().current_scene.add_child(projectile)
        projectile.global_transform = marker.global_transform
```

That gives you the editor workflow you probably want: move/rotate the markers
visually, group them by upgrade level, and avoid typing transforms by hand. It is
also less fragile than name-pattern lookup because renaming a marker does not
break anything as long as it stays under the right level node.

If you later need per-spawn metadata, like damage multiplier or fire delay, then
I would make a small `WeaponLevel` Resource or a custom child node. But for just
positions and directions, level containers plus Marker3D children is the simplest
version.
````

DeepSeek pass example:

- usefulness score: 9
- subreddit tone score: 9
- promotion risk score: 0
- recommendation: Yes
- link dependency: None
- link decision: no_link_present

## Clock UI State And Repair Interaction

Use when a beginner wants a UI clock/timer to stop sometimes and be restarted by
interacting with an in-world object.

````text
I would split it into three small pieces instead of trying to make the clock sprite and UI do everything at once.

One script owns the clock state:

```gdscript
enum ClockState { RUNNING, STOPPED }

var state: ClockState = ClockState.RUNNING
var time_left := 60.0

func _process(delta: float) -> void:
    if state != ClockState.RUNNING:
        return

    time_left -= delta
    update_clock_ui(time_left)

func stop_clock() -> void:
    state = ClockState.STOPPED
    show_clock_stopped_effect()

func restart_clock() -> void:
    state = ClockState.RUNNING
    hide_clock_stopped_effect()
```

Then use a separate Timer node only to decide *when* the problem happens:

```gdscript
func _on_break_timer_timeout() -> void:
    stop_clock()
```

And your world clock interaction just calls the restart method:

```gdscript
func interact_with_clock() -> void:
    if clock_controller.state == clock_controller.ClockState.STOPPED:
        clock_controller.restart_clock()
```

So yes, timers are still the right idea, but I would not make the timer itself be
the clock. Let `_process(delta)` handle the ticking display, let a Timer trigger
the interruption, and let the interactable clock sprite only repair/restart it.
That keeps the mechanic from turning into one giant script.
````

DeepSeek pass example:

- usefulness score: 9
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
