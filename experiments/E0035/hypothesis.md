# E0035 — Bayesian-Bootstrap Uncertainty-Aware Fixed-K13 Compression Championship

**Date opened:** 2026-09-15  
**Status:** active experimental / prospective-shadow candidate  
**Evidence classification:** `INSUFFICIENT_EVIDENCE`  
**Stage:** candidate_funnel | methodology  
**Paper trading only:** true

## Motivation

The 2026-09-04, 2026-09-08 and 2026-09-11 Main targets each produced only `1/5` winner-coordinate survival in the frozen K13. On 2026-09-11 the point-estimate anywhere ranking still placed three actual winners in its Top20, showing that small score differences around the K13 cutoff can become categorical exclusions.

E0035 tests whether **uncertainty in the estimated probability field** should enter the fixed-K13 decision itself.

The experiment deliberately does **not** invent a new upstream predictive signal. It holds the existing E0030 near-null probability family fixed and changes only the compression decision.

## Core hypothesis

When the upstream field is weak and coordinate ranks are unstable, a K13 optimized against a posterior-predictive distribution over plausible fields may reduce catastrophic `0/1` winner exclusions relative to a K13 optimized against one point-estimated field.

For basket `B`, `|B|=13`, and `H_B=|X∩B|`, the primary challenger seeks to minimize posterior-predictive `P(H_B<=1)`, then lexicographically maximize `P(H_B>=4)`, `P(H_B=5)`, and `E[H_B]`.

## Upstream probability model is frozen

E0035 uses the already-defined E0030 adaptive mixture unchanged:

- uniform fixed-cardinality subset model;
- cumulative-frequency subset model with coordinate weight `1 + count/10`;
- recent-five subset model with coordinate weight `1 + count_recent5/10`;
- initial component prior `0.8 / 0.1 / 0.1`;
- sequential component likelihood updating using only previously revealed targets;
- fixed 50% uniform floor.

No E0035 result may be interpreted as repairing the upstream model's proper-score deficit. Compression cannot create predictive information.

## Parameter-uncertainty representation

For each walk-forward target, construct a deterministic-seed Bayesian-bootstrap posterior predictive field using only target-excluded history:

- `16` Bayesian-bootstrap replicates;
- cumulative-history draw weights sampled from Dirichlet(1,...,1), implemented with normalized Exp(1) variates;
- recent-five weights bootstrapped independently over the fixed recent-five window;
- weighted counts pass through the unchanged E0030 `1 + count/10` formula;
- E0030 component mixture weights remain target-excluded sequential weights and are not retuned by E0035;
- the uniform component remains exact and unbootstrapped.

This produces a coherent finite posterior-predictive mixture of exactly normalized fixed-cardinality subset distributions.

## Fixed-K13 arms

All arms use exactly `K=13`.

1. `POINT_MEAN` — point E0030 field; exact Top13 anywhere marginals.
2. `POINT_ROBUST` — point E0030 field; deterministic multi-start one-swap robust objective.
3. `BB_MEAN` — Bayesian-bootstrap posterior predictive field; exact Top13 posterior-predictive anywhere marginals.
4. `BB_ROBUST` — primary E0035 challenger; deterministic multi-start one-swap robust objective on the posterior-predictive field.

Nonlinear arms are best-found local solutions, not globally certified optima.

## Replay / prospective boundary

Replay through 2026-09-11 is post-hoc discovery evidence. It receives zero prospective confirmation credit.

If implementation and sanity checks pass, the first eligible prospective shadow target is **2026-09-15**, using the canonical ledger through 2026-09-11 only.

## Primary metrics

At matched K13 exposure:

- total winner coordinates retained;
- mean retained winners per target;
- catastrophic draws `H<=1`;
- draws with `H>=3`, `H>=4`, and `H=5`;
- paired hit-count delta versus `POINT_MEAN`;
- basket disagreement versus `POINT_MEAN`;
- exact hypergeometric random-K13 controls.

## Falsification / downgrade

E0035 does not justify a compression change if `BB_ROBUST` is effectively identical to `POINT_MEAN`, catastrophic exclusions do not decline, gains require K expansion or target-conditioned tuning, normalization/reproduction checks fail, or any compression gain is misrepresented as upstream predictive lift.

## Authority requested

Discovery replay only plus prospective shadow from 2026-09-15 if frozen pre-result. No production authority, no K change, no alteration of E0033 assembly semantics, and no predictive `BREAKTHROUGH` claim without repeated prospective evidence and a proper-score-qualified upstream field.
