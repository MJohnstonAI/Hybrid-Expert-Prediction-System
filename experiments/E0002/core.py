#!/usr/bin/env python3
"""HEPS-Evolve v0.1: structured evolutionary search for main-number candidate ranking.

Research-only. This script evolves small, auditable weighted feature genomes and
scores them with strict walk-forward evaluation. LLMs are not required in the
inner loop.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
import statistics
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Sequence, Tuple

NUMBERS = tuple(range(1, 51))
RANDOM_MEAN_RANK = 25.5
FEATURE_KINDS = (
    "recency",
    "frequency",
    "gap_target",
    "shadow",
    "residue",
    "transition",
)


def hypergeom_tail_ge3(k: int = 20, population: int = 50, winners: int = 5) -> float:
    denom = math.comb(population, winners)
    return sum(
        math.comb(k, j) * math.comb(population - k, winners - j) / denom
        for j in range(3, winners + 1)
        if j <= k and winners - j <= population - k
    )

RANDOM_TOP20_3PLUS = hypergeom_tail_ge3(20)


@dataclass(frozen=True)
class Draw:
    date: str
    mains: Tuple[int, int, int, int, int]


def load_draws(path: Path) -> List[Draw]:
    if path.suffix.lower() == ".jsonl":
        draws: List[Draw] = []
        with path.open("r", encoding="utf-8") as fh:
            for line in fh:
                if not line.strip():
                    continue
                row = json.loads(line)
                draws.append(Draw(str(row["draw_date"]), tuple(int(x) for x in row["main_numbers"])))
    else:
        with path.open("r", encoding="utf-8", newline="") as fh:
            reader = csv.DictReader(fh)
            draws = []
            for row in reader:
                mains = tuple(int(row[f"n{i}"]) for i in range(1, 6))
                draws.append(Draw(str(row["draw_date"]), mains))
    draws.sort(key=lambda d: d.date)
    for d in draws:
        if len(set(d.mains)) != 5 or any(n < 1 or n > 50 for n in d.mains):
            raise ValueError(f"Invalid draw {d}")
    return draws


def dataset_fingerprint(draws: Sequence[Draw]) -> str:
    raw = "\n".join(f"{d.date}:{','.join(map(str, d.mains))}" for d in draws)
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]


def zscore(values: Dict[int, float]) -> Dict[int, float]:
    vals = list(values.values())
    mean = statistics.fmean(vals)
    sd = statistics.pstdev(vals)
    if sd <= 1e-12:
        return {n: 0.0 for n in values}
    return {n: (v - mean) / sd for n, v in values.items()}


def age_since_hit(history: Sequence[Draw], n: int) -> int:
    for age, draw in enumerate(reversed(history)):
        if n in draw.mains:
            return age
    return len(history) + 1


def feature_vector(history: Sequence[Draw], spec: Dict[str, Any]) -> Dict[int, float]:
    kind = spec["kind"]
    p = spec.get("params", {})
    if not history:
        return {n: 0.0 for n in NUMBERS}

    if kind == "recency":
        scale = max(0.25, float(p.get("scale", 6.0)))
        return {n: math.exp(-age_since_hit(history, n) / scale) for n in NUMBERS}

    if kind == "frequency":
        window = max(2, min(len(history), int(p.get("window", 50))))
        counts = {n: 0 for n in NUMBERS}
        for d in history[-window:]:
            for n in d.mains:
                counts[n] += 1
        return {n: counts[n] / window for n in NUMBERS}

    if kind == "gap_target":
        target = max(0.0, float(p.get("target", 7.0)))
        scale = max(0.25, float(p.get("scale", 3.0)))
        return {n: math.exp(-abs(age_since_hit(history, n) - target) / scale) for n in NUMBERS}

    if kind == "shadow":
        scale = max(0.25, float(p.get("scale", 1.5)))
        prev = history[-1].mains
        return {n: math.exp(-min(abs(n - x) for x in prev) / scale) for n in NUMBERS}

    if kind == "residue":
        modulus = max(2, min(16, int(p.get("modulus", 8))))
        prev = history[-1].mains
        counts = {r: 0 for r in range(modulus)}
        for x in prev:
            counts[x % modulus] += 1
        return {n: counts[n % modulus] / 5.0 for n in NUMBERS}

    if kind == "transition":
        lookback = max(5, min(len(history) - 1 if len(history) > 1 else 5, int(p.get("lookback", 80))))
        distance = max(0, min(5, int(p.get("predecessor_distance", 0))))
        smoothing = max(0.1, float(p.get("smoothing", 5.0)))
        current = history[-1].mains
        counts = {n: smoothing * 0.1 for n in NUMBERS}
        exposures = smoothing
        start = max(0, len(history) - 1 - lookback)
        for i in range(start, len(history) - 1):
            prev = history[i].mains
            if any(abs(a - b) <= distance for a in current for b in prev):
                exposures += 1.0
                for n in history[i + 1].mains:
                    counts[n] += 1.0
        return {n: counts[n] / exposures for n in NUMBERS}

    raise ValueError(f"Unknown feature kind: {kind}")


def canonical_genome(genome: Dict[str, Any]) -> Dict[str, Any]:
    features = []
    for f in genome["features"]:
        params = {}
        for k, v in sorted(f.get("params", {}).items()):
            params[k] = round(v, 6) if isinstance(v, float) else v
        features.append({"kind": f["kind"], "weight": round(float(f["weight"]), 6), "params": params})
    features.sort(key=lambda x: x["kind"])
    return {"features": features}


def genome_hash(genome: Dict[str, Any]) -> str:
    raw = json.dumps(canonical_genome(genome), sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]


def feature_signature(spec: Dict[str, Any]) -> str:
    raw = json.dumps(
        {"kind": spec["kind"], "params": spec.get("params", {})},
        sort_keys=True, separators=(",", ":")
    )
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16]


def score_candidates(
    history: Sequence[Draw],
    genome: Dict[str, Any],
    feature_cache: Dict[Tuple[int, str], Dict[int, float]] | None = None,
    target_index: int | None = None,
) -> Dict[int, float]:
    total = {n: 0.0 for n in NUMBERS}
    for spec in genome["features"]:
        cache_key = (target_index if target_index is not None else len(history), feature_signature(spec))
        if feature_cache is not None and cache_key in feature_cache:
            vec = feature_cache[cache_key]
        else:
            vec = zscore(feature_vector(history, spec))
            if feature_cache is not None:
                feature_cache[cache_key] = vec
        weight = float(spec["weight"])
        for n in NUMBERS:
            total[n] += weight * vec[n]
    return total


def rank_candidates(
    history: Sequence[Draw],
    genome: Dict[str, Any],
    feature_cache: Dict[Tuple[int, str], Dict[int, float]] | None = None,
    target_index: int | None = None,
) -> List[int]:
    score = score_candidates(history, genome, feature_cache, target_index)
    return sorted(NUMBERS, key=lambda n: (-score[n], n))


def evaluate_genome(
    draws: Sequence[Draw],
    genome: Dict[str, Any],
    target_indices: Sequence[int],
    feature_cache: Dict[Tuple[int, str], Dict[int, float]] | None = None,
) -> Dict[str, float]:
    ranks: List[int] = []
    top_hits = {10: 0, 15: 0, 20: 0}
    draw_top20_3plus = 0
    for i in target_indices:
        history = draws[:i]
        target = draws[i]
        ranking = rank_candidates(history, genome, feature_cache, i)
        pos = {n: rank for rank, n in enumerate(ranking, start=1)}
        wranks = [pos[n] for n in target.mains]
        ranks.extend(wranks)
        for k in top_hits:
            top_hits[k] += sum(r <= k for r in wranks)
        if sum(r <= 20 for r in wranks) >= 3:
            draw_top20_3plus += 1
    winners = len(ranks)
    targets = len(target_indices)
    return {
        "targets": targets,
        "winners": winners,
        "mean_rank": statistics.fmean(ranks) if ranks else 99.0,
        "median_rank": statistics.median(ranks) if ranks else 99.0,
        "top10_recall": top_hits[10] / winners if winners else 0.0,
        "top15_recall": top_hits[15] / winners if winners else 0.0,
        "top20_recall": top_hits[20] / winners if winners else 0.0,
        "top20_3plus_rate": draw_top20_3plus / targets if targets else 0.0,
    }


def selection_fitness(metrics: Dict[str, float], feature_count: int) -> float:
    rank_gain = (RANDOM_MEAN_RANK - metrics["mean_rank"]) / RANDOM_MEAN_RANK
    return (
        1.20 * rank_gain
        + 1.00 * (metrics["top10_recall"] - 0.20)
        + 0.85 * (metrics["top15_recall"] - 0.30)
        + 0.60 * (metrics["top20_recall"] - 0.40)
        + 0.45 * (metrics["top20_3plus_rate"] - RANDOM_TOP20_3PLUS)
        - 0.006 * max(0, feature_count - 1)
    )
