# Contribution — HEPS v33.4 Candidate Recall Guard + Directional Scenario Routing

Contributor: ChatGPT Sol
Date: 2026-08-05
Status: PROPOSED EXPERIMENTAL CORE UPGRADE

## Problem statement

HEPS v33.3 improved coalition assembly, but the 2026-08-04 prospective test failed upstream: the frozen 22-number hierarchy contained only one of the five eventual winners. Assembly logic cannot repair a candidate-discovery miss.

At the same time, the user/director's pre-draw HLR PowerBall direction hypothesis correctly called `H (>11)`, with PB15 drawn. This is useful as a specialist signal, but legacy holdout testing shows H/L/R motif repetition is mostly explained by ordinary slot geometry and is not strong enough for universal weighting.

## Proposed architecture

### Stage A1 — Expert nominations

Preserve each expert's ranked nominations and provenance. Do not collapse all evidence into one averaged scalar before deciding who enters the working pools.

### Stage A2 — Dual-Pool Recall Guard

Maintain two distinct candidate sets:

- `core_pool`: compact model-selected candidates optimized for coalition density;
- `rescue_pool`: broader specialist/structural candidates designed to reduce catastrophic omission risk.

Report recall for both pools separately. The rescue pool is not evidence of predictive edge; it is a risk-control device.

Recommended research sizes for 20-line slates:

- core: 13–18 candidates;
- rescue union: approximately 22–26 candidates, depending on expert overlap.

Do not declare one pool size optimal until end-to-end recall × assembly performance is measured prospectively.

### Stage B — Directional Scenario Router

Treat H/L/R as a scenario generator, not a hard filter.

At minimum preserve:

1. `null_geometry`: for each sorted slot, choose the modal H/L/R state implied by the exact fair 5/50 order-statistic distribution conditional on the current slot value;
2. `hlr_motif_challenger`: symbolic motif continuation based on a frozen pre-target rule;
3. optional `director_motif`: a human/director HLR hypothesis if explicitly frozen before the draw.

When scenarios disagree, allocate separate lines. Do not tune one scenario after the target is known.

### Matrix B — Hierarchical PowerBall routing

Split PowerBall prediction into:

1. direction: H/L/R;
2. displacement/VVD challenger;
3. exact-ball ranking.

Every direction call must be benchmarked against the exact fair conditional probability from the current PB value. Example: after PB15 in a 1–16 pool, `L` has null probability 14/16 = 87.5%; a lower next PB would therefore be a weak directional success unless the exact-ball layer also adds information.

### Stage C — Coalition intelligence

Keep the v33.3 Pair-of-Pairs + Anchor assembler unchanged. Apply it after candidate-pool and scenario creation.

### Stage D — 20-line research portfolio

Recommended experimental allocation:

- 8 core-pool coalition lines;
- 4 rescue-pool specialist coalitions;
- 4 directional-scenario lines split across null geometry and HLR challenger;
- 2 maximum-coverage rescue lines;
- 2 matched random/control lines.

All 20 lines are scored. No post-draw substitution is permitted.

## Evidence

### 2026-08-04 prospective failure

- frozen candidate hierarchy recall: 1/5;
- best final 20-line overlap: 1/5;
- exact PB15 existed on two frozen lines, with zero main hits on those lines;
- failure label: candidate discovery.

### Candidate-feature walk-forward

At a 22-number pool across 16 mechanical-era targets (min_train=3):

- hot 2.000 winners/draw;
- cold_void 2.250;
- stiction_shadow 1.938;
- pair_bridge 2.000;
- midfield 2.125;
- high_register 2.250;
- random expectation 2.200.

This does not support aggressive post-draw weight tuning.

### HLR evidence boundary

Legacy 811-draw diagnostic shows motif classification underperforms exact fair modal slot geometry in a 211-draw holdout. HLR therefore remains challenger-only.

Mechanical PB direction is more interesting but tiny: 9/14 motif hits versus 7/14 fair-mode hits for the testable targets. This is hypothesis-generating, not statistically persuasive.

## Acceptance criteria

Promote the dual-pool recall guard and scenario-routing *methodology* if it improves auditability and prevents expert erasure. Do not promote any claim of predictive edge until prospective recall, line-level overlap and matched-null metrics accumulate.
