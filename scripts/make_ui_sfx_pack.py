#!/usr/bin/env python3
"""Generate a small RunebitDice-style free UI SFX pack."""

from __future__ import annotations

import csv
import math
import random
import shutil
import struct
import subprocess
import wave
import zipfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


SAMPLE_RATE = 48000
ROOT = Path("ui-confirmation-error-sfx-pack-v0.1")
AUDIO_DIR = ROOT / "audio" / "wav"
ZIP_PATH = Path("ui-confirmation-error-sfx-pack-v0.1.zip")


def clamp(value: float) -> float:
    return max(-1.0, min(1.0, value))


def normalize(samples: list[float], peak: float = 0.78) -> list[float]:
    max_abs = max((abs(s) for s in samples), default=1.0)
    if max_abs < 1e-8:
        return samples
    return [s / max_abs * peak for s in samples]


def fade(samples: list[float], fade_in: float = 0.002, fade_out: float = 0.03) -> list[float]:
    out = samples[:]
    n = len(out)
    fi = max(1, int(fade_in * SAMPLE_RATE))
    fo = max(1, int(fade_out * SAMPLE_RATE))
    for i in range(min(fi, n)):
        out[i] *= i / fi
    for i in range(min(fo, n)):
        out[n - 1 - i] *= i / fo
    return out


def write_wav(path: Path, samples: list[float]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(path), "w") as wav:
        wav.setnchannels(1)
        wav.setsampwidth(2)
        wav.setframerate(SAMPLE_RATE)
        frames = b"".join(struct.pack("<h", int(clamp(s) * 32767)) for s in samples)
        wav.writeframes(frames)


def sine_tone(duration: float, frequencies: list[float], decay: float, rng: random.Random) -> list[float]:
    n = int(duration * SAMPLE_RATE)
    phases = [rng.random() * math.tau for _ in frequencies]
    out = []
    for i in range(n):
        t = i / SAMPLE_RATE
        env = min(1.0, t / 0.006) * math.exp(-t / decay)
        value = 0.0
        for index, freq in enumerate(frequencies):
            phases[index] += math.tau * freq / SAMPLE_RATE
            value += math.sin(phases[index]) / len(frequencies)
        out.append(value * env)
    return fade(normalize(out, 0.72))


def click(duration: float, base: float, rng: random.Random) -> list[float]:
    n = int(duration * SAMPLE_RATE)
    phase = rng.random() * math.tau
    out = []
    for i in range(n):
        t = i / SAMPLE_RATE
        env = min(1.0, t / 0.0015) * math.exp(-t / 0.026)
        phase += math.tau * (base + 80 * math.exp(-t / 0.03)) / SAMPLE_RATE
        transient = rng.uniform(-1.0, 1.0) * math.exp(-t / 0.004) * 0.34
        body = math.sin(phase) * env
        out.append(body + transient)
    return fade(normalize(out, 0.75))


def error_boop(duration: float, start: float, end: float, rng: random.Random) -> list[float]:
    n = int(duration * SAMPLE_RATE)
    phase = rng.random() * math.tau
    out = []
    for i in range(n):
        ratio = i / max(1, n - 1)
        t = i / SAMPLE_RATE
        freq = start * (1 - ratio) + end * ratio
        env = min(1.0, t / 0.008) * math.exp(-t / 0.12)
        phase += math.tau * freq / SAMPLE_RATE
        out.append((math.sin(phase) + 0.22 * math.sin(phase * 2.01)) * env)
    return fade(normalize(out, 0.7))


def layered(*parts: list[float], gap: float = 0.0) -> list[float]:
    silence = [0.0] * int(gap * SAMPLE_RATE)
    out: list[float] = []
    for index, part in enumerate(parts):
        if index:
            out.extend(silence)
        out.extend(part)
    return normalize(out, 0.76)


