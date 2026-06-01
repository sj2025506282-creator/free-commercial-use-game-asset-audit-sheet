#!/usr/bin/env python3
"""Strict technical audit for the 20-file UI SFX free pack."""

from __future__ import annotations

import argparse
import csv
import json
import math
import wave
import zipfile
from pathlib import Path


def wav_stats(path: Path) -> dict[str, object]:
    with wave.open(str(path), "rb") as wav:
        frames = wav.readframes(wav.getnframes())
        values = [
            int.from_bytes(frames[i : i + 2], "little", signed=True)
            for i in range(0, len(frames), 2)
        ]
        peak = max((abs(v) for v in values), default=0)
        rms = math.sqrt(sum(v * v for v in values) / max(1, len(values))) / 32768
        zero_crossings = sum(
            1
            for left, right in zip(values, values[1:])
            if (left < 0 <= right) or (right < 0 <= left)
        )
        return {
            "channels": wav.getnchannels(),
            "sample_rate": wav.getframerate(),
            "sample_width": wav.getsampwidth(),
            "frames": wav.getnframes(),
            "duration": wav.getnframes() / wav.getframerate(),
            "peak_int16": peak,
            "peak_dbfs": round(20 * math.log10(max(1, peak) / 32768), 2),
            "rms": round(rms, 5),
            "zero_crossing_rate": round(zero_crossings / max(1, len(values)), 5),
        }


def fail_unless(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pack_dir", type=Path)
    parser.add_argument("--zip", type=Path, required=True)
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args()

    root = args.pack_dir
    failures: list[str] = []
    warnings: list[str] = []
    wavs = sorted((root / "audio" / "wav").glob("**/*.wav"))
    stats = {str(path.relative_to(root)): wav_stats(path) for path in wavs}
    categories: dict[str, int] = {}
    for path in wavs:
        category = path.relative_to(root).parts[2]
        categories[category] = categories.get(category, 0) + 1

    required = ["README.txt", "LICENSE.txt", "FILE_LIST.csv", "GUMROAD_COPY.txt", "cover.png"]
    for filename in required:
        fail_unless((root / filename).exists(), f"missing required file: {filename}", failures)

    fail_unless(len(wavs) == 20, f"expected exactly 20 WAV files, found {len(wavs)}", failures)
    fail_unless(set(categories) == {"confirm", "error", "notification", "select"}, f"unexpected categories: {categories}", failures)
    fail_unless(all(count == 5 for count in categories.values()), f"expected 5 files per category: {categories}", failures)
    fail_unless(all(item["channels"] == 1 for item in stats.values()), "not all WAV files are mono", failures)
    fail_unless(all(item["sample_rate"] == 48000 for item in stats.values()), "not all WAV files are 48 kHz", failures)
    fail_unless(all(item["sample_width"] == 2 for item in stats.values()), "not all WAV files are 16-bit", failures)
    fail_unless(all(0.05 <= float(item["duration"]) <= 0.7 for item in stats.values()), "some UI WAV durations are outside 0.05s-0.7s", failures)
    fail_unless(all(int(item["peak_int16"]) <= 29000 for item in stats.values()), "some WAV peaks are too close to clipping", failures)
    fail_unless(all(float(item["rms"]) >= 0.015 for item in stats.values()), "some WAV files are nearly silent", failures)
    fail_unless(all(float(item["zero_crossing_rate"]) > 0.005 for item in stats.values()), "some WAV files appear too static", failures)

    preview_wav = root / "preview_all_20_ui_sfx.wav"
    preview_mp3 = root / "preview_all_20_ui_sfx.mp3"
    fail_unless(preview_wav.exists(), "missing preview WAV", failures)
    if not preview_mp3.exists():
        warnings.append("missing preview MP3")

    file_list = root / "FILE_LIST.csv"
    if file_list.exists():
        rows = list(csv.DictReader(file_list.open(encoding="utf-8")))
        listed = {row.get("filename", "") for row in rows}
        actual = {str(path.relative_to(root)) for path in wavs}
        fail_unless(listed == actual, "FILE_LIST.csv does not exactly match WAV files", failures)

    fail_unless(args.zip.exists(), f"missing ZIP: {args.zip}", failures)
    if args.zip.exists():
        with zipfile.ZipFile(args.zip) as zf:
            names = zf.namelist()
        fail_unless(sum(name.endswith(".wav") for name in names) >= 21, "ZIP missing WAV or preview files", failures)
        fail_unless(any(name.endswith("README.txt") for name in names), "ZIP missing README", failures)
        fail_unless(any(name.endswith("LICENSE.txt") for name in names), "ZIP missing LICENSE", failures)
        fail_unless(any(name.endswith("cover.png") for name in names), "ZIP missing cover", failures)

    total_duration = sum(float(item["duration"]) for item in stats.values())
    report = {
        "pack_dir": str(root),
        "zip": str(args.zip),
        "status": "pass" if not failures else "fail",
        "failures": failures,
        "warnings": warnings,
        "summary": {
            "wav_count": len(wavs),
            "category_count": len(categories),
            "categories": categories,
            "total_duration_seconds": round(total_duration, 3),
            "min_duration_seconds": round(min((float(item["duration"]) for item in stats.values()), default=0), 3),
            "max_duration_seconds": round(max((float(item["duration"]) for item in stats.values()), default=0), 3),
            "max_peak_dbfs": max((float(item["peak_dbfs"]) for item in stats.values()), default=None),
        },
    }
    print(json.dumps(report, ensure_ascii=False, indent=2 if args.pretty else None))
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
