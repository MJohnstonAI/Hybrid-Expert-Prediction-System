"""E0011 experimental, post-hoc replay only. Standard library; no ledger writes."""
from __future__ import annotations

import hashlib
import itertools as it
import json
import math
import random
import statistics
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "scripts"))
from validate_draws import validate_rows
from structural_null import hlr_null, vvd_null, gap_null, joint_hlr_null
from candidate_coalition_engine import (
    BASE_MAIN_EXPERTS, aggregate_candidate_evidence, centered_rank_skill,
)
from aggressive_expert_lab import expert_score_maps

N, M, SEED, BUDGET = 50, 5, 20260905, 20
TOTAL = math.comb(N, M)
KS = (7, 10, 13, 16, 17, 20)


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()


def elementary(weights, degree):
    e = [1.0] + [0.0] * degree
    for w in weights:
        for j in range(degree, 0, -1):
            e[j] += w * e[j - 1]
    return e


class SubsetModel:
    """Exactly normalized product-weight law on fixed-cardinality subsets."""
    def __init__(self, weights, size=5):
        if len(weights) < size or size < 1 or any(w <= 0 or not math.isfinite(w) for w in weights):
            raise ValueError("positive finite weights and feasible subset size required")
        self.weights, self.size = tuple(weights), size
        self.z = elementary(weights, size)[size]
        self.marginals = [
            w * elementary(weights[:i] + weights[i + 1:], size - 1)[size - 1] / self.z
            for i, w in enumerate(weights)
        ]
        self.suffix = [elementary(weights[i:], size) for i in range(len(weights) + 1)]

    def probability(self, line):
        if len(line) != self.size or len(set(line)) != self.size or any(n < 1 or n > len(self.weights) for n in line):
            raise ValueError("illegal line")
        return math.prod(self.weights[n - 1] for n in line) / self.z

    def sample(self, rng):
        left, chosen = self.size, []
        for i, w in enumerate(self.weights):
            if not left:
                break
            p = w * self.suffix[i + 1][left - 1] / self.suffix[i][left]
            if len(self.weights) - i == left or rng.random() < p:
                chosen.append(i + 1)
                left -= 1
        assert left == 0
        return tuple(chosen)

    def slots(self):
        return [[
            elementary(self.weights[:i], j)[j] * self.weights[i]
            * elementary(self.weights[i + 1:], self.size - j - 1)[self.size - j - 1] / self.z
            for i in range(len(self.weights))
        ] for j in range(self.size)]


class Mixture:
    def __init__(self, models, weights):
        self.models, self.weights = models, weights
        self.marginals = [sum(a * m.marginals[i] for a, m in zip(weights, models)) for i in range(N)]

    def probability(self, line):
        return sum(a * m.probability(line) for a, m in zip(self.weights, self.models))

    def sample(self, rng):
        model = rng.choices(self.models, weights=self.weights, k=1)[0]
        return model.sample(rng)


def forecast(history, log_weights):
    """Consumes previous draws only; target outcomes are not an argument."""
    cumulative = Counter(n for row in history for n in row["main_numbers"])
    recent = Counter(n for row in history[-5:] for n in row["main_numbers"])
    models = [SubsetModel([1.0] * N)] + [
        SubsetModel([1 + counts[n] / 10 for n in range(1, N + 1)])
        for counts in (cumulative, recent)
    ]
    scale = max(log_weights)
    raw = [math.exp(x - scale) for x in log_weights]
    posterior = [x / sum(raw) for x in raw]
    effective = [0.5 + 0.5 * posterior[0], 0.5 * posterior[1], 0.5 * posterior[2]]
    return models, Mixture(models, effective), posterior


def neighborhood(line, pool_size=N):
    """All winning five-sets with >=4 matches; exactly 226 for pool_size=50."""
    line = tuple(sorted(line))
    outcomes = {line}
    for omitted in line:
        kept = [n for n in line if n != omitted]
        for added in range(1, pool_size + 1):
            if added not in line:
                outcomes.add(tuple(sorted(kept + [added])))
    return outcomes


def coverage(slate):
    return set().union(*(neighborhood(line) for line in slate))


def greedy(candidates, neighborhoods, masses, budget=BUDGET):
    remaining, covered, chosen = list(range(len(candidates))), set(), []
    for _ in range(budget):
        gains = {i: math.fsum(masses[s] for s in sorted(neighborhoods[i] - covered)) for i in remaining}
        best = max(remaining, key=lambda i: (gains[i], -i))
        chosen.append(candidates[best])
        covered.update(neighborhoods[best])
        remaining.remove(best)
    return chosen


