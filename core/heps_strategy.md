# HEPS Strategy Compendium — Mathematical Reference

This file is a supporting mathematical reference. It is **not** a second architecture authority.

Authoritative sources are:

1. `core/heps_architecture.md` — active staged architecture;
2. `core/expert_registry.yaml` — expert status and allowed authority;
3. `governance/nomenclature.md` — binding concept definitions.

If this compendium conflicts with those files, the architecture/registry/nomenclature governs.

## MAIN_VOID_BRIDGE — Void / Starvation Support

A candidate may receive support from the elapsed draw interval since last appearance or from under-filled numeric regions.

A historical saturating form was:

`C(x) = 1 - exp(-lambda * t_x)`

where `t_x` is the number of draws since coordinate `x` last appeared.

The physical language historically attached to this feature is a hypothesis, not established mechanism. Current use should be described as a coordinate-starvation or void-support statistic unless independent machine evidence exists.

Hard forcing is not currently authorized by the expert registry.

## MAIN_STICTION_SHADOW — Repeat and Near-Coordinate Support

Tracks exact repeats and nearby numeric coordinates such as +/-1 and +/-2 relative to recent winners.

These are measurable numeric relationships. Do not describe them as proven physical stiction or pneumatic paths without direct physical evidence.

Hard forcing is not currently authorized.

## MAIN_SORTED_SLOT_DENSITY — Order-Statistic Support

Models Slot1-Slot5 strictly as sorted order statistics.

Candidate support may be based on empirical slot distributions, theoretical order-statistic expectations, rolling estimates, or other explicitly tested density estimators.

Historical hard examples such as `Slot1 <= 15` or `Slot5 >= 35` are not constitutional boundaries. Any hard boundary must be separately validated and promoted.

## MAIN_HARMONIC_BOUNDARY — Boundary / Register Governor

Maintains exposure against extreme collapse into a narrow region of the field. Historical implementations tracked high-register continuation and correction.

The feature remains low-authority unless stronger validation supports more aggressive use.

## MAIN_TRI_CLUSTER — Cluster Morphology

Tracks structures such as three coordinates falling inside a short numeric span.

Tri-cluster is a morphology/portfolio hypothesis, not a universal rule and not proof of a physical clumping mechanism.

## MORPH_SUM_SPREAD — Sum and Spread

Measures completed-line macro-sum and range/span.

Central values are naturally more common as **classes** under combinatorics. This does not make a specific exact line intrinsically more likely under a fair draw.

Use sum/spread for morphology, compression, or diagnostic scoring only when its combination-space base rate and winner-retention effect are measured.

## PORTFOLIO_CHAOS_BASELINE — Control Lane

Uniform or appropriately matched randomized controls are methodological infrastructure.

The control exists to estimate how much apparent performance can arise from exposure, selection, or chance. It should be preserved even when other experts change.

## Experimental interfaces

The following are defined elsewhere and remain experimental/shadow until promoted:

- `MAIN_HLR_SLOT` — per-slot Low/Repeat/High forecast;
- `MAIN_VVD_DELTA` — Vertical Variance Delta movement magnitude;
- `MAIN_GPR8` — Gap-Phase Residual candidate ranker;
- `MORPH_SLDV` — Sum of Last-Digit Variance morphology;
- `COALITION_PAIR_OF_PAIRS_ANCHOR` — coalition assembly hypothesis;
- `RANK_WINNER_FLOAT` — combination learning-to-rank stage.

Refer to `core/expert_registry.yaml` for current authority.

## Combination score interface

A generic combination score may be written as:

`HEPS_score(C) = sum_j w_j * E_j(C)`

but this equation does not authorize arbitrary weights or imply that all experts operate at the same stage.

The staged architecture should preserve the distinction between:

- slot/state forecasting;
- candidate scoring;
- coalition assembly;
- morphology;
- winner-float ranking;
- final portfolio optimization.

Weights or model parameters may update only under the three-speed learning rules in `core/heps_architecture.md`.

## Legacy top-10 lane allocation

The former fixed allocation of tri-cluster, void, stiction, sorted-momentum, and chaos lines is retained only as a historical/compatibility baseline.

It is no longer an immutable architecture rule. Each frozen draw cycle should declare its portfolio allocation and the evidence or baseline used to justify it.

## Scoring and post-draw learning

`scripts/score_prediction.py` may record evidence from stored pre-draw slates. A single result must not trigger ad-hoc weight changes.

Post-draw Physics of Failure should identify the first stage that lost or suppressed the actual winning coordinates/line and open research questions or parameter evidence accordingly.
