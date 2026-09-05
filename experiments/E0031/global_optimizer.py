"""Globally bounded fixed-cardinality threshold acquisition, not a forecast model.

Requires NumPy; cutting-plane master additionally requires SciPy >= 1.11.
Uniform mass is handled analytically. Retained scenario masses are never
renormalized into a complete distribution: omitted mass remains in the bound.
"""
from __future__ import annotations

import heapq
import itertools
import math
import time
from fractions import Fraction

import numpy as np


def null_tail(n=50, m=5, k=13, threshold=4):
    def c(a, b):
        return math.comb(a, b) if 0 <= b <= a else 0
    return sum(c(k, h) * c(n-k, m-h) for h in range(threshold, m+1)) / c(n, m)


class Distribution:
    def __init__(self, lines, masses, n=50, k=13, threshold=4, uniform_mass=0.0, omitted_mass=0.0):
        raw = np.asarray(lines)
        if raw.size == 0:
            raw = np.empty((0, 5), dtype=int)
        if raw.ndim != 2 or raw.shape[1] != 5 or not np.issubdtype(raw.dtype, np.integer):
            raise ValueError("lines must be integer rows of five sorted unique coordinates")
        if not 5 <= n <= 255 or not 0 <= k <= n or not 1 <= threshold <= 5:
            raise ValueError("invalid dimensions")
        if np.any(raw < 1) or np.any(raw > n) or np.any(np.diff(raw, axis=1) <= 0):
            raise ValueError("illegal line")
        weights = np.asarray(masses, dtype=float)
        if weights.shape != (len(raw),) or not np.all(np.isfinite(weights)) or np.any(weights < 0):
            raise ValueError("invalid masses")
        if not all(math.isfinite(x) and x >= 0 for x in (uniform_mass, omitted_mass)):
            raise ValueError("invalid uniform or omitted mass")
        if not math.isclose(math.fsum(weights) + uniform_mass + omitted_mass, 1.0, abs_tol=1e-10):
            raise ValueError("masses must sum to one INCLUDING uniform and omitted mass")
        self.lines = (raw - 1).astype(np.uint8)
        self.masses = weights
        self.n, self.k, self.threshold = n, k, threshold
        self.uniform_mass, self.omitted_mass = uniform_mass, omitted_mass
        self.residual_mass = float(math.fsum(weights))
        self.constant = uniform_mass * null_tail(n, 5, k, threshold)

    def evaluate(self, basket):
        if len(basket) != self.k or len(set(basket)) != self.k or any(not 1 <= n <= self.n for n in basket):
            raise ValueError("basket must contain exactly k legal unique coordinates")
        x = np.zeros(self.n, dtype=np.uint8)
        x[np.asarray(basket, dtype=int)-1] = 1
        captured = x[self.lines].sum(axis=1)
        return self.constant + float(math.fsum(self.masses[captured >= self.threshold]))

    def marginal_basket(self):
        marginals = np.bincount(self.lines.ravel(), weights=np.repeat(self.masses, 5), minlength=self.n)
        return sorted(sorted(range(self.n), key=lambda i: (-marginals[i], i))[:self.k][i] + 1 for i in range(self.k))

    def cut(self, x, chunk_size=100000):
        """Upper affine cut, tight at x for the concave extension.

        For threshold r, the smallest 6-r selected indicators in a five-set
        sum to >=1 exactly when at least r of its coordinates are selected.
        """
        x = np.asarray(x, dtype=float)
        if x.shape != (self.n,) or np.any(x < 0) or np.any(x > 1):
            raise ValueError("x must be in the unit cube")
        d = 6-self.threshold
        intercept, coefficients = 0.0, np.zeros(self.n)
        if self.residual_mass == 0:
            return intercept, coefficients
        for start in range(0, len(self.lines), chunk_size):
            lines = self.lines[start:start+chunk_size]
            weights = self.masses[start:start+chunk_size] / self.residual_mass
            values = x[lines]
            order = np.argsort(values, axis=1, kind="stable")[:, :d]
            subset = np.take_along_axis(lines, order, axis=1)
            sums = x[subset].sum(axis=1)
            use_constant = sums >= 1.0
            intercept += float(math.fsum(weights[use_constant]))
            if np.any(~use_constant):
                indices = subset[~use_constant].ravel()
                selected_weights = np.repeat(weights[~use_constant], d)
                coefficients += np.bincount(indices, weights=selected_weights, minlength=self.n)
        return intercept, coefficients


