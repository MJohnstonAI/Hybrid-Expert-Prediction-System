#!/usr/bin/env python3
"""Run a randomized null-model baseline against a HEPS draw."""
from __future__ import annotations

import argparse
import json
import random
from collections import Counter
from pathlib import Path
from typing import Any

from validate_draws import DEFAULT_LEDGER, load_jsonl, validate_rows


def choose_target(rows: list[tuple[int, dict[str, Any]]], draw_id: int | None) -> dict[str, Any]:
    if draw_id is None:
        return rows[-1][1]
    for _, row in rows:
        if row["draw_id"] == draw_id:
            return row
    raise ValueError(f"draw_id not found in ledger: {draw_id}")


def random_ticket(rng: random.Random) -> tuple[list[int], int]:
    return sorted(rng.sample(range(1, 51), 5)), rng.randint(1, 16)


def simulate(target: dict[str, Any], trials: int, seed: int) -> dict[str, Any]:
    rng = random.Random(seed)
    target_main = set(target["main_numbers"])
    target_powerball = target["powerball"]
    main_hit_counts: Counter[int] = Counter()
    main_plus_powerball_counts: Counter[str] = Counter()

    for _ in range(trials):
        main_numbers, powerball = random_ticket(rng)
        main_hits = len(target_main.intersection(main_numbers))
        powerball_hit = powerball == target_powerball
        main_hit_counts[main_hits] += 1
        main_plus_powerball_counts[f"{main_hits}+PB{int(powerball_hit)}"] += 1

    def rate(count: int) -> float:
        return count / trials if trials else 0.0

    return {
        "model": "uniform_random_null_model",
        "trials": trials,
        "seed": seed,
        "target_draw": {
            "draw_id": target["draw_id"],
            "draw_date": target["draw_date"],
            "main_numbers": target["main_numbers"],
            "powerball": target["powerball"],
        },
        "main_hit_distribution": {str(hits): main_hit_counts[hits] for hits in range(0, 6)},
        "main_hit_rates": {str(hits): rate(main_hit_counts[hits]) for hits in range(0, 6)},
        "threshold_rates": {
            "main_hits_at_least_3": rate(sum(main_hit_counts[hits] for hits in range(3, 6))),
            "main_hits_at_least_4": rate(sum(main_hit_counts[hits] for hits in range(4, 6))),
            "main_hits_exactly_5": rate(main_hit_counts[5]),
        },
        "main_plus_powerball_distribution": dict(sorted(main_plus_powerball_counts.items())),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ledger", type=Path, default=DEFAULT_LEDGER, help=f"Ledger path. Defaults to {DEFAULT_LEDGER}")
    parser.add_argument("--draw-id", type=int, default=None, help="Target draw_id. Defaults to latest ledger row")
    parser.add_argument("--trials", type=int, default=100_000, help="Number of randomized tickets to simulate")
    parser.add_argument("--seed", type=int, default=20260704, help="Deterministic random seed")
    args = parser.parse_args()

    if args.trials <= 0:
        print("--trials must be a positive integer")
        return 2

    rows = load_jsonl(args.ledger)
    errors = validate_rows(rows)
    if errors:
        print("Refusing to simulate against an invalid ledger")
        for error in errors:
            print(f"- {error}")
        return 1

    try:
        target = choose_target(rows, args.draw_id)
    except ValueError as exc:
        print(exc)
        return 1

    print(json.dumps(simulate(target, args.trials, args.seed), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
