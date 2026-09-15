"""E0035 uncertainty-aware fixed-K13 compression replay.

Discovery replay only.  The implementation intentionally holds the E0030
upstream model family fixed and changes only the compression decision.

Standard library only; no ledger writes.
"""
from __future__ import annotations

import argparse
import json
import math
import random
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence

ROOT = Path(__file__).resolve().parents[2]
LEDGER = ROOT / "data" / "draw_history.jsonl"
N = 50
M = 5
K = 13
DEFAULT_BOOTSTRAP_REPS = 16
BASE_SEED = 20260915


def elementary(weights: Sequence[float], degree: int = M) -> list[float]:
    e = [1.0] + [0.0] * degree
    for weight in weights:
        for j in range(degree, 0, -1):
            e[j] += weight * e[j - 1]
    return e


class SubsetModel:
    """Exactly normalized product-weight law on unordered fixed-size subsets."""

    def __init__(self, weights: Sequence[float]):
        if len(weights) != N or any((not math.isfinite(x)) or x <= 0 for x in weights):
            raise ValueError("expected 50 positive finite coordinate weights")
        self.weights = tuple(float(x) for x in weights)
        self.z = elementary(self.weights, M)[M]
        self.marginals = tuple(
            weight
            * elementary(self.weights[:i] + self.weights[i + 1 :], M - 1)[M - 1]
            / self.z
            for i, weight in enumerate(self.weights)
        )
        if not math.isclose(sum(self.marginals), M, rel_tol=0.0, abs_tol=1e-10):
            raise AssertionError("coordinate marginals must sum to five")

    def probability(self, line: Sequence[int]) -> float:
        if len(line) != M or len(set(line)) != M or any(n < 1 or n > N for n in line):
            raise ValueError("illegal 5/50 line")
        return math.prod(self.weights[n - 1] for n in line) / self.z

    def hit_distribution(self, basket: Iterable[int]) -> tuple[float, ...]:
        selected = set(int(x) for x in basket)
        if len(selected) != K or any(n < 1 or n > N for n in selected):
            raise ValueError("basket must contain exactly 13 legal coordinates")
        inside = elementary([w for n, w in enumerate(self.weights, 1) if n in selected], M)
        outside = elementary([w for n, w in enumerate(self.weights, 1) if n not in selected], M)
        probs = tuple(inside[h] * outside[M - h] / self.z for h in range(M + 1))
        if not math.isclose(sum(probs), 1.0, rel_tol=0.0, abs_tol=1e-10):
            raise AssertionError("hit distribution must normalize")
        return probs


class Mixture:
    def __init__(self, models: Sequence[SubsetModel], weights: Sequence[float]):
        if len(models) != len(weights) or not models:
            raise ValueError("models and weights must have equal nonzero length")
        if any(x < 0 or not math.isfinite(x) for x in weights):
            raise ValueError("mixture weights must be finite and nonnegative")
        total = math.fsum(weights)
        if total <= 0:
            raise ValueError("mixture weight sum must be positive")
        self.models = tuple(models)
        self.weights = tuple(x / total for x in weights)
        self.marginals = tuple(
            math.fsum(a * model.marginals[i] for a, model in zip(self.weights, self.models))
            for i in range(N)
        )
        self._metric_cache: dict[tuple[int, ...], BasketMetrics] = {}

    def probability(self, line: Sequence[int]) -> float:
        return math.fsum(a * model.probability(line) for a, model in zip(self.weights, self.models))

    def metrics(self, basket: Iterable[int]) -> "BasketMetrics":
        key = tuple(sorted(set(int(x) for x in basket)))
        if len(key) != K:
            raise ValueError("basket must contain 13 unique coordinates")
        cached = self._metric_cache.get(key)
        if cached is not None:
            return cached
        component = [model.hit_distribution(key) for model in self.models]
        probs = tuple(
            math.fsum(a * distribution[h] for a, distribution in zip(self.weights, component))
            for h in range(M + 1)
        )
        result = BasketMetrics(key, probs)
        self._metric_cache[key] = result
        return result


