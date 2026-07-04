#!/usr/bin/env python3
"""
Append a new HEPS draw row to data/draw_history.jsonl after validation.

Usage:
    python scripts/append_draw.py 2026-07-03 1,2,3,4,5 11
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from datetime import date

LEDGER = Path("data/draw_history.jsonl")


def read_rows():
    if not LEDGER.exists():
        return []
    rows = []
    for line in LEDGER.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            rows.append(json.loads(line))
    return rows


def append_draw(draw_date: str, main_csv: str, pb: str):
    date.fromisoformat(draw_date)
    main = sorted(int(x.strip()) for x in main_csv.split(","))
    pb_int = int(pb)

    if len(main) != 5 or len(set(main)) != 5:
        raise ValueError("main numbers must contain five unique values")
    if any(n < 1 or n > 50 for n in main):
        raise ValueError("main numbers must be between 1 and 50")
    if pb_int < 1 or pb_int > 16:
        raise ValueError("powerball must be between 1 and 16")

    rows = read_rows()
    if any(r["draw_date"] == draw_date for r in rows):
        raise ValueError(f"draw_date already exists: {draw_date}")

    next_id = max([r.get("draw_id", 0) for r in rows] or [0]) + 1
    row = {
        "draw_id": next_id,
        "draw_date": draw_date,
        "main": main,
        "powerball": pb_int,
        "macro_sum": sum(main),
        "regime": "mechanical_50_16",
        "source_url": None,
        "machine_name": None,
    }

    with LEDGER.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, separators=(",", ":")) + "\n")

    print(json.dumps(row, indent=2))


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(__doc__)
        raise SystemExit(2)
    append_draw(sys.argv[1], sys.argv[2], sys.argv[3])
