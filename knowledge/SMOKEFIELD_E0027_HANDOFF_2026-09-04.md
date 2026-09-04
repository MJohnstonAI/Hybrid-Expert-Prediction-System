# HEPS Main — E0027 SmokeField Handoff

## Bottom line

E0027 tested the proposed smoke/diffusing-particle abstraction as a Main-only shadow championship.

Decision: **do not promote SmokeField into predictive HEPS architecture**.

## Tested components

- slot velocity/orientation;
- acceleration persistence;
- exact non-crossing slot ordering;
- adjacent-gap dispersion;
- adjacent-gap mean-reversion / pressure;
- all-pair separation collision ranking;
- signed-transition + pair/gap combinations.

## What failed

Acceleration/inertia was materially worse than the exact uniform legal-line null.

Plain gap-dispersion worsened the signed-transition field.

All-pair collision/separation ranking was effectively random and did not improve matched oracle-K13 winner percentile over signed transition.

No SmokeField K13 challenger produced 4+/5 or 5/5 containment across the 19 eligible walk-forward targets.

## One narrow useful observation

Gap-pressure regularization improved the tested signed-transition Brier score on 14/19 targets and improved its mean log score, but the resulting model still failed to beat the exact uniform null and did not improve K13 capture.

Interpretation: **regularizer, not independent information source**.

It may be revisited only inside a future repaired signed-transition model under a preregistered proper-score test. It must not receive an expert vote or separate ensemble weight.

## E0026 relationship

E0026 Scenario-Constrained Slot-Routed K13 Acquisition remains active as a methodological proposal.

E0027 does not invalidate E0026 because E0026 is about preserving candidate-slot provenance and scenario-valid routing, not about physical diffusion.

The non-crossing idea is already correctly represented in E0026 by exact legal sorted-line constraints.

## Friday 2026-09-04

E0027 has **zero authority** to revise Main K13 or the frozen slate.

Read:

1. `experiments/E0027/results.json`
2. `experiments/E0027/decision.md`
3. `experiments/E0027/protocol.yaml`
4. `experiments/E0016/`
5. `experiments/E0026/`
