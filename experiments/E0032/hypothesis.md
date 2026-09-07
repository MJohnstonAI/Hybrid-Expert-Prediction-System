# E0032 — Astra K13 Red-Team and Multi-Objective Compression Championship

**Date:** 2026-09-07  
**Status:** active prospective shadow  
**Evidence classification:** `INSUFFICIENT_EVIDENCE`  
**Stage:** candidate_funnel | methodology  
**Paper trading only:** true

## Purpose

Independently audit the mathematical fixed-K13 contribution preserved in
`collaboration/contributions/Astra_codex_2026-09-07/` and operationalize only the
parts that survive review.

This experiment deliberately separates two problems:

1. **probability estimation:** construct a coherent pre-target distribution `P(X)` over legal 5/50 lines;
2. **decision compression:** given that already-frozen `P(X)`, choose exactly 13 coordinates under a declared utility.

E0032 does **not** fit a new predictive probability model. A compressor cannot create information that is absent from, or misspecified in, the upstream field.

## Astra claims under review

1. There is no objective-independent optimal K13.
2. For expected retained winners, `Top13` anywhere-coordinate marginals are globally Bayes-optimal.
3. Four-plus survival and complete 5/5 containment depend on joint information and need not be maximized by marginal Top13.
4. For the HEPS slot-product residual field, normalization, slot/anywhere marginals and fixed-basket hit-count probabilities can be computed exactly by dynamic programming without enumerating all `C(50,5)=2,118,760` lines.
5. Exact evaluation of a basket is distinct from globally optimizing over all `C(50,13)=354,860,518,600` baskets.

## Prospective fixed-K13 arms

All arms use the **same frozen probability field** and exactly `K=13`.

- `K13_MEAN`: maximize `E[H]`, where `H=|X∩B|`. This is exactly Top13 anywhere-coordinate marginals.
- `K13_4PLUS`: maximize `P(H>=4)` as a shadow optimization objective.
- `K13_5`: maximize `P(H=5)` / complete-line containment mass `M(B)` as a shadow optimization objective.
- `K13_ROBUST`: lexicographically minimize `P(H<=1)`, then maximize `P(H>=4)`, then `P(H=5)`, then `E[H]`.

For the three nonlinear arms, a local/multistart optimizer is **not** called globally optimal unless a valid global certificate closes the remaining bound. Best-found and certified-optimal are separate statuses.

## Primary research question

Does objective choice materially change fixed-K13 winner survival on future targets when the underlying probability field and exposure are held constant?

## Key falsification

E0032 fails to justify a compression change if:

- the upstream probability field is worse than structural/simple controls on prospective proper score;
- the four arms are effectively identical;
- nonlinear arms do not improve their declared prospective hit-count utility relative to `K13_MEAN`;
- apparent gains rely on target-conditioned tuning, K expansion, or post-result optimizer changes;
- an implementation fails exact uniform-null recovery or synthetic exhaustive checks.

## Authority

Shadow comparison only. No production authority, no K change, no hard exclusion authority, and no permission to rewrite a frozen prediction. Any 2026-09-08 numerical basket must be generated and frozen before result knowledge from a separately frozen upstream probability field.