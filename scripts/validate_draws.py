#!/usr/bin/env python3
"""
Validate the HEPS canonical draw ledger.

Usage:
    python scripts/validate_draws.py data/draw_history.jsonl
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from datetime import date


def load_jsonl(path: Path):
    rows = []
    with path.open("r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            try:
                rows.append((line_no, json.loads(stripped)))
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON on line {line_no}: {exc}") from exc
    return rows


def validate(path: Path) -> int:
    rows = load_jsonl(path)
    seen_dates = set()
    errors = []

    for line_no, row in rows:
        draw_date = row.get("draw_date")
        main = row.get("main")
        pb = row.get("powerball")
        macro_sum = row.get("macro_sum")

        try:
            date.fromisoformat(draw_date)
        except Exception:
            errors.append(f"Line {line_no}: invalid draw_date {draw_date!r}")

        if draw_date in seen_dates:
            errors.append(f"Line {line_no}: duplicate draw_date {draw_date}")
        seen_dates.add(draw_date)

        if not isinstance(main, list) or len(main) != 5:
            errors.append(f"Line {line_no}: main must be a list of five integers")
            continue

        if len(set(main)) != 5:
            errors.append(f"Line {line_no}: main numbers must be unique: {main}")

        if any((not isinstance(n, int) or n < 1 or n > 50) for n in main):
            errors.append(f"Line {line_no}: main numbers out of range 1-50: {main}")

        if main != sorted(main):
            errors.append(
                f"Line {line_no}: main numbers should be sorted ascending unless drawn-order data is explicitly represented: {main}"
            )

        if not isinstance(pb, int) or pb < 1 or pb > 16:
            errors.append(f"Line {line_no}: powerball out of range 1-16: {pb}")

        expected_sum = sum(main)
        if macro_sum != expected_sum:
            errors.append(f"Line {line_no}: macro_sum {macro_sum} != sum(main) {expected_sum}")

    if errors:
        print("HEPS draw ledger validation FAILED")
        for err in errors:
            print(f"- {err}")
        return 1

    print(f"HEPS draw ledger validation passed: {len(rows)} rows")
    return 0


if __name__ == "__main__":
    input_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("data/draw_history.jsonl")
    raise SystemExit(validate(input_path))
