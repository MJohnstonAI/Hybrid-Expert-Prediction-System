#!/usr/bin/env python3
"""Exposure and power-horizon calculator for HEPS XTRA acquisition experiments.

Under the exact exchangeable 5/50 null, any target-blind fixed K-set has the same
winner-overlap distribution. This script makes that baseline and approximate
minimum target horizon explicit before an experiment consumes prospective draws.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from statistics import NormalDist
from typing import Dict

FIELD_N = 50
WINNERS = 5


def hypergeom_overlap_pmf(k: int) -> Dict[int, float]:
    den = math.comb(FIELD_N, WINNERS)
    out: Dict[int, float] = {}
    lo = max(0, WINNERS - (FIELD_N - k))
    hi = min(WINNERS, k)
    for h in range(lo, hi + 1):
        out[h] = math.comb(k, h) * math.comb(FIELD_N - k, WINNERS - h) / den
    return out


def null_moments(k: int) -> tuple[float, float]:
    p = k / FIELD_N
    mean = WINNERS * p
    var = WINNERS * p * (1.0 - p) * ((FIELD_N - WINNERS) / (FIELD_N - 1))
    return mean, math.sqrt(var)


def approximate_horizon(
    k: int,
    delta: float,
    alpha: float,
    power: float,
    family_tests: int,
) -> int:
    if delta <= 0:
        raise ValueError("delta must be > 0")
    if not 0 < alpha < 1:
        raise ValueError("alpha must be in (0,1)")
    if not 0 < power < 1:
        raise ValueError("power must be in (0,1)")
    if family_tests < 1:
        raise ValueError("family_tests must be >=1")
    _, sd = null_moments(k)
    adjusted_alpha = alpha / family_tests
    z_alpha = NormalDist().inv_cdf(1.0 - adjusted_alpha)
    z_power = NormalDist().inv_cdf(power)
    return math.ceil(((z_alpha + z_power) * sd / delta) ** 2)


def parse_deltas(text: str) -> list[float]:
    vals = [float(x.strip()) for x in text.split(",") if x.strip()]
    if not vals:
        raise ValueError("at least one delta is required")
    return vals


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--k", type=int, default=13)
    p.add_argument("--alpha", type=float, default=0.05)
    p.add_argument("--power", type=float, default=0.80)
    p.add_argument("--family-tests", type=int, default=1)
    p.add_argument("--deltas", default="0.10,0.15,0.20,0.25,0.30")
    p.add_argument("--draws-per-week", type=float, default=2.0)
    p.add_argument("--out", default=None)
    args = p.parse_args()
    if not 1 <= args.k <= FIELD_N:
        raise ValueError("k must be between 1 and 50")

    mean, sd = null_moments(args.k)
    pmf = hypergeom_overlap_pmf(args.k)
    horizons = []
    for delta in parse_deltas(args.deltas):
        n = approximate_horizon(
            args.k, delta, args.alpha, args.power, args.family_tests
        )
        weeks = n / args.draws_per_week
        horizons.append(
            {
                "minimum_effect_hits_per_draw": delta,
                "alternative_mean_hits": mean + delta,
                "approx_targets": n,
                "approx_weeks": weeks,
                "approx_months": weeks / 4.345,
            }
        )

    result = {
        "game": "powerball_xtra_5_of_50",
        "k": args.k,
        "null_expected_hits": mean,
        "null_sd_hits": sd,
        "null_overlap_pmf": {str(h): p for h, p in pmf.items()},
        "one_sided_alpha": args.alpha,
        "power": args.power,
        "family_tests_bonferroni": args.family_tests,
        "method": "normal_approximation_on_mean_overlap; planning_only",
        "horizons": horizons,
        "interpretation": (
            "Fixed review counts are not proof thresholds. Use this as an order-of-"
            "magnitude prospective power gate; paired-model variance and temporal "
            "dependence must be reported when enough frozen targets exist."
        ),
    }
    text = json.dumps(result, indent=2, sort_keys=True)
    if args.out:
        path = Path(args.out)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)


if __name__ == "__main__":
    main()
