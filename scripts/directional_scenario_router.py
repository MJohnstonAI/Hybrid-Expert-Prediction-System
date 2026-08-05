#!/usr/bin/env python3
"""Exact H/L/R null-geometry router for HEPS v33.4.

This module computes the fair combinatorial H/L/R probabilities for each sorted
main-number slot in a 5-of-50 draw and for the 1-of-16 PowerBall.  It is a
benchmark/router, not a predictive-edge claim.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LEDGER = REPO_ROOT / "data" / "draw_history.jsonl"
TOTAL_MAIN = math.comb(50, 5)


def load_rows(path: Path) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    if not rows:
        raise ValueError("ledger is empty")
    return rows


def slot_value_probability(slot_index: int, value: int) -> float:
    """Probability that sorted slot 1..5 equals value in a fair 5-of-50 draw."""
    j = slot_index
    if not (1 <= j <= 5 and 1 <= value <= 50):
        return 0.0
    left = j - 1
    right = 5 - j
    if value - 1 < left or 50 - value < right:
        return 0.0
    return math.comb(value - 1, left) * math.comb(50 - value, right) / TOTAL_MAIN


def main_direction_probabilities(slot_index: int, current_value: int) -> dict[str, float]:
    lower = sum(slot_value_probability(slot_index, x) for x in range(1, current_value))
    repeat = slot_value_probability(slot_index, current_value)
    higher = sum(slot_value_probability(slot_index, x) for x in range(current_value + 1, 51))
    return {"L": lower, "R": repeat, "H": higher}


def powerball_direction_probabilities(current_pb: int) -> dict[str, float]:
    if not 1 <= current_pb <= 16:
        raise ValueError("PowerBall must be in 1..16")
    return {
        "L": (current_pb - 1) / 16,
        "R": 1 / 16,
        "H": (16 - current_pb) / 16,
    }


def modal_state(probabilities: dict[str, float]) -> str:
    # Deterministic tie-breaker keeps the benchmark reproducible.
    order = {"L": 0, "R": 1, "H": 2}
    return max(probabilities, key=lambda state: (probabilities[state], -order[state]))


def analyze(latest: dict[str, Any]) -> dict[str, Any]:
    main = latest["main_numbers"]
    if len(main) != 5 or sorted(main) != main:
        raise ValueError("latest main_numbers must be five ascending values")

    main_slots = []
    template = []
    for slot_index, current_value in enumerate(main, start=1):
        probs = main_direction_probabilities(slot_index, current_value)
        state = modal_state(probs)
        template.append(state)
        main_slots.append(
            {
                "slot": slot_index,
                "current_value": current_value,
                "probabilities": {key: round(value, 8) for key, value in probs.items()},
                "modal_state": state,
            }
        )

    pb_probs = powerball_direction_probabilities(latest["powerball"])
    return {
        "draw_date": latest["draw_date"],
        "current_main": main,
        "current_powerball": latest["powerball"],
        "main_slots": main_slots,
        "null_geometry_template": template,
        "powerball_probabilities": {key: round(value, 8) for key, value in pb_probs.items()},
        "powerball_modal_state": modal_state(pb_probs),
        "evidence_boundary": "Exact fair combinatorial benchmark only; not evidence of predictive edge.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ledger", type=Path, default=DEFAULT_LEDGER)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    result = analyze(load_rows(args.ledger)[-1])
    rendered = json.dumps(result, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)


if __name__ == "__main__":
    main()
