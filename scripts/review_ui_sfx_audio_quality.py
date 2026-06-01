#!/usr/bin/env python3
"""Automated listenability review for short UI SFX WAV files."""

from __future__ import annotations

import argparse
import csv
import json
import math
import statistics
import wave
from pathlib import Path


def read_wav(path: Path) -> tuple[int, list[float]]:
    with wave.open(str(path), "rb") as wav:
        sample_rate = wav.getframerate()
        raw = wav.readframes(wav.getnframes())
    values = [
        int.from_bytes(raw[i : i + 2], "little", signed=True) / 32768
        for i in range(0, len(raw), 2)
    ]
    return sample_rate, values


def rms(values: list[float]) -> float:
    return math.sqrt(sum(v * v for v in values) / max(1, len(values)))


def dbfs(value: float) -> float:
    return 20 * math.log10(max(value, 1e-9))


def zero_crossing_rate(values: list[float]) -> float:
    return sum(
        1
        for left, right in zip(values, values[1:])
        if (left < 0 <= right) or (right < 0 <= left)
    ) / max(1, len(values))


def spectral_centroid(values: list[float], sample_rate: int) -> float:
    try:
        import numpy as np
    except Exception:
        return -1
    arr = np.array(values, dtype=float)
    if arr.size < 16:
        return 0
    window = np.hanning(arr.size)
    spectrum = np.abs(np.fft.rfft(arr * window))
    freqs = np.fft.rfftfreq(arr.size, d=1 / sample_rate)
    total = spectrum.sum()
    if total <= 1e-9:
        return 0
    return float((freqs * spectrum).sum() / total)


def review_file(path: Path) -> dict[str, object]:
    sample_rate, samples = read_wav(path)
    duration = len(samples) / sample_rate
    peak = max((abs(v) for v in samples), default=0)
    full_rms = rms(samples)
    tail_len = max(1, int(0.025 * sample_rate))
    head_len = max(1, int(0.006 * sample_rate))
    tail_rms = rms(samples[-tail_len:])
    head_rms = rms(samples[:head_len])
    centroid = spectral_centroid(samples, sample_rate)
    zcr = zero_crossing_rate(samples)

    issues: list[str] = []
    if not (0.05 <= duration <= 0.7):
        issues.append("duration_outside_ui_range")
    if peak > 0.89:
        issues.append("peak_too_hot")
    if peak < 0.18:
        issues.append("peak_too_low")
    if full_rms < 0.018:
        issues.append("too_quiet")
    if tail_rms > full_rms * 0.45 and tail_rms > 0.025:
        issues.append("tail_may_be_abrupt_or_too_loud")
    if head_rms > full_rms * 1.2 and peak > 0.75:
        issues.append("attack_may_click")
    if centroid >= 0 and not (180 <= centroid <= 6000):
        issues.append("spectral_centroid_outside_expected_ui_range")
    if zcr < 0.005:
        issues.append("too_static")

    return {
        "file": str(path),
        "duration": round(duration, 4),
        "peak_dbfs": round(dbfs(peak), 2),
        "rms_dbfs": round(dbfs(full_rms), 2),
        "tail_rms_dbfs": round(dbfs(tail_rms), 2),
        "zero_crossing_rate": round(zcr, 5),
        "spectral_centroid_hz": round(centroid, 1),
        "issues": issues,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pack_dir", type=Path)
    parser.add_argument("--out", type=Path)
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args()

    wavs = sorted((args.pack_dir / "audio" / "wav").glob("**/*.wav"))
    results = [review_file(path) for path in wavs]
    issue_files = [item for item in results if item["issues"]]
    durations = [float(item["duration"]) for item in results]
    rms_values = [float(item["rms_dbfs"]) for item in results]
    centroids = [float(item["spectral_centroid_hz"]) for item in results]
    report = {
        "pack_dir": str(args.pack_dir),
        "status": "pass" if not issue_files else "review_needed",
        "file_count": len(results),
        "issue_file_count": len(issue_files),
        "summary": {
            "duration_min": round(min(durations), 4) if durations else None,
            "duration_max": round(max(durations), 4) if durations else None,
            "rms_dbfs_median": round(statistics.median(rms_values), 2) if rms_values else None,
            "spectral_centroid_hz_median": round(statistics.median(centroids), 1) if centroids else None,
        },
        "files_with_issues": issue_files,
    }
    text = json.dumps(report, ensure_ascii=False, indent=2 if args.pretty else None)
    print(text)
    if args.out:
        args.out.write_text(text + "\n", encoding="utf-8")
        csv_path = args.out.with_suffix(".csv")
        with csv_path.open("w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=list(results[0].keys()))
            writer.writeheader()
            writer.writerows(results)
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