@dataclass(frozen=True)
class BasketMetrics:
    basket: tuple[int, ...]
    hit_probabilities: tuple[float, ...]

    @property
    def expected_hits(self) -> float:
        return sum(h * p for h, p in enumerate(self.hit_probabilities))

    @property
    def catastrophe(self) -> float:
        return self.hit_probabilities[0] + self.hit_probabilities[1]

    @property
    def four_plus(self) -> float:
        return self.hit_probabilities[4] + self.hit_probabilities[5]

    @property
    def containment(self) -> float:
        return self.hit_probabilities[5]

    def as_dict(self) -> dict:
        return {
            "basket": list(self.basket),
            "hit_probabilities": list(self.hit_probabilities),
            "expected_hits": self.expected_hits,
            "catastrophe": self.catastrophe,
            "four_plus": self.four_plus,
            "containment": self.containment,
        }


def load_rows() -> list[dict]:
    rows = [json.loads(line) for line in LEDGER.read_text(encoding="utf-8").splitlines() if line.strip()]
    if not rows or rows[0]["draw_date"] != "2026-06-02":
        raise ValueError("canonical active Main boundary changed")
    previous = None
    for expected_id, row in enumerate(rows, 1):
        if row["draw_id"] != expected_id:
            raise ValueError("draw_id sequence invalid")
        if previous is not None and row["draw_date"] <= previous:
            raise ValueError("draw dates must be strictly chronological")
        if len(row["main_numbers"]) != M or row["main_numbers"] != sorted(set(row["main_numbers"])):
            raise ValueError("invalid Main numbers")
        previous = row["draw_date"]
    return rows


def e0030_point_field(history: Sequence[dict], log_weights: Sequence[float]) -> tuple[list[SubsetModel], Mixture, list[float], list[float]]:
    cumulative = Counter(n for row in history for n in row["main_numbers"])
    recent = Counter(n for row in history[-5:] for n in row["main_numbers"])
    models = [
        SubsetModel([1.0] * N),
        SubsetModel([1.0 + cumulative[n] / 10.0 for n in range(1, N + 1)]),
        SubsetModel([1.0 + recent[n] / 10.0 for n in range(1, N + 1)]),
    ]
    scale = max(log_weights)
    raw = [math.exp(x - scale) for x in log_weights]
    posterior = [x / math.fsum(raw) for x in raw]
    effective = [0.5 + 0.5 * posterior[0], 0.5 * posterior[1], 0.5 * posterior[2]]
    return models, Mixture(models, effective), posterior, effective


def _normalized_exp_weights(rng: random.Random, count: int) -> list[float]:
    values = [rng.expovariate(1.0) for _ in range(count)]
    scale = count / math.fsum(values)
    return [x * scale for x in values]


def bayesian_bootstrap_field(
    history: Sequence[dict], effective_weights: Sequence[float], *, reps: int, seed: int
) -> Mixture:
    if reps < 1:
        raise ValueError("bootstrap reps must be positive")
    rng = random.Random(seed)
    models: list[SubsetModel] = [SubsetModel([1.0] * N)]
    weights: list[float] = [effective_weights[0]]

    for _ in range(reps):
        draw_weights = _normalized_exp_weights(rng, len(history))
        cumulative = [0.0] * (N + 1)
        for draw_weight, row in zip(draw_weights, history):
            for number in row["main_numbers"]:
                cumulative[number] += draw_weight
        models.append(SubsetModel([1.0 + cumulative[n] / 10.0 for n in range(1, N + 1)]))
        weights.append(effective_weights[1] / reps)

        recent_history = history[-5:]
        recent_weights = _normalized_exp_weights(rng, len(recent_history))
        recent = [0.0] * (N + 1)
        for draw_weight, row in zip(recent_weights, recent_history):
            for number in row["main_numbers"]:
                recent[number] += draw_weight
        models.append(SubsetModel([1.0 + recent[n] / 10.0 for n in range(1, N + 1)]))
        weights.append(effective_weights[2] / reps)

    return Mixture(models, weights)


