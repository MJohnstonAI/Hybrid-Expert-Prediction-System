from __future__ import annotations

import argparse
import csv
import hashlib
import json
import random
import statistics
from pathlib import Path
from typing import Any, Dict, List, Sequence, Tuple

from core import *

def random_feature(rng: random.Random, kind: str | None = None) -> Dict[str, Any]:
    kind = kind or rng.choice(FEATURE_KINDS)
    if kind == "recency":
        params = {"scale": round(rng.uniform(1.0, 24.0), 4)}
    elif kind == "frequency":
        params = {"window": rng.randint(8, 800)}
    elif kind == "gap_target":
        params = {"target": round(rng.uniform(1.0, 25.0), 4), "scale": round(rng.uniform(0.75, 10.0), 4)}
    elif kind == "shadow":
        params = {"scale": round(rng.uniform(0.5, 4.0), 4)}
    elif kind == "residue":
        params = {"modulus": rng.randint(2, 12)}
    elif kind == "transition":
        params = {
            "lookback": rng.randint(10, 180),
            "predecessor_distance": rng.randint(0, 3),
            "smoothing": round(rng.uniform(1.0, 30.0), 4),
        }
    else:
        raise ValueError(kind)
    return {"kind": kind, "weight": round(rng.uniform(-1.5, 1.5), 4), "params": params}


def seed_genomes(seed_file: Path | None = None) -> List[Dict[str, Any]]:
    base = [
        {"features": [{"kind": "recency", "weight": 1.0, "params": {"scale": 6.0}}]},
        {"features": [{"kind": "frequency", "weight": 1.0, "params": {"window": 10000}}]},
        {"features": [{"kind": "gap_target", "weight": 1.0, "params": {"target": 7.0, "scale": 3.0}}]},
        {"features": [{"kind": "shadow", "weight": 1.0, "params": {"scale": 1.5}}]},
        {"features": [{"kind": "residue", "weight": 1.0, "params": {"modulus": 8}}]},
        {"features": [{"kind": "transition", "weight": 1.0, "params": {"lookback": 80, "predecessor_distance": 0, "smoothing": 10.0}}]},
        {"features": [
            {"kind": "recency", "weight": 0.5, "params": {"scale": 6.0}},
            {"kind": "gap_target", "weight": 0.25, "params": {"target": 7.0, "scale": 3.0}},
            {"kind": "residue", "weight": 0.25, "params": {"modulus": 8}},
        ]},
        {"features": [
            {"kind": "recency", "weight": 0.5, "params": {"scale": 6.0}},
            {"kind": "frequency", "weight": 0.5, "params": {"window": 10000}},
        ]},
    ]
    if seed_file is None:
        return base
    payload = json.loads(seed_file.read_text(encoding="utf-8"))
    external = []
    for item in payload:
        external.append(item.get("genome", item))
    return [canonical_genome(g) for g in external]


def random_genome(rng: random.Random, min_features: int = 1, max_features: int = 4) -> Dict[str, Any]:
    count = rng.randint(min_features, min(max_features, len(FEATURE_KINDS)))
    kinds = rng.sample(FEATURE_KINDS, count)
    return {"features": [random_feature(rng, k) for k in kinds]}


def mutate(genome: Dict[str, Any], rng: random.Random, max_features: int = 5) -> Dict[str, Any]:
    child = json.loads(json.dumps(canonical_genome(genome)))
    features = child["features"]
    action = rng.choices(
        ["weight", "param", "add", "remove", "replace"],
        weights=[30, 30, 18, 10, 12],
        k=1,
    )[0]
    if action == "weight":
        f = rng.choice(features)
        f["weight"] = round(max(-2.5, min(2.5, float(f["weight"]) + rng.gauss(0, 0.25))), 4)
    elif action == "param":
        idx = rng.randrange(len(features))
        f = features[idx]
        fresh = random_feature(rng, f["kind"])
        key = rng.choice(list(fresh["params"].keys()))
        f["params"][key] = fresh["params"][key]
    elif action == "add" and len(features) < max_features:
        existing = {f["kind"] for f in features}
        available = [k for k in FEATURE_KINDS if k not in existing]
        if available:
            features.append(random_feature(rng, rng.choice(available)))
    elif action == "remove" and len(features) > 1:
        features.pop(rng.randrange(len(features)))
    elif action == "replace":
        existing = {f["kind"] for f in features}
        idx = rng.randrange(len(features))
        available = [k for k in FEATURE_KINDS if k not in existing or k == features[idx]["kind"]]
        features[idx] = random_feature(rng, rng.choice(available))
    return canonical_genome(child)


