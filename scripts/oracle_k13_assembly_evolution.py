#!/usr/bin/env python3
"""E0022 oracle-K13 assembly evolution runner.

Stage-isolation only. It assumes the frozen K13 already contains all five target
winners, adds eight random decoys, enumerates all C(13,5)=1287 lines, and scores
coalition ranking without giving any candidate-acquisition credit.

Main and XTRA state are fitted separately. Pre-June 2026 rows are forbidden.
Discrete scores use average midranks; treating every tied line as best-in-tie is
reported only as a diagnostic because it inflates oracle percentiles.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import random
import statistics
from pathlib import Path

from xtra_algorithm_championship import (
    frequency_line_score,
    raw_pair_score,
    spectral_embedding,
    spectral_line_score,
)

ROOT = Path(__file__).resolve().parents[1]
MAIN_LEDGER = ROOT / "data" / "draw_history.jsonl"
XTRA_LEDGER = ROOT / "data" / "powerball_xtra_history.jsonl"
SEED = 20260902


def load_rows(path: Path, variant: str) -> list[dict]:
    rows = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw.strip():
            continue
        row = json.loads(raw)
        if row["draw_date"] < "2026-06-02":
            raise ValueError("pre-June row is forbidden in E0022")
        if variant == "xtra" and row.get("game_variant") != "powerball_xtra":
            raise ValueError("non-XTRA row in XTRA ledger")
        rows.append({"date": row["draw_date"], "main": tuple(row["main_numbers"])})
    return rows


def load_supplement(path: Path | None) -> list[dict]:
    if path is None:
        return []
    rows = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw.strip():
            continue
        row = json.loads(raw)
        if row.get("status") != "noncanonical_external_replay_only":
            raise ValueError("supplement must be explicitly noncanonical replay data")
        rows.append({"date": row["draw_date"], "main": tuple(row["main_numbers"])})
    return rows


def midrank_percentiles(scores: list[float]) -> list[float]:
    """Higher-is-better percentiles with average ranks for ties."""
    n = len(scores)
    if n <= 1:
        return [1.0] * n
    order = sorted(range(n), key=lambda i: (scores[i], i))
    out = [0.0] * n
    start = 0
    while start < n:
        end = start + 1
        value = scores[order[start]]
        while end < n and math.isclose(scores[order[end]], value, rel_tol=0.0, abs_tol=1e-12):
            end += 1
        # 1-based average rank converted to 0..1 percentile.
        avg_rank = ((start + 1) + end) / 2.0
        pct = (avg_rank - 1.0) / (n - 1)
        for pos in range(start, end):
            out[order[pos]] = pct
        start = end
    return out


def optimistic_best_tie_percentile(scores: list[float], winner_index: int) -> float:
    """Historical diagnostic only: gives every tied line best rank in its tie."""
    target = scores[winner_index]
    greater = sum(score > target for score in scores)
    return 1.0 - greater / max(1, len(scores) - 1)


def recency_state(training: list[dict]) -> dict[int, float]:
    last = {n: -10000.0 for n in range(1, 51)}
    for i, row in enumerate(training):
        for n in row["main"]:
            last[n] = float(i)
    return last


def recency_line_score(line: tuple[int, ...], last: dict[int, float]) -> float:
    return sum(last[n] for n in line)


def oracle_game(rows: list[dict], reps: int, min_prior: int = 8, seed: int = SEED) -> dict:
    rng = random.Random(seed)
    methods = ("frequency", "recency", "raw_pair", "spectral", "dissent_or")
    values = {name: [] for name in methods}
    optimistic_pair = []
    per_target = []

    for t in range(min_prior, len(rows)):
        training = rows[:t]
        target = tuple(rows[t]["main"])
        target_set = set(target)
        emb, _A, ci, cij, _eig = spectral_embedding(training)
        last = recency_state(training)
        remaining = [n for n in range(1, 51) if n not in target_set]
        target_values = {name: [] for name in methods}

        for _ in range(reps):
            universe = tuple(sorted(target_set | set(rng.sample(remaining, 8))))
            lines = list(itertools.combinations(universe, 5))
            winner_index = lines.index(tuple(sorted(target)))

            raw_scores = {
                "frequency": [frequency_line_score(line, ci) for line in lines],
                "recency": [recency_line_score(line, last) for line in lines],
                "raw_pair": [raw_pair_score(line, cij) for line in lines],
                "spectral": [spectral_line_score(line, emb) for line in lines],
            }
            pct = {name: midrank_percentiles(scores) for name, scores in raw_scores.items()}
            dissent = [max(pct["frequency"][i], pct["recency"][i], pct["spectral"][i]) for i in range(len(lines))]
            pct["dissent_or"] = midrank_percentiles(dissent)

            for name in methods:
                winner_pct = pct[name][winner_index]
                values[name].append(winner_pct)
                target_values[name].append(winner_pct)
            optimistic_pair.append(optimistic_best_tie_percentile(raw_scores["raw_pair"], winner_index))

        per_target.append({
            "date": rows[t]["date"],
            "mean_winner_percentile": {name: statistics.mean(target_values[name]) for name in methods},
        })

    return {
        "targets": len(per_target),
        "reps_per_target": reps,
        "mean_winner_percentile": {name: statistics.mean(values[name]) for name in methods},
        "raw_pair_optimistic_best_tie_mean": statistics.mean(optimistic_pair),
        "raw_pair_midrank_mean": statistics.mean(values["raw_pair"]),
        "per_target": per_target,
    }


def four_plus_cover(candidate_count: int, budget: int) -> dict:
    lines = list(itertools.combinations(range(candidate_count), 5))
    sets = [set(line) for line in lines]
    cover4 = []
    for line_set in sets:
        cover4.append({j for j, winner in enumerate(sets) if len(line_set & winner) >= 4})
    chosen = []
    covered: set[int] = set()
    remaining = set(range(len(lines)))
    for _ in range(min(budget, len(lines))):
        best = max(remaining, key=lambda i: (len(cover4[i] - covered), tuple(-n for n in lines[i])))
        chosen.append(best)
        covered.update(cover4[best])
        remaining.remove(best)
    total = len(lines)
    no_cover = 1.0
    radius = len(cover4[0])
    for j in range(len(chosen)):
        no_cover *= (total - radius - j) / (total - j)
    random_expected = 1.0 - no_cover
    return {
        "candidate_count": candidate_count,
        "budget": len(chosen),
        "winner_states": total,
        "covered_4plus": len(covered),
        "four_plus_fraction": len(covered) / total,
        "random_distinct_expected_fraction": random_expected,
        "exact_5of5_fraction": len(chosen) / total,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--reps", type=int, default=30)
    ap.add_argument("--xtra-supplement", type=Path)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    main_rows = load_rows(MAIN_LEDGER, "main")
    xtra_rows = load_rows(XTRA_LEDGER, "xtra") + load_supplement(args.xtra_supplement)
    xtra_rows.sort(key=lambda row: row["date"])

    result = {
        "experiment_id": "E0022",
        "rank_ties": "average_midrank",
        "main": oracle_game(main_rows, args.reps, seed=SEED),
        "xtra": oracle_game(xtra_rows, args.reps, seed=SEED + 1),
        "johnson_four_plus_first": [four_plus_cover(13, budget) for budget in (5, 10, 20, 30, 50)],
        "warning": "Post-hoc discovery replay; no predictive BREAKTHROUGH authority.",
    }
    text = json.dumps(result, indent=2, sort_keys=True)
    if args.output:
        args.output.write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
