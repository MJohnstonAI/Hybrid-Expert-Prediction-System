# E0021 — Joint Signed-Displacement Legal-Line Acquisition

## Status

`PROPOSED DESIGN / NO PROSPECTIVE AUTHORITY YET`

Evidence classification: `INSUFFICIENT_EVIDENCE`.

Paper trading only.

## Origin

E0021 is the corrected successor to the probability-field component of E0019 after the Longcat 2.0 mathematical review, HEPS red-team verification, and the 2026-09-01 Main post-draw audit.

It retains E0019's useful complete-line containment objective while replacing the mathematically unjustified HLR×VVD residual product.

## Core hypothesis

A Main candidate field built from **one regularized signed-displacement transition representation per sorted slot**, expressed as a residual tilt relative to exact structural slot geometry and then normalized over the complete legal 5/50 line space, can improve prospective probability calibration and fixed-K candidate containment versus:

- exact structural null;
- E0019 historical HLR×VVD field;
- simple frequency/recency;
- marginal Top-K compression;
- E0016 nonequilibrium-current shadow.

The key question is not whether E0021 can retrospectively generate recent winners. The key question is whether its full probability field improves proper score first, then preserves future winners at identical K.

## Canonical transition

For previous slot coordinate `p_j` and next coordinate `x_j` define:

`DELTA_j = x_j - p_j`.

HLR, VVD, exact coordinate and terminal digit are derived views of `DELTA_j`; they do not enter as independent expert likelihood multipliers.

## Slot residual model

For slot `j`:

- `P0_j(x)` = exact order-statistic slot null;
- `q_j(x | p_j, history)` = strongly regularized learned transition distribution;
- `T_j(x) = q_j(x | p_j, history) / P0_j(x)` = learned **residual ratio** on legal support.

A convenient parameterization is:

`q_j(x) proportional to P0_j(x) * exp(phi_j(x-p_j))`

with low-dimensional/heavily shrunk `phi_j` estimated only from rows before the target.

## Correct joint legal-line model

The exact IID line null is uniform over legal sorted lines:

`P0_line(x)=1/C(50,5)` for `x1<...<x5`.

For legal line `x=(x1,...,x5)` define:

`Q(x) = P0_line(x) * product_j T_j(x_j)`

and normalize:

`P(x) = Q(x) / sum_legal_y Q(y)`.

Because `P0_line` is constant over legal lines, ranking weights are proportional to `product_j T_j(x_j)`, but the probabilistic baseline remains the exact uniform legal-line null.

### Mandatory null-recovery sanity check

If every learned slot model equals its exact structural null, then every `T_j=1` and E0021 must reduce **exactly** to the uniform legal 5/50 line distribution.

Do not use `product_j q_j(x_j)` as the joint line field. Multiplying the five slot probabilities would multiply order-statistic geometry across dependent slots and would not recover the exact uniform line null when no residual signal exists.

This factorization is a low-dimensional residual parameterization, not a claim that physical or sorted slots are independent.

## Candidate objective

For candidate set `K` of size 13:

`M(K) = sum_{x subset K, |x|=5} P(x)`.

Select/optimize K13 without changing K. Compare against exact matched-exposure controls.

## Adjacent-slot preservation challenger

The 2026-09-01 audit motivates a separate fixed-K challenger that may preserve up to two coordinates with strong **anywhere-coordinate** support derived from an adjacent slot, but only by displacing existing K13 members. No K expansion or union credit.

This challenger must be scored separately from the base E0021 K13.

## Required evidence order

1. full legal-line / coordinate proper score versus structural/simple baselines;
2. exact null-recovery unit test;
3. K13 winner-coordinate recall at identical exposure;
4. 3+/4+/5/5 survival and catastrophic exclusions;
5. complete-line containment probability;
6. downstream coalition/ranking only after acquisition is scored.

A K13 recall gain with worse proper score is not a promotable predictive lift.

## Falsification

Reject/demote if:

- the implementation fails exact null recovery when residual potentials are zero;
- full probability field does not beat structural/simple baselines prospectively;
- K13 lift disappears under matched controls or independent reproduction;
- adjacent-slot preservation merely exchanges one noisy seat for another without persistent benefit;
- gains require target-conditioned tuning;
- the model collapses to a high-variance displacement table unsupported by the sample size.

## Authority

No production or hard-pruning authority. E0021 begins as a methodology/candidate-funnel shadow after implementation and prospective freeze.