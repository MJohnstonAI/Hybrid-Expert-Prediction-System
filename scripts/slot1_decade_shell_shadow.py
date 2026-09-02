#!/usr/bin/env python3
"""E0023 Main Slot1-anchored decade-shell diagnostic shadow.

Main-only. No pre-June 2026 history. The score is an exact-null-residualized
conditional decade-shell recurrence given the sorted minimum (Slot1).
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import random
import statistics
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LEDGER = ROOT / "data" / "draw_history.jsonl"
TOTAL_LINES = math.comb(50, 5)
KAPPA = 20.0
SEED = 20260902


def decade_shell(line):
    counts = [0, 0, 0, 0, 0]
    for number in line:
        counts[(number - 1) // 10] += 1
    return tuple(counts)


def state(line):
    values = tuple(sorted(line))
    return values[0], decade_shell(values)


def _weak_compositions(total=5, parts=5):
    for values in itertools.product(range(total + 1), repeat=parts):
        if sum(values) == total:
            yield values


def exact_joint_null_count(slot1, shell):
    if slot1 < 1 or slot1 > 46 or len(shell) != 5 or sum(shell) != 5:
        return 0
    decade = (slot1 - 1) // 10
    if any(shell[d] for d in range(decade)) or shell[decade] < 1:
        return 0
    count = 1
    for d in range(5):
        need = shell[d] - (1 if d == decade else 0)
        if need < 0:
            return 0
        if d < decade:
            available = 0
        elif d == decade:
            available = (d + 1) * 10 - slot1
        else:
            available = 10
        if need > available:
            return 0
        count *= math.comb(available, need)
    return count


def exact_null_tables():
    joint = Counter()
    slot1 = Counter()
    shell = Counter()
    for minimum in range(1, 47):
        for signature in _weak_compositions():
            count = exact_joint_null_count(minimum, signature)
            if count:
                joint[(minimum, signature)] = count
                slot1[minimum] += count
                shell[signature] += count
    if sum(joint.values()) != TOTAL_LINES:
        raise AssertionError("exact null table does not sum to C(50,5)")
    return joint, slot1, shell


NULL_JOINT, NULL_SLOT1, NULL_SHELL = exact_null_tables()


def load_rows(path=DEFAULT_LEDGER):
    rows = []
    for raw in Path(path).read_text(encoding="utf-8").splitlines():
        if not raw.strip():
            continue
        row = json.loads(raw)
        if row["draw_date"] < "2026-06-02":
            raise ValueError("E0023 forbids pre-June 2026 history")
        mains = tuple(int(x) for x in row["main_numbers"])
        if tuple(sorted(mains)) != mains or len(set(mains)) != 5:
            raise ValueError(f"invalid Main line: {mains}")
        rows.append({"date": row["draw_date"], "main": mains})
    return rows


def conditional_shell_score(line, training, kappa=KAPPA):
    minimum, signature = state(line)
    null_joint = NULL_JOINT[(minimum, signature)]
    null_minimum = NULL_SLOT1[minimum]
    if not null_joint or not null_minimum:
        return float("-inf")
    p0 = null_joint / null_minimum
    state_counts = Counter(state(row["main"]) for row in training)
    minimum_counts = Counter(row["main"][0] for row in training)
    observed_state = state_counts[(minimum, signature)]
    observed_minimum = minimum_counts[minimum]
    phat = (observed_state + kappa * p0) / (observed_minimum + kappa)
    return math.log(phat / p0)


def _midrank_percentile(scores, winner_index):
    target = scores[winner_index]
    lower = sum(score < target - 1e-12 for score in scores)
    tied = sum(abs(score - target) <= 1e-12 for score in scores)
    return (lower + (tied - 1) / 2.0) / max(1, len(scores) - 1)


def oracle_audit(rows, reps=30, min_prior=8, seed=SEED):
    rng = random.Random(seed)
    all_values = []
    per_target = []
    for t in range(min_prior, len(rows)):
        training = rows[:t]
        target = rows[t]["main"]
        target_set = set(target)
        remaining = [n for n in range(1, 51) if n not in target_set]
        target_values = []
        for _ in range(reps):
            universe = tuple(sorted(target_set | set(rng.sample(remaining, 8))))
            lines = list(itertools.combinations(universe, 5))
            winner_index = lines.index(target)
            scores = [conditional_shell_score(line, training) for line in lines]
            target_values.append(_midrank_percentile(scores, winner_index))
        mean_value = statistics.mean(target_values)
        all_values.extend(target_values)
        per_target.append({"date": rows[t]["date"], "mean_winner_percentile": mean_value})
    target_means = [row["mean_winner_percentile"] for row in per_target]
    return {
        "targets": len(per_target),
        "reps_per_target": reps,
        "mean_winner_percentile": statistics.mean(all_values),
        "median_target_mean_percentile": statistics.median(target_means),
        "targets_above_0_5": sum(value > 0.5 for value in target_means),
        "minimum_target_mean_percentile": min(target_means),
        "maximum_target_mean_percentile": max(target_means),
        "per_target": per_target,
    }


def rank_candidates(candidates, training, topn=20):
    values = tuple(sorted(set(candidates)))
    if len(values) < 5:
        raise ValueError("at least five unique candidates required")
    lines = list(itertools.combinations(values, 5))
    scored = sorted(((conditional_shell_score(line, training), line) for line in lines), reverse=True)
    return [{"line": list(line), "score": score, "state": [line[0], list(decade_shell(line))]} for score, line in scored[:topn]]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ledger", type=Path, default=DEFAULT_LEDGER)
    parser.add_argument("--reps", type=int, default=30)
    parser.add_argument("--candidates", help="comma-separated frozen candidate universe")
    parser.add_argument("--topn", type=int, default=20)
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    rows = load_rows(args.ledger)
    result = {
        "experiment_id": "E0023",
        "evidence": "INSUFFICIENT_EVIDENCE",
        "kappa": KAPPA,
        "active_start": "2026-06-02",
        "oracle_audit": oracle_audit(rows, reps=args.reps),
    }
    if args.candidates:
        candidates = [int(x.strip()) for x in args.candidates.split(",") if x.strip()]
        result["current_shadow_top_lines"] = rank_candidates(candidates, rows, args.topn)
    text = json.dumps(result, indent=2)
    if args.out:
        args.out.write_text(text + "\n", encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