def crossover(a: Dict[str, Any], b: Dict[str, Any], rng: random.Random, max_features: int = 5) -> Dict[str, Any]:
    pool: Dict[str, Dict[str, Any]] = {}
    for f in canonical_genome(a)["features"] + canonical_genome(b)["features"]:
        if f["kind"] not in pool or rng.random() < 0.5:
            pool[f["kind"]] = json.loads(json.dumps(f))
    kinds = list(pool)
    rng.shuffle(kinds)
    kinds = kinds[:max_features]
    if not kinds:
        return random_genome(rng)
    return canonical_genome({"features": [pool[k] for k in kinds]})


def feature_kind_set(genome: Dict[str, Any]) -> set[str]:
    return {f["kind"] for f in genome["features"]}


def novelty(genome: Dict[str, Any], reference: Sequence[Dict[str, Any]]) -> float:
    a = feature_kind_set(genome)
    if not reference:
        return 1.0
    distances = []
    for g in reference:
        b = feature_kind_set(g)
        union = len(a | b)
        distances.append(1.0 - len(a & b) / union if union else 0.0)
    return min(distances)


def load_cache(path: Path) -> Dict[str, Any]:
    if path.exists():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}


def save_cache(path: Path, cache: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(cache, indent=2, sort_keys=True), encoding="utf-8")


def evaluate_cached(
    draws: Sequence[Draw],
    genome: Dict[str, Any],
    target_indices: Sequence[int],
    split_name: str,
    cache: Dict[str, Any],
    data_fp: str,
    feature_cache: Dict[Tuple[int, str], Dict[int, float]] | None = None,
) -> Dict[str, float]:
    target_digest = hashlib.sha256(
        ",".join(map(str, target_indices)).encode("utf-8")
    ).hexdigest()[:10]
    key = f"{data_fp}:{split_name}:{target_digest}:{genome_hash(genome)}"
    if key not in cache:
        cache[key] = evaluate_genome(draws, genome, target_indices, feature_cache)
    return cache[key]