def make_specs() -> list[dict[str, object]]:
    rng = random.Random(20260601)
    specs = [
        ("confirm", "UISFX_001_confirm_soft_chime.wav", sine_tone(0.32, [660, 990], 0.11, rng), "Soft positive confirmation chime"),
        ("confirm", "UISFX_002_confirm_double_ping.wav", layered(sine_tone(0.13, [740], 0.055, rng), sine_tone(0.18, [988], 0.07, rng), gap=0.045), "Double confirmation ping"),
        ("confirm", "UISFX_003_confirm_unlock.wav", layered(click(0.09, 760, rng), sine_tone(0.22, [880, 1320], 0.08, rng), gap=0.018), "Unlock or success UI sound"),
        ("confirm", "UISFX_004_confirm_bright.wav", sine_tone(0.28, [784, 1176, 1568], 0.085, rng), "Bright success tone"),
        ("confirm", "UISFX_005_confirm_low_soft.wav", sine_tone(0.3, [392, 588], 0.12, rng), "Low soft accept tone"),
        ("select", "UISFX_006_select_tick_short.wav", click(0.08, 980, rng), "Short menu select tick"),
        ("select", "UISFX_007_select_tick_glass.wav", layered(click(0.07, 1280, rng), sine_tone(0.12, [1560], 0.04, rng), gap=0.0), "Glass-like select tick"),
        ("select", "UISFX_008_select_soft_button.wav", click(0.12, 540, rng), "Soft button press"),
        ("select", "UISFX_009_select_cursor_move.wav", sine_tone(0.11, [620], 0.035, rng), "Cursor move tone"),
        ("select", "UISFX_010_select_tab_switch.wav", layered(click(0.06, 720, rng), click(0.08, 920, rng), gap=0.035), "Tab switch tick pair"),
        ("error", "UISFX_011_error_soft_down.wav", error_boop(0.28, 420, 250, rng), "Soft descending error tone"),
        ("error", "UISFX_012_error_wrong_choice.wav", layered(error_boop(0.17, 480, 320, rng), error_boop(0.18, 420, 260, rng), gap=0.055), "Wrong choice double error"),
        ("error", "UISFX_013_error_locked.wav", layered(click(0.07, 310, rng), error_boop(0.22, 330, 230, rng), gap=0.01), "Locked action sound"),
        ("error", "UISFX_014_error_warning_pulse.wav", error_boop(0.36, 520, 520, rng), "Single warning pulse"),
        ("error", "UISFX_015_error_cancel.wav", error_boop(0.22, 360, 210, rng), "Cancel or deny tone"),
        ("notification", "UISFX_016_notification_light.wav", sine_tone(0.34, [523.25, 783.99], 0.14, rng), "Light notification tone"),
        ("notification", "UISFX_017_notification_popup.wav", layered(click(0.06, 880, rng), sine_tone(0.2, [1046.5], 0.075, rng), gap=0.022), "Popup notification sound"),
        ("notification", "UISFX_018_notification_quest.wav", sine_tone(0.42, [587.33, 880, 1174.66], 0.16, rng), "Quest or item notification chime"),
        ("notification", "UISFX_019_notification_subtle.wav", sine_tone(0.24, [493.88, 659.25], 0.12, rng), "Subtle notification tone"),
        ("notification", "UISFX_020_notification_done.wav", layered(sine_tone(0.12, [659.25], 0.055, rng), sine_tone(0.22, [987.77, 1318.51], 0.085, rng), gap=0.04), "Task complete notification"),
    ]
    return [
        {"category": category, "filename": filename, "samples": samples, "description": description}
        for category, filename, samples, description in specs
    ]


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    name = "Arial Bold.ttf" if bold else "Arial.ttf"
    path = Path("/System/Library/Fonts/Supplemental") / name
    return ImageFont.truetype(str(path), size)


def make_cover(path: Path) -> None:
    img = Image.new("RGB", (1600, 900), "#121417")
    draw = ImageDraw.Draw(img)
    draw.rectangle((0, 610, 1600, 900), fill="#20323a")
    draw.rectangle((1120, 0, 1600, 900), fill="#35443a")
    for x in range(1060, 1540, 80):
        draw.rounded_rectangle((x, 190, x + 44, 234), radius=8, fill="#e6d36f")
        draw.rounded_rectangle((x - 38, 290, x + 6, 334), radius=8, fill="#85c8ff")
        draw.rounded_rectangle((x + 18, 392, x + 62, 436), radius=8, fill="#e56f6f")
    draw.text((88, 98), "FREE UI SFX", fill="#ffffff", font=font(104, True))
    draw.text((90, 230), "CONFIRMATION + ERROR", fill="#e6d36f", font=font(76, True))
    draw.text((92, 348), "20 original WAV sounds", fill="#ffffff", font=font(58, True))
    draw.text((96, 476), "Select ticks · success chimes · warning tones · notifications", fill="#dce7ea", font=font(35))
    draw.text((96, 736), "GAME-READY · MONO WAV · 48 KHZ", fill="#ffffff", font=font(42, True))
    draw.text((96, 796), "Commercial use allowed · no attribution required", fill="#dce7ea", font=font(31))
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path)


