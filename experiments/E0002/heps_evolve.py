#!/usr/bin/env python3
"""HEPS-Evolve v0.1 CLI and public experiment API."""
from __future__ import annotations

import argparse

from core import *
from evolution import *


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--data", required=True, help="CSV (draw_date,n1..n5) or canonical JSONL")
    p.add_argument("--seed-file", default=None, help="Optional JSON seed genome list")
    p.add_argument("--out-dir", default="outputs/research/heps_evolve_e0002")
    p.add_argument("--cache", default=None)
    p.add_argument("--warmup", type=int, default=30)
    p.add_argument("--discovery-targets", type=int, default=470)
    p.add_argument("--population", type=int, default=100)
    p.add_argument("--generations", type=int, default=20)
    p.add_argument("--max-features", type=int, default=5)
    p.add_argument("--finalists", type=int, default=10)
    p.add_argument("--elite-fraction", type=float, default=0.12)
    p.add_argument("--novelty-fraction", type=float, default=0.08)
    p.add_argument("--crossover-rate", type=float, default=0.30)
    p.add_argument("--null-trials", type=int, default=1000)
    p.add_argument("--seed", type=int, default=20260807)
    return p.parse_args()


if __name__ == "__main__":
    evolve(parse_args())
