"""E0032 fixed-K13 compression utilities.

This module consumes an already-frozen positive 5x50 slot-product residual field.
It does not fit a forecast model and does not read target outcomes.

Exact:
- partition normalization
- slot and anywhere marginals
- fixed-basket hit-count distribution
- K13_MEAN theorem

Heuristic unless separately certified:
- K13_4PLUS
- K13_5
- K13_ROBUST
"""
from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Iterable, Sequence

N = 50
M = 5
K = 13


def _validate_weights(weights: Sequence[Sequence[float]]) -> tuple[tuple[float, ...], ...]:
    if len(weights) != M or any(len(row) != N for row in weights):
        raise ValueError("weights must be a 5x50 matrix")
    out = []
    for row in weights:
        vals = tuple(float(x) for x in row)
        if any((not math.isfinite(x)) or x <= 0.0 for x in vals):
            raise ValueError("weights must be positive finite values")
        out.append(vals)
    return tuple(out)


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
    def three_plus(self) -> float:
        return sum(self.hit_probabilities[3:])

    @property
    def four_plus(self) -> float:
        return self.hit_probabilities[4] + self.hit_probabilities[5]

    @property
    def containment(self) -> float:
        return self.hit_probabilities[5]


class SlotProductField:
    """P(x1<...<x5) proportional to product_j weights[j][xj]."""

    def __init__(self, weights: Sequence[Sequence[float]]):
        self.weights = _validate_weights(weights)
        self.z = self.partition()
        if not math.isfinite(self.z) or self.z <= 0.0:
            raise ValueError("invalid partition function")

    def partition(self, allowed: Iterable[int] | None = None) -> float:
        allowed_set = None if allowed is None else set(int(v) for v in allowed)
        if allowed_set is not None and any(v < 1 or v > N for v in allowed_set):
            raise ValueError("allowed coordinates out of range")
        dp = [1.0] + [0.0] * M
        for value in range(1, N + 1):
            if allowed_set is not None and value not in allowed_set:
                continue
            for j in range(M, 0, -1):
                dp[j] += self.weights[j - 1][value - 1] * dp[j - 1]
        return dp[M]

    def slot_marginals(self) -> tuple[tuple[float, ...], ...]:
        left = [[0.0] * (N + 1) for _ in range(M + 1)]
        right = [[0.0] * (N + 2) for _ in range(M + 2)]
        left[0] = [1.0] * (N + 1)
        right[M + 1] = [1.0] * (N + 2)

        for j in range(1, M + 1):
            for value in range(1, N + 1):
                left[j][value] = (
                    left[j][value - 1]
                    + self.weights[j - 1][value - 1] * left[j - 1][value - 1]
                )

        for j in range(M, 0, -1):
            for value in range(N, 0, -1):
                right[j][value] = (
                    right[j][value + 1]
                    + self.weights[j - 1][value - 1] * right[j + 1][value + 1]
                )

        out = []
        for j in range(1, M + 1):
            row = []
            for value in range(1, N + 1):
                p = (
                    left[j - 1][value - 1]
                    * self.weights[j - 1][value - 1]
                    * right[j + 1][value + 1]
                    / self.z
                )
                row.append(p)
            out.append(tuple(row))
        return tuple(out)

    def anywhere_marginals(self) -> tuple[float, ...]:
        slots = self.slot_marginals()
        marg = tuple(sum(slots[j][i] for j in range(M)) for i in range(N))
        if not math.isclose(sum(marg), M, rel_tol=0.0, abs_tol=1e-10):
            raise AssertionError("anywhere marginals must sum to five")
        return marg

    def hit_distribution(self, basket: Iterable[int]) -> tuple[float, ...]:
        basket = tuple(sorted(set(int(v) for v in basket)))
        if len(basket) != K or any(v < 1 or v > N for v in basket):
            raise ValueError("basket must contain exactly 13 unique coordinates")
        selected = set(basket)
        dp = [[0.0] * (M + 1) for _ in range(M + 1)]
        dp[0][0] = 1.0
        for value in range(1, N + 1):
            b = 1 if value in selected else 0
            for j in range(M, 0, -1):
                w = self.weights[j - 1][value - 1]
                for h in range(b, j + 1):
                    dp[j][h] += w * dp[j - 1][h - b]
        probs = tuple(x / self.z for x in dp[M])
        if not math.isclose(sum(probs), 1.0, rel_tol=0.0, abs_tol=1e-10):
            raise AssertionError("hit distribution must normalize")
        return probs

    def metrics(self, basket: Iterable[int]) -> BasketMetrics:
        basket = tuple(sorted(set(int(v) for v in basket)))
        return BasketMetrics(basket=basket, hit_probabilities=self.hit_distribution(basket))

    def mean_basket(self) -> tuple[int, ...]:
        marg = self.anywhere_marginals()
        chosen = sorted(range(1, N + 1), key=lambda v: (-marg[v - 1], v))[:K]
        return tuple(sorted(chosen))