def random_lines(pool, count, rng):
    result = set()
    while len(result) < count:
        result.add(tuple(sorted(rng.sample(list(pool), M))))
    return sorted(result)


def portfolios(model, ranking, seed):
    rng, candidates = random.Random(seed), set()
    while len(candidates) < 128:
        candidates.add(model.sample(rng))
    candidates = sorted(candidates)
    neighborhoods = [neighborhood(line) for line in candidates]
    universe = set().union(*neighborhoods)
    masses = {line: model.probability(line) for line in universe}
    return {
        "joint_greedy": greedy(candidates, neighborhoods, masses),
        "null_greedy_same_candidates": greedy(candidates, neighborhoods, dict.fromkeys(universe, 1.0)),
        "random_K13": random_lines(ranking[:13], BUDGET, random.Random(seed + 1)),
        "random_full": random_lines(range(1, N + 1), BUDGET, random.Random(seed + 2)),
    }


def load_game(game):
    path = ROOT / "data" / ("draw_history.jsonl" if game == "MAIN" else "powerball_xtra_history.jsonl")
    rows = [json.loads(s) for s in path.read_text(encoding="utf-8").splitlines() if s.strip()]
    raw_errors = validate_rows(list(enumerate(rows, 1)))
    if game == "MAIN" and raw_errors:
        raise ValueError(raw_errors)
    # Explicit compatibility view; preserve raw rows and their IDs/provenance in all artifacts.
    view = json.loads(json.dumps(rows))
    if game == "XTRA":
        for i, row in enumerate(view):
            if row.get("game_variant") != "powerball_xtra" or row["draw_id"] != rows[0]["draw_id"] + i:
                raise ValueError("XTRA namespace or source ID sequence invalid")
            row["draw_id"] = i + 1
            for key, flag in (("source_url", "source_url_missing"), ("draw_method", "draw_method_unknown"), ("machine_name", "machine_name_unknown")):
                if row.get(key) in (None, "", "unknown") and flag not in row["data_quality_flags"]:
                    row["data_quality_flags"].append(flag)
    errors = validate_rows(list(enumerate(view, 1)))
    if errors or any(not "2026-06-02" <= r["draw_date"] <= "2026-08-21" for r in rows):
        raise ValueError(errors or "snapshot cutoff changed; register new protocol")
    manifest_path = ROOT / "data" / ("draw_manifest.json" if game == "MAIN" else "powerball_xtra_manifest.json")
    manifest = json.loads(manifest_path.read_text())
    count_key, date_key = ("row_count", "latest_draw_date") if game == "MAIN" else ("canonical_row_count", "latest_canonical_draw_date")
    if manifest[count_key] != len(rows) or manifest[date_key] != rows[-1]["draw_date"]:
        raise ValueError("manifest mismatch")
    audit = {
        "source_path": str(path.relative_to(ROOT)), "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "row_count": len(rows), "latest_date": rows[-1]["draw_date"], "raw_validator_errors": raw_errors,
        "compatibility_view_errors": errors, "original_ledger_modified": False,
        "external_verification_performed": False,
        "draw_methods": dict(Counter(r["draw_method"] for r in rows)),
        "machines": dict(Counter(r["machine_name"] for r in rows)),
        "source_url_missing_count": sum(not r.get("source_url") for r in rows),
        "raw_flags": {str(r["draw_id"]): r["data_quality_flags"] for r in rows},
    }
    return rows, audit


def rank(values, tie_order):
    return sorted(range(1, N + 1), key=lambda n: (-values[n - 1], tie_order[n]))


def basket_mass(model, basket, minimum=4):
    """Exact P(at least minimum of the five winners are in basket)."""
    if isinstance(model, Mixture):
        return sum(a * basket_mass(m, basket, minimum) for a, m in zip(model.weights, model.models))
    inside = elementary([w for i, w in enumerate(model.weights, 1) if i in basket], model.size)
    outside = elementary([w for i, w in enumerate(model.weights, 1) if i not in basket], model.size)
    return sum(inside[j] * outside[model.size - j] for j in range(minimum, model.size + 1)) / model.z


def acquire(model, initial, passes=5):
    basket = set(initial)
    mass, swaps = basket_mass(model, basket), []
    for _ in range(passes):
        best, move = mass, None
        for remove in sorted(basket):
            for add in sorted(set(range(1, N + 1)) - basket):
                proposed = basket - {remove} | {add}
                candidate_mass = basket_mass(model, proposed)
                if candidate_mass > best + 1e-14:
                    best, move = candidate_mass, (remove, add)
        if move is None:
            break
        basket = basket - {move[0]} | {move[1]}
        swaps.append(list(move))
        mass = best
    return {"basket": sorted(basket), "four_plus_mass": mass, "five_mass": basket_mass(model, basket, 5), "swaps": swaps}