def mean_basket(field: Mixture) -> tuple[int, ...]:
    ranked = sorted(range(1, N + 1), key=lambda n: (-field.marginals[n - 1], n))
    return tuple(sorted(ranked[:K]))


def robust_key(metrics: BasketMetrics) -> tuple[float, ...]:
    return (-metrics.catastrophe, metrics.four_plus, metrics.containment, metrics.expected_hits)


def deterministic_starts(field: Mixture, extra: Iterable[Iterable[int]] = ()) -> list[tuple[int, ...]]:
    ranked = sorted(range(1, N + 1), key=lambda n: (-field.marginals[n - 1], n))
    base_ranked = ranked[:K]
    base = tuple(sorted(base_ranked))
    starts = {base}
    for offset in range(3):
        remove = base_ranked[K - 1 - offset]
        add = ranked[K + offset]
        starts.add(tuple(sorted((set(base) - {remove}) | {add})))
    for basket in extra:
        candidate = tuple(sorted(set(int(x) for x in basket)))
        if len(candidate) == K:
            starts.add(candidate)
    return sorted(starts)


def improve_one_swap(field: Mixture, start: Iterable[int]) -> BasketMetrics:
    current = field.metrics(start)
    while True:
        selected = set(current.basket)
        excluded = [n for n in range(1, N + 1) if n not in selected]
        best = current
        best_key = robust_key(current)
        for remove in current.basket:
            base = selected - {remove}
            for add in excluded:
                candidate = tuple(sorted(base | {add}))
                metrics = field.metrics(candidate)
                key = robust_key(metrics)
                if key > best_key or (key == best_key and candidate < best.basket):
                    best, best_key = metrics, key
        if best.basket == current.basket:
            return current
        current = best


def solve_robust(field: Mixture, *, extra_starts: Iterable[Iterable[int]] = ()) -> BasketMetrics:
    best = None
    for start in deterministic_starts(field, extra_starts):
        result = improve_one_swap(field, start)
        if best is None or robust_key(result) > robust_key(best) or (
            robust_key(result) == robust_key(best) and result.basket < best.basket
        ):
            best = result
    assert best is not None
    return best


def random_k13_controls() -> dict[str, float]:
    denominator = math.comb(N, M)
    p = [math.comb(K, h) * math.comb(N - K, M - h) / denominator for h in range(M + 1)]
    return {
        "expected_hits": sum(h * p[h] for h in range(M + 1)),
        "catastrophe": p[0] + p[1],
        "three_plus": p[3] + p[4] + p[5],
        "four_plus": p[4] + p[5],
        "five": p[5],
    }


def _summarize(records: Sequence[dict], arm: str) -> dict:
    hits = [row["hits"][arm] for row in records]
    return {
        "targets": len(hits),
        "coordinate_hits": sum(hits),
        "mean_hits": sum(hits) / len(hits),
        "catastrophes_H_le_1": sum(x <= 1 for x in hits),
        "draws_H_ge_3": sum(x >= 3 for x in hits),
        "draws_H_ge_4": sum(x >= 4 for x in hits),
        "draws_H_5": sum(x == 5 for x in hits),
        "last10_coordinate_hits": sum(hits[-10:]),
        "last3_hits": hits[-3:],
    }