def _key(metrics: BasketMetrics, objective: str) -> tuple[float, ...]:
    if objective == "four_plus":
        return (metrics.four_plus, metrics.containment, -metrics.catastrophe, metrics.expected_hits)
    if objective == "five":
        return (metrics.containment, metrics.four_plus, -metrics.catastrophe, metrics.expected_hits)
    if objective == "robust":
        return (-metrics.catastrophe, metrics.four_plus, metrics.containment, metrics.expected_hits)
    raise ValueError("objective must be four_plus, five, or robust")


def _improve_by_swaps(field: SlotProductField, start: Iterable[int], objective: str) -> BasketMetrics:
    current = field.metrics(start)
    while True:
        selected = set(current.basket)
        excluded = [v for v in range(1, N + 1) if v not in selected]
        best = current
        best_key = _key(current, objective)
        for remove in current.basket:
            for add in excluded:
                candidate = tuple(sorted((selected - {remove}) | {add}))
                metrics = field.metrics(candidate)
                key = _key(metrics, objective)
                if key > best_key or (key == best_key and candidate < best.basket):
                    best, best_key = metrics, key
        if best.basket == current.basket:
            return current
        current = best


def deterministic_starts(field: SlotProductField) -> list[tuple[int, ...]]:
    """Small deterministic multistart family; no target-conditioned randomness."""
    marg = field.anywhere_marginals()
    ranked = sorted(range(1, N + 1), key=lambda v: (-marg[v - 1], v))
    base = tuple(sorted(ranked[:K]))
    starts = {base}
    # One-seat perturbations of the mean-optimal basket using the next 12 marginals.
    selected = set(base)
    for remove in base:
        for add in ranked[K : K + 12]:
            starts.add(tuple(sorted((selected - {remove}) | {add})))
    return sorted(starts)


def solve_arms(weights: Sequence[Sequence[float]]) -> dict:
    field = SlotProductField(weights)
    mean = field.metrics(field.mean_basket())
    starts = deterministic_starts(field)
    out = {
        "K13_MEAN": {"solver_status": "globally_optimal_by_marginal_theorem", "metrics": mean},
    }
    for name, objective in (
        ("K13_4PLUS", "four_plus"),
        ("K13_5", "five"),
        ("K13_ROBUST", "robust"),
    ):
        best = None
        for start in starts:
            result = _improve_by_swaps(field, start, objective)
            if best is None or _key(result, objective) > _key(best, objective) or (
                _key(result, objective) == _key(best, objective) and result.basket < best.basket
            ):
                best = result
        out[name] = {
            "solver_status": "best_found_deterministic_multistart_swap_not_global_certificate",
            "starts": len(starts),
            "metrics": best,
        }
    return out


def uniform_controls() -> dict[str, float]:
    den = math.comb(N, M)
    p = [
        math.comb(K, h) * math.comb(N - K, M - h) / den
        for h in range(M + 1)
    ]
    return {
        "expected_hits": sum(h * p[h] for h in range(M + 1)),
        "four_plus": p[4] + p[5],
        "five": p[5],
        "catastrophe": p[0] + p[1],
    }
