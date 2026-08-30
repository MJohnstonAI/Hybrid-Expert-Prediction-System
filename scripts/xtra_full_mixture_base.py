#!/usr/bin/env python3
"""Build a full-support XTRA slot-probability base before residual experts.

The model never collapses to one HLR vector. It estimates per-slot HLR successor
probabilities from XTRA-only history, shrinks them to the exact 5/50
order-statistic HLR geometry, reweights every legal 5-of-50 combination, and
marginalizes back to slot/global probability fields.

The resulting ``slot_marginals`` object is directly consumable by
``scripts/physics_shadow_e0016.py xtra --base-slot-field ...``.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
from pathlib import Path
from typing import Dict, List, Sequence, Tuple

FIELD_N = 50
PICKS = 5
STATES = ("L", "R", "H")
EPS = 1e-15
ACTIVE_START = "2026-06-02"


def load_jsonl(path: str) -> List[dict]:
    rows: List[dict] = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                rows.append(json.loads(line))
    return rows


def main_numbers(row: dict) -> Tuple[int, ...]:
    nums = tuple(int(x) for x in row["main_numbers"])
    if len(nums) != PICKS or tuple(sorted(nums)) != nums or len(set(nums)) != PICKS:
        raise ValueError(f"invalid sorted main_numbers: {nums}")
    if nums[0] < 1 or nums[-1] > FIELD_N:
        raise ValueError(f"main number out of bounds: {nums}")
    return nums


def merge_rows(canonical: Sequence[dict], extension: Sequence[dict]) -> List[dict]:
    by_date: Dict[str, dict] = {}
    for source_name, rows in (("canonical", canonical), ("working_extension", extension)):
        for row in rows:
            date = str(row["draw_date"])
            if date < ACTIVE_START:
                continue
            if date in by_date:
                old = main_numbers(by_date[date])
                new = main_numbers(row)
                if old != new or int(by_date[date]["powerball"]) != int(row["powerball"]):
                    raise ValueError(f"conflicting duplicate draw_date {date}")
                continue
            copied = dict(row)
            copied["_state_source"] = source_name
            by_date[date] = copied
    rows = [by_date[d] for d in sorted(by_date)]
    for row in rows:
        main_numbers(row)
    return rows


def slot_pmf(slot: int) -> Dict[int, float]:
    den = math.comb(FIELD_N, PICKS)
    j = slot + 1
    out: Dict[int, float] = {}
    for n in range(1, FIELD_N + 1):
        if n - 1 < j - 1 or FIELD_N - n < PICKS - j:
            out[n] = 0.0
        else:
            out[n] = (
                math.comb(n - 1, j - 1)
                * math.comb(FIELD_N - n, PICKS - j)
                / den
            )
    return out


SLOT_PMFS = [slot_pmf(j) for j in range(PICKS)]


def hlr_state(previous: Sequence[int], current: Sequence[int]) -> Tuple[str, ...]:
    out = []
    for p, c in zip(previous, current):
        out.append("L" if c < p else "R" if c == p else "H")
    return tuple(out)


def structural_hlr_probs(slot: int, previous_coordinate: int) -> Dict[str, float]:
    probs = {s: 0.0 for s in STATES}
    for n, p in SLOT_PMFS[slot].items():
        state = "L" if n < previous_coordinate else "R" if n == previous_coordinate else "H"
        probs[state] += p
    z = sum(probs.values())
    return {s: probs[s] / z for s in STATES}


def learned_hlr_successors(rows: Sequence[dict], tau: float) -> Tuple[Tuple[str, ...], List[dict]]:
    if len(rows) < 2:
        raise ValueError("at least two XTRA rows are required")
    states = [hlr_state(main_numbers(a), main_numbers(b)) for a, b in zip(rows[:-1], rows[1:])]
    current_state = states[-1]
    current_coords = main_numbers(rows[-1])
    slot_models: List[dict] = []
    for j in range(PICKS):
        counts = {s: 0 for s in STATES}
        for t in range(len(states) - 1):
            if states[t][j] == current_state[j]:
                counts[states[t + 1][j]] += 1
        n_obs = sum(counts.values())
        p0 = structural_hlr_probs(j, current_coords[j])
        posterior = {
            s: (counts[s] + tau * p0[s]) / (n_obs + tau)
            for s in STATES
        }
        slot_models.append(
            {
                "slot": j + 1,
                "current_coordinate": current_coords[j],
                "conditioning_state": current_state[j],
                "successor_counts": counts,
                "matching_transition_count": n_obs,
                "structural_hlr": p0,
                "posterior_hlr": posterior,
            }
        )
    return current_state, slot_models


def full_mixture(rows: Sequence[dict], tau: float) -> dict:
    current_state, slot_models = learned_hlr_successors(rows, tau)
    current_coords = main_numbers(rows[-1])

    slot_acc = [{n: 0.0 for n in range(1, FIELD_N + 1)} for _ in range(PICKS)]
    pattern_mass: Dict[str, float] = {}
    total_weight = 0.0
    legal_count = 0

    # Under the exact null each legal combination has identical mass, so the common
    # factor 1/C(50,5) cancels during normalization. We retain only the HLR residual
    # likelihood ratio. Every state has positive shrinkage mass, so every legal
    # combination remains alive.
    for combo in itertools.combinations(range(1, FIELD_N + 1), PICKS):
        ratios = []
        pattern = []
        for j, n in enumerate(combo):
            state = "L" if n < current_coords[j] else "R" if n == current_coords[j] else "H"
            pattern.append(state)
            p0 = slot_models[j]["structural_hlr"][state]
            q = slot_models[j]["posterior_hlr"][state]
            if p0 <= 0.0:
                ratios.append(1.0)
            else:
                ratios.append(max(q, EPS) / p0)
        # Geometric pooling avoids treating five sparse slot-transition estimates as
        # five independent likelihood multipliers.
        weight = math.exp(sum(math.log(max(r, EPS)) for r in ratios) / PICKS)
        total_weight += weight
        legal_count += 1
        key = "".join(pattern)
        pattern_mass[key] = pattern_mass.get(key, 0.0) + weight
        for j, n in enumerate(combo):
            slot_acc[j][n] += weight

    if total_weight <= 0:
        raise RuntimeError("mixture produced zero total weight")
    slot_marginals: Dict[str, Dict[str, float]] = {}
    for j in range(PICKS):
        z = sum(slot_acc[j].values())
        slot_marginals[str(j + 1)] = {
            str(n): slot_acc[j][n] / z
            for n in range(1, FIELD_N + 1)
            if slot_acc[j][n] > 0.0
        }

    global_inclusion = {
        str(n): sum(float(slot_marginals[str(j + 1)].get(str(n), 0.0)) for j in range(PICKS))
        for n in range(1, FIELD_N + 1)
    }
    normalized_pattern_mass = {
        key: mass / total_weight for key, mass in pattern_mass.items()
    }
    top_patterns = sorted(
        normalized_pattern_mass.items(), key=lambda kv: (-kv[1], kv[0])
    )[:20]

    return {
        "expert_id": "XTRA_HLR_FULL_MIXTURE_BASE",
        "architecture_status": "shadow",
        "evidence": "INSUFFICIENT_EVIDENCE",
        "training_rows": len(rows),
        "cutoff": rows[-1]["draw_date"],
        "latest_state_source": rows[-1].get("_state_source", "unknown"),
        "tau": tau,
        "current_main": list(current_coords),
        "current_hlr": list(current_state),
        "slot_hlr_models": slot_models,
        "legal_combination_count": legal_count,
        "all_legal_combinations_positive": True,
        "pooling": "geometric_mean_of_slot_HLR_residual_likelihood_ratios",
        "slot_marginals": slot_marginals,
        "global_inclusion": global_inclusion,
        "top_joint_hlr_patterns": [
            {"pattern": key, "probability": prob} for key, prob in top_patterns
        ],
        "guardrail": (
            "No HLR pattern is a hard gate. Feed these full-support slot marginals "
            "to downstream residual experts such as Richardson."
        ),
    }


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--ledger", default="data/powerball_xtra_history.jsonl")
    p.add_argument("--working-extension", default=None)
    p.add_argument("--cutoff", default=None, help="YYYY-MM-DD; applied after merging")
    p.add_argument("--tau", type=float, default=6.0)
    p.add_argument("--out", default=None)
    return p.parse_args()


def main() -> None:
    args = parse_args()
    if args.tau <= 0:
        raise ValueError("tau must be > 0")
    canonical = load_jsonl(args.ledger)
    extension = load_jsonl(args.working_extension) if args.working_extension else []
    rows = merge_rows(canonical, extension)
    if args.cutoff:
        rows = [r for r in rows if r["draw_date"] <= args.cutoff]
    if len(rows) < 2:
        raise ValueError("not enough rows at cutoff")
    result = full_mixture(rows, args.tau)
    result["data_boundary"] = "XTRA_only_from_2026-06-02"
    result["working_extension_used"] = bool(args.working_extension)
    text = json.dumps(result, indent=2, sort_keys=True)
    if args.out:
        path = Path(args.out)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)


if __name__ == "__main__":
    main()