def run_replay(*, bootstrap_reps: int = DEFAULT_BOOTSTRAP_REPS) -> dict:
    rows = load_rows()
    log_weights = [math.log(0.8), math.log(0.1), math.log(0.1)]
    records = []
    logloss_deltas = []

    for target_index in range(5, len(rows)):
        history = rows[:target_index]
        components, point_field, posterior, effective = e0030_point_field(history, log_weights)
        bb_field = bayesian_bootstrap_field(
            history,
            effective,
            reps=bootstrap_reps,
            seed=BASE_SEED + 1009 * target_index,
        )

        point_mean = mean_basket(point_field)
        bb_mean = mean_basket(bb_field)
        point_robust = solve_robust(point_field, extra_starts=[bb_mean])
        bb_robust = solve_robust(bb_field, extra_starts=[point_mean, point_robust.basket])

        target = rows[target_index]
        winners = set(target["main_numbers"])
        baskets = {
            "POINT_MEAN": point_mean,
            "POINT_ROBUST": point_robust.basket,
            "BB_MEAN": bb_mean,
            "BB_ROBUST": bb_robust.basket,
        }
        records.append(
            {
                "target_date": target["draw_date"],
                "actual": target["main_numbers"],
                "hits": {name: len(winners & set(basket)) for name, basket in baskets.items()},
                "baskets": {name: list(basket) for name, basket in baskets.items()},
                "bb_vs_point_symmetric_difference": len(set(bb_robust.basket) ^ set(point_mean)),
            }
        )

        uniform_loss = math.log(math.comb(N, M))
        model_loss = -math.log(point_field.probability(target["main_numbers"]))
        logloss_deltas.append(model_loss - uniform_loss)

        log_weights = [
            old + math.log(component.probability(target["main_numbers"]))
            for old, component in zip(log_weights, components)
        ]

    arms = ["POINT_MEAN", "POINT_ROBUST", "BB_MEAN", "BB_ROBUST"]
    summary = {arm: _summarize(records, arm) for arm in arms}
    point_hits = [row["hits"]["POINT_MEAN"] for row in records]
    bb_hits = [row["hits"]["BB_ROBUST"] for row in records]
    paired = [b - p for b, p in zip(bb_hits, point_hits)]

    components, point_field, posterior, effective = e0030_point_field(rows, log_weights)
    bb_field = bayesian_bootstrap_field(
        rows,
        effective,
        reps=bootstrap_reps,
        seed=BASE_SEED + 1009 * len(rows),
    )
    point_mean = mean_basket(point_field)
    bb_mean = mean_basket(bb_field)
    point_robust = solve_robust(point_field, extra_starts=[bb_mean])
    bb_robust = solve_robust(bb_field, extra_starts=[point_mean, point_robust.basket])

    return {
        "experiment": "E0035",
        "evidence_classification": "INSUFFICIENT_EVIDENCE",
        "replay_status": "post_hoc_discovery",
        "canonical_cutoff": rows[-1]["draw_date"],
        "canonical_rows": len(rows),
        "bootstrap_replicates": bootstrap_reps,
        "random_K13_control": random_k13_controls(),
        "point_field_mean_logloss_delta_model_minus_uniform": math.fsum(logloss_deltas) / len(logloss_deltas),
        "summary": summary,
        "paired_BB_ROBUST_minus_POINT_MEAN": {
            "sum_hit_delta": sum(paired),
            "mean_hit_delta": sum(paired) / len(paired),
            "targets_better": sum(x > 0 for x in paired),
            "targets_equal": sum(x == 0 for x in paired),
            "targets_worse": sum(x < 0 for x in paired),
        },
        "mean_bb_robust_symmetric_difference_vs_point_mean": math.fsum(
            row["bb_vs_point_symmetric_difference"] for row in records
        )
        / len(records),
        "last_three_records": records[-3:],
        "prospective_2026_09_15": {
            "training_cutoff": rows[-1]["draw_date"],
            "component_posterior": posterior,
            "effective_mixture_weights": effective,
            "POINT_MEAN": point_field.metrics(point_mean).as_dict(),
            "POINT_ROBUST": point_robust.as_dict(),
            "BB_MEAN": bb_field.metrics(bb_mean).as_dict(),
            "BB_ROBUST": bb_robust.as_dict(),
            "solver_note": "nonlinear robust arms are deterministic multistart one-swap best-found; no global certificate",
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bootstrap-reps", type=int, default=DEFAULT_BOOTSTRAP_REPS)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run_replay(bootstrap_reps=args.bootstrap_reps)
    text = json.dumps(result, indent=2, sort_keys=True)
    print(text)
    if args.output:
        args.output.write_text(text + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