def mean_se(values):
    return {"mean": statistics.mean(values), "descriptive_se": statistics.stdev(values) / math.sqrt(len(values)) if len(values) > 1 else None}


def replay(game):
    rows, audit = load_game(game)
    logs, records, skill = [math.log(x) for x in (0.8, 0.1, 0.1)], [], {}
    game_seed = SEED + (100000 if game == "XTRA" else 0)
    for index in range(5, len(rows)):
        history = rows[:index]
        models, mixed, posterior = forecast(history, logs)
        order = random.Random(game_seed + index).sample(range(1, 51), 50)
        tie = {n: i for i, n in enumerate(order)}
        maps = {k: v for k, v in expert_score_maps(history).items() if k in BASE_MAIN_EXPERTS}
        incumbent = aggregate_candidate_evidence(maps, skill, range(1, N + 1))["ranking"]
        rankings = {name: rank(m.marginals, tie) for name, m in zip(("uniform", "frequency", "recency", "mixture"), models + [mixed])}
        rankings["incumbent_candidate_adapter"] = incumbent
        acquisition = acquire(mixed, rankings["mixture"][:13])
        slate = portfolios(mixed, rankings["mixture"], game_seed + index * 100)
        frozen = {"history_sha256": digest(history), "training_rows": index, "probability_weights": mixed.weights,
                  "component_coordinate_weights": [list(m.weights) for m in models],
                  "marginals": mixed.marginals, "rankings": rankings, "joint_K13": acquisition, "portfolios": slate}
        freeze_hash = digest(frozen)  # Logical replay boundary only, not a historical timestamp.
        target = rows[index]
        assert history[-1]["draw_date"] < target["draw_date"]
        winner = set(target["main_numbers"])
        losses = {}
        for name, model in zip(("uniform", "frequency", "recency", "mixture"), models + [mixed]):
            losses[name] = {"log_loss": -math.log(model.probability(target["main_numbers"])),
                            "brier": sum((p - int(n in winner)) ** 2 for n, p in enumerate(model.marginals, 1)) / N}
        portfolio_scores = {}
        for name, lines in slate.items():
            hits = [len(set(line) & winner) for line in lines]
            portfolio_scores[name] = {"lines": len(lines), "best_hits": max(hits),
                                     "three_plus_lines": sum(h >= 3 for h in hits), "four_plus_lines": sum(h >= 4 for h in hits),
                                     "five_lines": hits.count(5), "null_four_plus_mass": len(coverage(lines)) / TOTAL}
        records.append({"date": target["draw_date"], "source_draw_id": target["draw_id"], "actual": target["main_numbers"],
                        "freeze_sha256": freeze_hash, "frozen": frozen, "losses": losses,
                        "candidate_hits": {name: {str(k): len(winner & set(r[:k])) for k in KS} for name, r in rankings.items()},
                        "joint_K13_hits": len(winner & set(acquisition["basket"])), "portfolio_scores": portfolio_scores})
        logs = [a + math.log(m.probability(target["main_numbers"])) for a, m in zip(logs, models)]
        for name, scores in maps.items():
            skill.setdefault(name, []).append(centered_rank_skill(scores, winner, range(1, N + 1)))
    summary = {"targets": len(records), "submitted_lines_per_strategy": len(records) * BUDGET, "probability": {}, "candidate": {}, "portfolio": {}}
    for name in records[0]["losses"]:
        summary["probability"][name] = {
            "mean_log_loss": statistics.mean(r["losses"][name]["log_loss"] for r in records),
            "mean_brier": statistics.mean(r["losses"][name]["brier"] for r in records),
            "paired_log_loss_minus_null": mean_se([r["losses"][name]["log_loss"] - r["losses"]["uniform"]["log_loss"] for r in records]),
            "log_likelihood_ratio_vs_null": sum(r["losses"]["uniform"]["log_loss"] - r["losses"][name]["log_loss"] for r in records),
        }
    for name in records[0]["candidate_hits"]:
        summary["candidate"][name] = {}
        for k in KS:
            h = [r["candidate_hits"][name][str(k)] for r in records]
            summary["candidate"][name][str(k)] = {"coordinate_hits": sum(h), "coordinate_denominator": 5 * len(h),
                "draws_3plus": sum(x >= 3 for x in h), "draws_4plus": sum(x >= 4 for x in h), "draws_5": h.count(5),
                "catastrophes_at_most_1": sum(x <= 1 for x in h)}
    for name in records[0]["portfolio_scores"]:
        scores = [r["portfolio_scores"][name] for r in records]
        summary["portfolio"][name] = {"draws_3plus": sum(s["best_hits"] >= 3 for s in scores),
            "draws_4plus": sum(s["best_hits"] >= 4 for s in scores), "draws_5": sum(s["best_hits"] == 5 for s in scores),
            "best_hits": max(s["best_hits"] for s in scores), "mean_null_four_plus_mass": statistics.mean(s["null_four_plus_mass"] for s in scores),
            "expected_null_four_plus_draws": sum(s["null_four_plus_mass"] for s in scores),
            "paired_four_plus_minus_same_candidates_null": mean_se([int(r["portfolio_scores"][name]["best_hits"] >= 4) - int(r["portfolio_scores"]["null_greedy_same_candidates"]["best_hits"] >= 4) for r in records])}
    h = [r["joint_K13_hits"] for r in records]
    summary["joint_K13"] = {"coordinate_hits": sum(h), "coordinate_denominator": len(h) * 5,
        "draws_3plus": sum(x >= 3 for x in h), "draws_4plus": sum(x >= 4 for x in h), "draws_5": h.count(5),
        "catastrophes_at_most_1": sum(x <= 1 for x in h),
        "targets_different_from_marginal_K13": sum(bool(r["frozen"]["joint_K13"]["swaps"]) for r in records),
        "paired_four_plus_minus_incumbent": mean_se([int(r["joint_K13_hits"] >= 4) - int(r["candidate_hits"]["incumbent_candidate_adapter"]["13"] >= 4) for r in records])}
    models, mixed, posterior = forecast(rows, logs)
    order = random.Random(game_seed + 999).sample(range(1, 51), 50)
    ranking = rank(mixed.marginals, {n: i for i, n in enumerate(order)})
    demo = {"status": "stale_snapshot_demonstration_NOT_live_prediction", "history_cutoff": rows[-1]["draw_date"],
            "future_target_date": None, "paper_trading_only": True, "posterior_component_weights": posterior,
            "effective_component_weights": mixed.weights, "marginal_inclusions": mixed.marginals,
            "component_coordinate_weights": [list(m.weights) for m in models], "top13_diagnostic": ranking[:13],
            "joint_K13": acquire(mixed, ranking[:13]),
            "powerball_probabilities": [1 / 16] * 16,
            "slates": portfolios(mixed, ranking, game_seed + 99900)}
    demo["exact_four_plus_null_coverage"] = {k: len(coverage(v)) / TOTAL for k, v in demo["slates"].items()}
    latest = rows[-1]["main_numbers"]
    structural = {"previous_source_draw_id": rows[-1]["draw_id"], "previous_numbers": latest,
                  "hlr": hlr_null(latest), "vvd": vvd_null(latest), "gap": gap_null(latest),
                  "joint_hlr": joint_hlr_null(latest)}
    return {"audit": audit, "summary": summary, "records": records, "demonstration": demo, "structural_null": structural}


def main():
    result = {"experiment": "E0011", "evidence": "INSUFFICIENT_EVIDENCE", "mode": "post_hoc_replay",
              "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "protocol_sha256": hashlib.sha256((HERE / "protocol.yaml").read_bytes()).hexdigest(), "games": {}}
    for game in ("MAIN", "XTRA"):
        result["games"][game] = replay(game)
        print(json.dumps({"game": game, "summary": result["games"][game]["summary"]}), flush=True)
    result["exact_geometry"] = {"legal_five_sets": TOTAL, "single_line_four_plus_winning_sets": 226,
        "twenty_line_four_plus_upper_bound": 20 * 226 / TOTAL, "twenty_distinct_lines_exact_five_probability": 20 / TOTAL,
        "zero_of_19_one_sided_95_percent_upper": 1 - 0.05 ** (1 / 19),
        "K_nulls": {str(k): {"expected_hits": k / 10, "four_plus": (math.comb(k, 4) * (50-k) + math.comb(k, 5)) / TOTAL,
                              "five": math.comb(k, 5) / TOTAL} for k in KS}}
    (HERE / "results.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    for game, data in result["games"].items():
        (HERE / f"{game.lower()}_demonstration_not_live.json").write_text(json.dumps(data["demonstration"], indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