def solve_global(distribution, seconds=60.0, max_iterations=1000, absolute_tolerance=1e-7):
    """MILP outer approximation; returns lower/upper bounds on FULL objective.

    Exact in exact arithmetic at zero gap. Reported floating-point certificates
    inherit HiGHS feasibility/duality tolerances, with a numerical guard.
    A timeout is never relabelled optimal. No installed packages are modified.
    """
    from scipy.optimize import milp, Bounds, LinearConstraint

    d = distribution
    best = d.marginal_basket()
    lower = d.evaluate(best)
    residual_upper = 1.0
    started = time.monotonic()
    trace = []
    if d.residual_mass == 0:
        return {"basket": best, "lower_bound": lower, "upper_bound": lower+d.omitted_mass,
                "absolute_gap": d.omitted_mass, "status": "uniform_exact" if not d.omitted_mass else "omitted_mass_bound", "iterations": 0, "trace": []}
    rows, limits = [], []
    x = np.zeros(d.n)
    x[np.asarray(best)-1] = 1
    intercept, coefficients = d.cut(x)
    rows.append(np.r_[-coefficients, 1.0]); limits.append(intercept)
    reason = "iteration_limit"
    numerical_guard = 1e-8
    for iteration in range(max_iterations):
        remaining = seconds - (time.monotonic()-started)
        if remaining <= 0:
            reason = "time_limit"
            break
        equality = np.r_[np.ones(d.n), 0.0]
        constraint = LinearConstraint(np.vstack([equality] + rows),
                                      np.r_[d.k, np.full(len(rows), -np.inf)], np.r_[d.k, limits])
        res = milp(c=np.r_[np.zeros(d.n), -1.0], integrality=np.r_[np.ones(d.n), 0],
                   bounds=Bounds(np.zeros(d.n+1), np.ones(d.n+1)), constraints=constraint,
                   options={"time_limit": remaining, "mip_rel_gap": 0.0, "presolve": True})
        dual = getattr(res, "mip_dual_bound", None)
        if dual is not None and math.isfinite(dual):
            residual_upper = min(residual_upper, max(0.0, -float(dual)) + numerical_guard)
        if res.x is None:
            reason = "master_without_incumbent"
            break
        selected = np.rint(res.x[:d.n]).astype(int)
        if np.max(np.abs(selected-res.x[:d.n])) > 1e-5 or selected.sum() != d.k or np.any((selected<0)|(selected>1)):
            reason = "master_without_integral_incumbent"
            break
        candidate = list(np.flatnonzero(selected)+1)
        value = d.evaluate(candidate)
        if value > lower:
            best, lower = candidate, value
        upper = max(lower, d.constant+d.residual_mass*residual_upper+d.omitted_mass)
        trace.append({"iteration": iteration+1, "master_status": int(res.status), "lower": lower, "upper": upper})
        if upper-lower <= absolute_tolerance:
            reason = "certified_to_tolerance"
            break
        intercept, coefficients = d.cut(selected.astype(float))
        rows.append(np.r_[-coefficients, 1.0]); limits.append(intercept)
    upper = max(lower, d.constant+d.residual_mass*residual_upper+d.omitted_mass)
    return {"basket": list(map(int, best)), "lower_bound": lower, "upper_bound": upper,
            "absolute_gap": upper-lower, "status": reason, "iterations": len(trace),
            "seconds": time.monotonic()-started, "omitted_mass": d.omitted_mass,
            "certificate_type": "floating_point_MILP_bound_with_numerical_guard", "trace": trace}


def solve_rational(lines, masses, n=50, k=13, threshold=4, node_limit=None):
    """Finite exact branch-and-bound for rational explicit scenario distributions.

    This is the correctness reference, not a promise of fast dense 50/13 solves.
    A stopped run retains its exact rational frontier upper bound.
    """
    weights = [Fraction(w) for w in masses]
    if len(lines) != len(weights) or any(w < 0 for w in weights) or sum(weights) != 1:
        raise ValueError("nonnegative rational masses summing to one required")
    masks = []
    for line in lines:
        if len(line) != 5 or len(set(line)) != 5 or any(not 1 <= i <= n for i in line):
            raise ValueError("illegal line")
        masks.append(sum(1 << (i-1) for i in line))
    if not 0 <= k <= n or not 1 <= threshold <= 5:
        raise ValueError("invalid dimensions")
    marg = [sum(w for s, w in zip(masks, weights) if s & (1 << i)) for i in range(n)]
    order = sorted(range(n), key=lambda i: (-marg[i], i))
    def value(mask):
        return sum(w for s, w in zip(masks, weights) if (s & mask).bit_count() >= threshold)
    def bound(selected, remaining, seats):
        return sum(w for s, w in zip(masks, weights)
                   if (s & selected).bit_count() + min(seats, (s & remaining).bit_count()) >= threshold)
    best = sum(1 << i for i in order[:k]); lower = value(best)
    all_mask = (1 << n)-1
    frontier, serial, visited = [], 0, 0
    heapq.heappush(frontier, (-bound(0, all_mask, k), serial, 0, all_mask, k))
    while frontier and (node_limit is None or visited < node_limit):
        negative, _, selected, remaining, seats = heapq.heappop(frontier)
        if -negative <= lower:
            continue
        visited += 1
        if seats == 0 or seats == remaining.bit_count():
            full = selected | (remaining if seats else 0)
            candidate_value = value(full)
            if candidate_value > lower:
                best, lower = full, candidate_value
            continue
        branch = next(i for i in order if remaining & (1 << i))
        rest = remaining & ~(1 << branch)
        for chosen, slots in ((selected | (1 << branch), seats-1), (selected, seats)):
            if slots < 0 or slots > rest.bit_count():
                continue
            upper = bound(chosen, rest, slots)
            if upper > lower:
                serial += 1
                heapq.heappush(frontier, (-upper, serial, chosen, rest, slots))
    upper = max(lower, -frontier[0][0]) if frontier else lower
    return {"basket": [i+1 for i in range(n) if best & (1 << i)], "lower_bound": lower,
            "upper_bound": upper, "absolute_gap": upper-lower, "nodes": visited,
            "status": "exact" if upper == lower else "node_limit"}


def exhaustive(distribution):
    """Small-universe independent comparator; infeasible for 50 choose 13."""
    best, score = None, -1.0
    for basket in itertools.combinations(range(1, distribution.n+1), distribution.k):
        v = distribution.evaluate(basket)
        if v > score:
            best, score = basket, v
    return {"basket": list(best), "value": score}
