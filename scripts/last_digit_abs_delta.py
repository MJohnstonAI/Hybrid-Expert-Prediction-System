#!/usr/bin/env python3
"""HEPS E0028 Last-Digit Sum Absolute-Delta (LDSAD) analysis.

Reads a Mechanical-Era JSONL ledger, computes draw-level sums of last digits,
consecutive absolute changes, an observed frequency pivot, and the exact IID
5-of-50 null distribution. Standard library only.

Example:
  python scripts/last_digit_abs_delta.py \
    --ledger data/draw_history.jsonl \
    --bands 11-13,10-13,9-13

For XTRA, point --ledger at the canonical XTRA Mechanical-Era ledger and do
NOT assume the Main-fitted 11-13 band has authority. Derive/freeze XTRA bands
under its own protocol.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter, defaultdict
from pathlib import Path

ACTIVE_START = "2026-06-02"
TOTAL_LEGAL_LINES = math.comb(50, 5)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--ledger", required=True, help="JSONL ledger with main_numbers and draw_date")
    p.add_argument(
        "--bands",
        default="",
        help="Comma-separated inclusive integer bands, e.g. 11-13,10-13,9-13",
    )
    return p.parse_args()


def parse_bands(text: str) -> list[tuple[int, int]]:
    out: list[tuple[int, int]] = []
    if not text.strip():
        return out
    for token in text.split(","):
        lo_s, hi_s = token.strip().split("-", 1)
        lo, hi = int(lo_s), int(hi_s)
        if lo > hi:
            raise ValueError(f"Invalid band {token}: lower bound exceeds upper bound")
        out.append((lo, hi))
    return out


def read_ledger(path: Path) -> list[dict]:
    rows: list[dict] = []
    with path.open("r", encoding="utf-8") as fh:
        for line in fh:
            if not line.strip():
                continue
            row = json.loads(line)
            date = row.get("draw_date")
            nums = row.get("main_numbers")
            if date is None or nums is None:
                raise ValueError("Each row requires draw_date and main_numbers")
            if date < ACTIVE_START:
                raise ValueError(f"Pre-Mechanical-Era row rejected: {date}")
            if len(nums) != 5 or len(set(nums)) != 5 or any(not (1 <= n <= 50) for n in nums):
                raise ValueError(f"Invalid 5/50 main_numbers at {date}: {nums}")
            rows.append(row)
    rows.sort(key=lambda r: r["draw_date"])
    if len(rows) < 2:
        raise ValueError("Need at least two draws")
    return rows


def sld(nums: list[int]) -> int:
    return sum(n % 10 for n in nums)


def exact_sld_counts() -> Counter[int]:
    """Exact SLD counts over all C(50,5) lines via residue-class DP.

    In 1..50 every terminal digit 0..9 occurs exactly five times.
    DP state is (numbers_selected, last_digit_sum) -> number of legal subsets.
    """
    dp: dict[tuple[int, int], int] = {(0, 0): 1}
    for residue in range(10):
        nxt: dict[tuple[int, int], int] = defaultdict(int)
        for (k, total), ways in dp.items():
            for take in range(0, min(5, 5 - k) + 1):
                nxt[(k + take, total + take * residue)] += ways * math.comb(5, take)
        dp = dict(nxt)
    counts = Counter({total: ways for (k, total), ways in dp.items() if k == 5})
    if sum(counts.values()) != TOTAL_LEGAL_LINES:
        raise AssertionError("Exact SLD DP does not sum to C(50,5)")
    return counts


def exact_delta_probs() -> dict[int, float]:
    counts = exact_sld_counts()
    probs = {s: c / TOTAL_LEGAL_LINES for s, c in counts.items()}
    delta: dict[int, float] = defaultdict(float)
    for a, pa in probs.items():
        for b, pb in probs.items():
            delta[abs(a - b)] += pa * pb
    return dict(delta)


def main() -> None:
    args = parse_args()
    bands = parse_bands(args.bands)
    rows = read_ledger(Path(args.ledger))

    slds = [sld(list(map(int, r["main_numbers"]))) for r in rows]
    deltas = [abs(slds[i] - slds[i - 1]) for i in range(1, len(slds))]
    obs = Counter(deltas)
    null = exact_delta_probs()
    n = len(deltas)

    pivot = []
    for d in sorted(obs, reverse=True):
        observed_rate = obs[d] / n
        null_rate = null.get(d, 0.0)
        pivot.append(
            {
                "delta": d,
                "count": obs[d],
                "observed_rate": observed_rate,
                "exact_iid_null_rate": null_rate,
                "observed_null_lift": observed_rate / null_rate if null_rate else None,
            }
        )

    band_rows = []
    for lo, hi in bands:
        count = sum(1 for d in deltas if lo <= d <= hi)
        observed_rate = count / n
        null_rate = sum(null.get(d, 0.0) for d in range(lo, hi + 1))
        band_rows.append(
            {
                "band": [lo, hi],
                "count": count,
                "observed_rate": observed_rate,
                "exact_iid_null_rate": null_rate,
                "observed_null_lift": observed_rate / null_rate if null_rate else None,
                "warning": "Post-hoc selected bands require multiplicity accounting and prospective freeze.",
            }
        )

    result = {
        "statistic": "LAST_DIGIT_SUM_ABS_DELTA",
        "active_start": ACTIVE_START,
        "ledger": str(args.ledger),
        "draws": len(rows),
        "transitions": n,
        "first_draw": rows[0]["draw_date"],
        "last_draw": rows[-1]["draw_date"],
        "sld_sequence": slds,
        "ldsad_sequence": deltas,
        "pivot_descending_delta": pivot,
        "bands": band_rows,
        "exact_null": {
            "legal_lines": TOTAL_LEGAL_LINES,
            "method": "exact residue-class DP for SLD, independent-draw convolution for absolute delta",
        },
    }
    print(json.dumps(result, indent=2, sort_keys=False))


if __name__ == "__main__":
    main()
