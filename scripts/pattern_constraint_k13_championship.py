#!/usr/bin/env python3
"""E0029 Main K13 pattern-constraint / spectral-rescue championship.

Stage isolation only: each replay K13 contains the five target winners plus eight
random nonwinner decoys. All C(13,5)=1,287 lines are enumerated. Features for a
target use only prior Main Mechanical-Era draws.

Primary shadow architecture:
  Pattern-OR top 80% OR E0013 spectral top 5% -> spectral ranking.

This runner is discovery/backtest infrastructure. It does not grant production
hard-pruning authority.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import random
import statistics
from collections import Counter, defaultdict
from pathlib import Path

from oracle_k13_assembly_evolution import (
    MAIN_LEDGER,
    load_rows,
    midrank_percentiles,
    recency_line_score,
    recency_state,
)
from xtra_algorithm_championship import (
    frequency_line_score,
    spectral_embedding,
    spectral_line_score,
)

ACTIVE_START = "2026-06-02"
TOTAL_LINES = math.comb(50, 5)
DEFAULT_KAPPA = 20.0
DEFAULT_SEED = 20261201


def feature_value(line: tuple[int, ...], name: str) -> int:
    if name == "sld":
        return sum(n % 10 for n in line)
    if name == "sum":
        return sum(line)
    if name == "span":
        return line[-1] - line[0]
    raise KeyError(name)


def exact_feature_counts() -> dict[str, Counter[int]]:
    out = {"sld": Counter(), "sum": Counter(), "span": Counter()}
    for line in itertools.combinations(range(1, 51), 5):
        out["sld"][feature_value(line, "sld")] += 1
        out["sum"][feature_value(line, "sum")] += 1
        out["span"][feature_value(line, "span")] += 1
    for name, counts in out.items():
        if sum(counts.values()) != TOTAL_LINES:
            raise AssertionError(f"{name} exact counts do not sum to C(50,5)")
    return out


def conditional_delta_null(counts: Counter[int], previous_value: int) -> dict[int, float]:
    out: dict[int, float] = defaultdict(float)
    for value, ways in counts.items():
        out[abs(value - previous_value)] += ways / TOTAL_LINES
    return dict(out)


def residual_delta_ratios(
    training: list[dict],
    feature_name: str,
    exact_counts: Counter[int],
    kappa: float = DEFAULT_KAPPA,
) -> dict[int, float]:
    """Target-excluded residual ratios versus exact structural expectation.

    The empirical absolute-delta distribution is compared with the average exact
    null distribution induced by the historical source states. A Dirichlet-like
    kappa shrinkage pulls the empirical distribution back toward that exact null.
    """
    n = len(training) - 1
    if n <= 0:
        return {}
    observed: Counter[int] = Counter()
    expected: dict[int, float] = defaultdict(float)
    for i in range(1, len(training)):
        prev = tuple(training[i - 1]["main"])
        cur = tuple(training[i]["main"])
        prev_value = feature_value(prev, feature_name)
        cur_value = feature_value(cur, feature_name)
        observed[abs(cur_value - prev_value)] += 1
        for delta, prob in conditional_delta_null(exact_counts, prev_value).items():
            expected[delta] += prob

    ratios: dict[int, float] = {}
    for delta in set(expected) | set(observed):
        p0_avg = expected.get(delta, 0.0) / n
        if p0_avg <= 0.0:
            ratios[delta] = 1.0
            continue
        posterior = (observed.get(delta, 0) + kappa * p0_avg) / (n + kappa)
        ratios[delta] = posterior / p0_avg
    return ratios


def slot_null_prob(slot: int, coordinate: int) -> float:
    """Exact probability that sorted slot (0-based) equals coordinate."""
    if coordinate < slot + 1 or 50 - coordinate < 4 - slot:
        return 0.0
    return (
        math.comb(coordinate - 1, slot)
        * math.comb(50 - coordinate, 4 - slot)
        / TOTAL_LINES
    )


def hlr_state(x: int, previous: int) -> str:
    return "L" if x < previous else ("H" if x > previous else "R")


def structural_hlr(slot: int, previous: int) -> dict[str, float]:
    out = {"L": 0.0, "R": 0.0, "H": 0.0}
    for x in range(1, 51):
        out[hlr_state(x, previous)] += slot_null_prob(slot, x)
    return out


def slot_state_sequences(training: list[dict]) -> list[list[str]]:
    seqs = [[] for _ in range(5)]
    for i in range(1, len(training)):
        prev, cur = training[i - 1]["main"], training[i]["main"]
        for slot in range(5):
            seqs[slot].append(hlr_state(cur[slot], prev[slot]))
    return seqs


def current_directional_run(seq: list[str]) -> int:
    if not seq or seq[-1] == "R":
        return 0
    state = seq[-1]
    run = 1
    for value in reversed(seq[:-1]):
        if value != state:
            break
        run += 1
    return run


def run_before(seq: list[str], outcome_index: int) -> int:
    if outcome_index <= 0 or seq[outcome_index - 1] == "R":
        return 0
    state = seq[outcome_index - 1]
    run = 1
    j = outcome_index - 2
    while j >= 0 and seq[j] == state:
        run += 1
        j -= 1
    return run


def barp_probabilities(training: list[dict]) -> list[dict[str, float]]:
    """E0005 BARP exactly as declared in its protocol."""
    seqs = slot_state_sequences(training)
    previous = training[-1]["main"]
    result: list[dict[str, float]] = []
    for slot, seq in enumerate(seqs):
        p0 = structural_hlr(slot, previous[slot])
        run = current_directional_run(seq)
        if run == 0:
            result.append(p0)
            continue

        exact: list[str] = []
        pooled: list[str] = []
        for i, outcome in enumerate(seq):
            r = run_before(seq, i)
            if r > 0 and outcome in ("H", "L"):
                pooled.append(outcome)
                if r == run:
                    exact.append(outcome)
        sample = exact if len(exact) >= 3 else pooled
        c_h, c_l = sample.count("H"), sample.count("L")
        odds_emp = (c_h + 1.0) / (c_l + 1.0)
        structural_odds = p0["H"] / max(p0["L"], 1e-15)
        odds = odds_emp * structural_odds**0.6
        remaining = 1.0 - p0["R"]
        q_h = remaining * odds / (1.0 + odds)
        q_l = remaining / (1.0 + odds)
        result.append({"H": q_h, "L": q_l, "R": p0["R"]})
    return result


def hlr_residual_lookup(training: list[dict]) -> list[dict[str, float]]:
    previous = training[-1]["main"]
    q = barp_probabilities(training)
    out: list[dict[str, float]] = []
    for slot in range(5):
        p0 = structural_hlr(slot, previous[slot])
        out.append(
            {
                state: math.log(max(q[slot][state], 1e-15) / max(p0[state], 1e-15))
                for state in ("L", "R", "H")
            }
        )
    return out


def oracle_replay(
    rows: list[dict],
    reps: int,
    seed: int,
    kappa: float,
    pattern_keep: float = 0.80,
    spectral_rescue: float = 0.05,
    min_prior: int = 8,
) -> dict:
    rng = random.Random(seed)
    exact_counts = exact_feature_counts()
    methods = ("spectral", "dissent_or", "pattern_or", "primary")
    all_values = {name: [] for name in methods}
    gate_survival: list[float] = []
    gate_fraction: list[float] = []
    per_target = []

    for t in range(min_prior, len(rows)):
        training = rows[:t]
        target = tuple(rows[t]["main"])
        target_set = set(target)
        previous = tuple(rows[t - 1]["main"])
        emb, _A, ci, _cij, _eig = spectral_embedding(training)
        last = recency_state(training)
        hlookup = hlr_residual_lookup(training)
        ratios = {
            name: residual_delta_ratios(training, name, exact_counts[name], kappa)
            for name in ("sld", "sum", "span")
        }
        prev_features = {name: feature_value(previous, name) for name in ("sld", "sum", "span")}
        remaining = [n for n in range(1, 51) if n not in target_set]
        target_values = {name: [] for name in methods}
        target_gate = []
        target_fraction = []

        for _ in range(reps):
            universe = tuple(sorted(target_set | set(rng.sample(remaining, 8))))
            lines = list(itertools.combinations(universe, 5))
            winner_index = lines.index(tuple(sorted(target)))

            raw_frequency = [frequency_line_score(line, ci) for line in lines]
            raw_recency = [recency_line_score(line, last) for line in lines]
            raw_spectral = [spectral_line_score(line, emb) for line in lines]
            raw_hlr = []
            raw_feature = {name: [] for name in ("sld", "sum", "span")}

            for line in lines:
                raw_hlr.append(
                    sum(hlookup[slot][hlr_state(line[slot], previous[slot])] for slot in range(5))
                )
                for name in ("sld", "sum", "span"):
                    delta = abs(feature_value(line, name) - prev_features[name])
                    raw_feature[name].append(math.log(max(ratios[name].get(delta, 1.0), 1e-15)))

            pct_frequency = midrank_percentiles(raw_frequency)
            pct_recency = midrank_percentiles(raw_recency)
            pct_spectral = midrank_percentiles(raw_spectral)
            pct_hlr = midrank_percentiles(raw_hlr)
            pct_sld = midrank_percentiles(raw_feature["sld"])
            pct_sum = midrank_percentiles(raw_feature["sum"])
            pct_span = midrank_percentiles(raw_feature["span"])

            dissent_raw = [
                max(pct_frequency[i], pct_recency[i], pct_spectral[i]) for i in range(len(lines))
            ]
            pct_dissent = midrank_percentiles(dissent_raw)
            pattern_raw = [
                max(pct_hlr[i], pct_sld[i], pct_sum[i], pct_span[i]) for i in range(len(lines))
            ]
            pct_pattern = midrank_percentiles(pattern_raw)

            pattern_threshold = 1.0 - pattern_keep
            spectral_threshold = 1.0 - spectral_rescue
            gate = [
                pct_pattern[i] >= pattern_threshold or pct_spectral[i] >= spectral_threshold
                for i in range(len(lines))
            ]
            final_raw = [
                1.0 + pct_spectral[i] if gate[i] else pct_pattern[i] for i in range(len(lines))
            ]
            pct_final = midrank_percentiles(final_raw)

            values = {
                "spectral": pct_spectral[winner_index],
                "dissent_or": pct_dissent[winner_index],
                "pattern_or": pct_pattern[winner_index],
                "primary": pct_final[winner_index],
            }
            for name, value in values.items():
                all_values[name].append(value)
                target_values[name].append(value)
            target_gate.append(1.0 if gate[winner_index] else 0.0)
            target_fraction.append(sum(gate) / len(gate))
            gate_survival.append(target_gate[-1])
            gate_fraction.append(target_fraction[-1])

        per_target.append(
            {
                "date": rows[t]["date"],
                "mean_winner_percentile": {
                    name: statistics.mean(target_values[name]) for name in methods
                },
                "winner_gate_survival": statistics.mean(target_gate),
                "mean_fraction_lines_retained": statistics.mean(target_fraction),
            }
        )

    def method_summary(values: list[float]) -> dict:
        return {
            "mean_winner_percentile": statistics.mean(values),
            "median_winner_percentile": statistics.median(values),
            "above_median_rate": sum(v > 0.5 for v in values) / len(values),
            "top100_rate": sum(v >= 1.0 - 99.0 / 1286.0 for v in values) / len(values),
        }

    return {
        "targets": len(per_target),
        "reps_per_target": reps,
        "seed": seed,
        "kappa": kappa,
        "pattern_keep": pattern_keep,
        "spectral_rescue": spectral_rescue,
        "methods": {name: method_summary(all_values[name]) for name in methods},
        "winner_gate_survival": statistics.mean(gate_survival),
        "mean_fraction_lines_retained": statistics.mean(gate_fraction),
        "mean_fraction_lines_eliminated": 1.0 - statistics.mean(gate_fraction),
        "per_target": per_target,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reps", type=int, default=30)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    parser.add_argument("--kappa", type=float, default=DEFAULT_KAPPA)
    parser.add_argument("--pattern-keep", type=float, default=0.80)
    parser.add_argument("--spectral-rescue", type=float, default=0.05)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    rows = load_rows(MAIN_LEDGER, "main")
    if rows[0]["date"] < ACTIVE_START:
        raise ValueError("Pre-June Main row is forbidden in E0029")
    result = {
        "experiment_id": "E0029",
        "replay_label": "target_excluded_discovery_replay_not_prospective_confirmation",
        "main": oracle_replay(
            rows,
            reps=args.reps,
            seed=args.seed,
            kappa=args.kappa,
            pattern_keep=args.pattern_keep,
            spectral_rescue=args.spectral_rescue,
        ),
    }
    text = json.dumps(result, indent=2, sort_keys=True)
    if args.output:
        args.output.write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