def write_text_files(rows: list[dict[str, str]]) -> None:
    (ROOT / "README.txt").write_text(
        """Free UI Confirmation + Error SFX Pack v0.1

20 original synthetic UI sound effects for game prototypes, menus, HUDs, inventory screens, and jam builds.

Contents:
- 20 mono WAV files
- 48 kHz, 16-bit
- categories: confirm, select, error, notification
- preview_all_20_ui_sfx.wav
- FILE_LIST.csv
- LICENSE.txt

Use notes:
- Designed as short, dry UI sounds that can be layered or processed.
- No third-party sound libraries, game assets, movie audio, marketplace samples, or unclear-rights source material were used.
- Generated procedurally with Python oscillators/noise and hand-coded envelopes.
""",
        encoding="utf-8",
    )
    (ROOT / "LICENSE.txt").write_text(
        """License for Free UI Confirmation + Error SFX Pack v0.1

Commercial use allowed.
Attribution is appreciated but not required.
Modification, editing, mixing, and processing are allowed.

You may use these sounds inside finished games, videos, apps, prototypes, client work, streams, and interactive projects.

You may not resell, redistribute, re-upload, or repackage the raw sound files as a standalone sound effects library, asset pack, sample pack, dataset, or download collection.

Provided as-is, without warranty.
""",
        encoding="utf-8",
    )
    (ROOT / "GUMROAD_COPY.txt").write_text(
        """Title: Free UI Confirmation + Error SFX Pack

Short description:
20 original mono WAV UI sounds for game menus, HUDs, jam builds, and prototypes.

Includes:
- confirmation chimes
- menu select ticks
- soft error/warning tones
- notification sounds
- preview WAV
- file list and license

Commercial use allowed. No attribution required. Raw redistribution as another asset pack is not allowed.
""",
        encoding="utf-8",
    )
    with (ROOT / "FILE_LIST.csv").open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["filename", "category", "format", "sample_rate", "channels", "description"],
        )
        writer.writeheader()
        writer.writerows(rows)


def make_pack() -> None:
    if ROOT.exists():
        shutil.rmtree(ROOT)
    if ZIP_PATH.exists():
        ZIP_PATH.unlink()

    specs = make_specs()
    rows: list[dict[str, str]] = []
    preview: list[float] = []
    silence = [0.0] * int(0.16 * SAMPLE_RATE)
    for spec in specs:
        rel = Path("audio") / "wav" / str(spec["category"]) / str(spec["filename"])
        write_wav(ROOT / rel, spec["samples"])
        preview.extend(spec["samples"])
        preview.extend(silence)
        rows.append(
            {
                "filename": str(rel),
                "category": str(spec["category"]),
                "format": "WAV",
                "sample_rate": str(SAMPLE_RATE),
                "channels": "mono",
                "description": str(spec["description"]),
            }
        )

    write_wav(ROOT / "preview_all_20_ui_sfx.wav", normalize(preview, 0.72))
    ffmpeg = shutil.which("ffmpeg")
    if ffmpeg:
        subprocess.run(
            [
                ffmpeg,
                "-y",
                "-hide_banner",
                "-loglevel",
                "error",
                "-i",
                str(ROOT / "preview_all_20_ui_sfx.wav"),
                str(ROOT / "preview_all_20_ui_sfx.mp3"),
            ],
            check=True,
        )
    make_cover(ROOT / "cover.png")
    write_text_files(rows)

    with zipfile.ZipFile(ZIP_PATH, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(ROOT.rglob("*")):
            if path.is_file():
                zf.write(path, path.relative_to(ROOT.parent))


if __name__ == "__main__":
    make_pack()