def evenly_spaced_subset(indices: Sequence[int], size: int) -> List[int]:
    if size >= len(indices):
        return list(indices)
    if size <= 1:
        return [indices[len(indices) // 2]]
    picked = []
    for j in range(size):
        pos = round(j * (len(indices) - 1) / (size - 1))
        picked.append(indices[pos])
    return sorted(set(picked))


def screening_schedule(discovery: Sequence[int], generation: int, generations: int) -> Tuple[str, List[int]]:
    ratio = generation / max(1, generations)
    if ratio < 0.50:
        return "tier1_small", evenly_spaced_subset(discovery, min(80, len(discovery)))
    if ratio < 0.80:
        return "tier2_medium", evenly_spaced_subset(discovery, min(200, len(discovery)))
    return "tier3_full", list(discovery)


def baseline_genomes() -> Dict[str, Dict[str, Any]]:
    return {
        "recency": seed_genomes()[0],
        "cumulative_frequency": seed_genomes()[1],
        "recency_frequency": seed_genomes()[-1],
    }


def null_distribution(draws: Sequence[Draw], target_indices: Sequence[int], trials: int, seed: int) -> Dict[str, Any]:
    rng = random.Random(seed)
    mean_ranks = []
    top10s = []
    top15s = []
    top20s = []
    threeplus = []
    for _ in range(trials):
        ranks: List[int] = []
        hits = {10: 0, 15: 0, 20: 0}
        d3 = 0
        for i in target_indices:
            ranking = list(NUMBERS)
            rng.shuffle(ranking)
            pos = {n: r for r, n in enumerate(ranking, 1)}
            wr = [pos[n] for n in draws[i].mains]
            ranks.extend(wr)
            for k in hits:
                hits[k] += sum(r <= k for r in wr)
            d3 += int(sum(r <= 20 for r in wr) >= 3)
        winners = len(ranks)
        mean_ranks.append(statistics.fmean(ranks))
        top10s.append(hits[10] / winners)
        top15s.append(hits[15] / winners)
        top20s.append(hits[20] / winners)
        threeplus.append(d3 / len(target_indices))
    return {
        "trials": trials,
        "mean_rank_mean": statistics.fmean(mean_ranks),
        "top10_recall_mean": statistics.fmean(top10s),
        "top15_recall_mean": statistics.fmean(top15s),
        "top20_recall_mean": statistics.fmean(top20s),
        "top20_3plus_rate_mean": statistics.fmean(threeplus),
        "samples": {
            "mean_rank": mean_ranks,
            "top10_recall": top10s,
            "top15_recall": top15s,
            "top20_recall": top20s,
            "top20_3plus_rate": threeplus,
        },
    }


def empirical_tail(champion: Dict[str, float], null: Dict[str, Any]) -> Dict[str, float]:
    s = null["samples"]
    trials = len(s["mean_rank"])
    return {
        "mean_rank_lower_tail_p": (1 + sum(x <= champion["mean_rank"] for x in s["mean_rank"])) / (trials + 1),
        "top10_upper_tail_p": (1 + sum(x >= champion["top10_recall"] for x in s["top10_recall"])) / (trials + 1),
        "top15_upper_tail_p": (1 + sum(x >= champion["top15_recall"] for x in s["top15_recall"])) / (trials + 1),
        "top20_upper_tail_p": (1 + sum(x >= champion["top20_recall"] for x in s["top20_recall"])) / (trials + 1),
        "top20_3plus_upper_tail_p": (1 + sum(x >= champion["top20_3plus_rate"] for x in s["top20_3plus_rate"])) / (trials + 1),
    }


def evolve(args: argparse.Namespace) -> Dict[str, Any]:
    rng = random.Random(args.seed)
    draws = load_draws(Path(args.data))
    if len(draws) <= args.warmup + 5:
        raise ValueError("Dataset too small for requested warmup")
    available = len(draws) - args.warmup
    discovery_count = min(args.discovery_targets, max(1, available - 1))
    disc = list(range(args.warmup, args.warmup + discovery_count))
    val = list(range(args.warmup + discovery_count, len(draws)))
    if not val:
        split = max(1, int(available * 0.7))
        disc = list(range(args.warmup, args.warmup + split))
        val = list(range(args.warmup + split, len(draws)))

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    cache_path = Path(args.cache) if args.cache else out_dir / "eval_cache.json"
    cache = load_cache(cache_path)
    fp = dataset_fingerprint(draws)

    population: List[Dict[str, Any]] = []
    seen = set()
    for g in seed_genomes(Path(args.seed_file) if args.seed_file else None):
        h = genome_hash(g)
        if h not in seen:
            population.append(g); seen.add(h)
    while len(population) < args.population:
        g = random_genome(rng, max_features=args.max_features)
        h = genome_hash(g)
        if h not in seen:
            population.append(g); seen.add(h)

    variants_seen: set[str] = set()
    lineage_rows = []
    generation_summaries = []
    feature_cache: Dict[Tuple[int, str], Dict[int, float]] = {}
    final_scored: List[Dict[str, Any]] = []

    for gen in range(args.generations + 1):
        tier_name, screen_targets = screening_schedule(disc, gen, args.generations)
        scored = []
        for g in population:
            h = genome_hash(g)
            variants_seen.add(h)
            m = evaluate_cached(draws, g, screen_targets, tier_name, cache, fp, feature_cache)
            fit = selection_fitness(m, len(g["features"]))
            rec = {"hash": h, "genome": g, "metrics": m, "fitness": fit}
            scored.append(rec)
        scored.sort(key=lambda r: (-r["fitness"], r["metrics"]["mean_rank"], r["hash"]))
        final_scored = scored
        best = scored[0]
        generation_summaries.append({
            "generation": gen,
            "screen_tier": tier_name,
            "screen_targets": len(screen_targets),
            "best_hash": best["hash"],
            "best_fitness": best["fitness"],
            "best_mean_rank": best["metrics"]["mean_rank"],
            "best_top15": best["metrics"]["top15_recall"],
            "best_top20": best["metrics"]["top20_recall"],
            "unique_population": len({r["hash"] for r in scored}),
        })
        print(f"gen={gen:03d} tier={tier_name} n={len(screen_targets)} best={best['hash']} fit={best['fitness']:.5f} rank={best['metrics']['mean_rank']:.3f} top15={best['metrics']['top15_recall']:.3f} top20={best['metrics']['top20_recall']:.3f}")
        if gen == args.generations:
            break

        elite_n = max(2, int(args.population * args.elite_fraction))
        novelty_n = max(1, int(args.population * args.novelty_fraction))
        elites = scored[:elite_n]
        refs = [r["genome"] for r in elites]
        rest = scored[elite_n:]
        rest.sort(key=lambda r: (-novelty(r["genome"], refs), -r["fitness"]))
        novel = rest[:novelty_n]
        parents = elites + novel

        next_pop = [r["genome"] for r in elites]
        next_seen = {genome_hash(g) for g in next_pop}
        attempts = 0
        while len(next_pop) < args.population and attempts < args.population * 100:
            attempts += 1
            if rng.random() < args.crossover_rate and len(parents) >= 2:
                pa, pb = rng.sample(parents, 2)
                child = crossover(pa["genome"], pb["genome"], rng, args.max_features)
                parent_ids = [pa["hash"], pb["hash"]]
                if rng.random() < 0.65:
                    child = mutate(child, rng, args.max_features)
            else:
                pa = rng.choice(parents)
                child = mutate(pa["genome"], rng, args.max_features)
                parent_ids = [pa["hash"]]
            h = genome_hash(child)
            if h in next_seen:
                continue
            next_seen.add(h)
            next_pop.append(child)
            lineage_rows.append({"generation": gen + 1, "child": h, "parents": "|".join(parent_ids)})
        while len(next_pop) < args.population:
            child = random_genome(rng, max_features=args.max_features)
            h = genome_hash(child)
            if h not in next_seen:
                next_seen.add(h); next_pop.append(child)
                lineage_rows.append({"generation": gen + 1, "child": h, "parents": "RANDOM_INJECTION"})
        population = next_pop
        if gen % 5 == 0:
            save_cache(cache_path, cache)

    save_cache(cache_path, cache)
    finalists = final_scored[: min(args.finalists, len(final_scored))]
    champion = finalists[0]
    for r in finalists:
        r["validation_metrics"] = evaluate_cached(draws, r["genome"], val, "validation", cache, fp, feature_cache)
        r["validation_fitness_reference_only"] = selection_fitness(r["validation_metrics"], len(r["genome"]["features"]))
    save_cache(cache_path, cache)

    baselines = {}
    for name, g in baseline_genomes().items():
        baselines[name] = {
            "genome": g,
            "discovery": evaluate_cached(draws, g, disc, f"baseline_{name}_discovery", cache, fp, feature_cache),
            "validation": evaluate_cached(draws, g, val, f"baseline_{name}_validation", cache, fp, feature_cache),
        }

    null = null_distribution(draws, val, args.null_trials, args.seed + 991) if args.null_trials > 0 else None
    null_summary = None
    if null:
        null_summary = {k: v for k, v in null.items() if k != "samples"}
        null_summary["champion_empirical_tails"] = empirical_tail(champion["validation_metrics"], null)

    result = {
        "experiment_id": "E0002",
        "engine": "HEPS-Evolve v0.1",
        "status": "exploratory_survivor_search_only",
        "evidence_classification": "INSUFFICIENT_EVIDENCE",
        "dataset": {
            "path": args.data,
            "fingerprint": fp,
            "draws": len(draws),
            "first_date": draws[0].date,
            "last_date": draws[-1].date,
            "warmup": args.warmup,
            "discovery_targets": len(disc),
            "validation_targets": len(val),
            "validation_first_date": draws[val[0]].date if val else None,
        },
        "search": {
            "seed": args.seed,
            "population": args.population,
            "generations": args.generations,
            "max_features": args.max_features,
            "finalists": len(finalists),
            "variants_evaluated": len(variants_seen),
            "seed_file": args.seed_file,
            "fitness_formula": "1.20*rank_gain + 1.00*(top10-.20) + .85*(top15-.30) + .60*(top20-.40) + .45*(top20_3plus-null) - .006*(features-1)",
        },
        "champion": champion,
        "finalists": finalists,
        "baselines": baselines,
        "null_validation": null_summary,
        "generation_summaries": generation_summaries,
        "interpretation_rule": "Small-data evolution may reject/qualify candidates but cannot establish a HEPS breakthrough; prospective frozen evidence is mandatory.",
    }

    (out_dir / "results.json").write_text(json.dumps(result, indent=2, sort_keys=True), encoding="utf-8")
    with (out_dir / "lineage.csv").open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=["generation", "child", "parents"])
        writer.writeheader(); writer.writerows(lineage_rows)
    with (out_dir / "generation_summary.csv").open("w", encoding="utf-8", newline="") as fh:
        fields = ["generation", "screen_tier", "screen_targets", "best_hash", "best_fitness", "best_mean_rank", "best_top15", "best_top20", "unique_population"]
        writer = csv.DictWriter(fh, fieldnames=fields)
        writer.writeheader(); writer.writerows(generation_summaries)
    return result
