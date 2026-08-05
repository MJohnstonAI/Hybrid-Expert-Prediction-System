# HEPS STRATEGIC COMPENDIUM & COGNITIVE SPECIFICATION

This document is the mathematical/semantic operating reference for HEPS agents.

## 1. HEPS v33.4 operating sequence

`Expert nominations → Core/Rescue recall guard → Directional scenarios → Pair-of-Pairs coalition synthesis → 20-line portfolio covering → Frozen artifact → Post-draw attribution`

No downstream stage may receive credit for information that was absent upstream.

## 2. Candidate experts

### Coulomb Void Starvation (`expert_void_bridge`)

Track prolonged absence and under-filled numerical regions. A starvation score may be expressed as:

$$C(x)=1-e^{-\lambda t_x}$$

This is a ranking feature, not an overdue-number probability law.

### Stiction / Shadow (`expert_stiction_shadow`)

Track exact repeat and ±1/±2 numerical neighbourhoods around recent draws. Sorted slots are order statistics, not physical ball trajectories.

### Sorted-position structure (`expert_sorted_momentum`)

Track slot-specific order-statistic distributions and structural compatibility.

### Tri-cluster / register (`expert_tri_cluster_high`)

Generate compact/high-register hypotheses as one lane only. Do not impose a universal high-register multiplier.

### Stale-hot / return horizon

Preserve recurring but rested candidates separately from pure cold/void logic.

### Midfield / structural rescue

Preserve credible central candidates that may otherwise be erased by high-register, hot or void dominance. This is a recall hedge, not a predictive claim.

### Chaos/null control (`expert_chaos_hedge`)

Produce explicit random/control candidates and lines.

## 3. Dual-Pool Candidate Recall Guard

### Core pool

Compact candidate set for dense coalition search. Research range: 13–18 numbers.

### Rescue pool

Broader specialist/structural union. Research range: roughly 22–26 numbers.

Every prediction must report both pool sizes and winner recall after the draw. Pool-size-adjusted nulls are mandatory.

For a uniformly random 5-of-50 target, expected candidate recall for a pool of size `v` is:

$$E[R]=5v/50=v/10$$

Therefore a larger rescue pool cannot be described as improved prediction merely because it captures more winners.

Mechanical-era single-feature 22-number candidate pools are currently approximately null-equivalent. Do not chase weights after one miss.

## 4. Directional Scenario Routing

For sorted main slot `j`, define state:

- `H` if next slot value is greater;
- `L` if lower;
- `R` if equal.

The states are not equiprobable. The exact fair probability of slot `j` taking value `x` in a 5-of-50 draw is:

$$P(X_j=x)=\frac{\binom{x-1}{j-1}\binom{50-x}{5-j}}{\binom{50}{5}}$$

Use this to calculate exact conditional `P(L)`, `P(R)` and `P(H)` relative to the current slot value.

### Required scenarios

1. `null_geometry` — modal H/L/R state from exact fair slot geometry;
2. `hlr_motif_challenger` — frozen symbolic motif rule;
3. optional `director_motif` — user/director hypothesis frozen pre-draw.

HLR is never a hard veto. Disagreement creates separate scenario lines.

### HLR evidence boundary

An 811-draw legacy diagnostic (2018-01-09 to 2025-10-17) was used as a prior only. A 600-train/211-holdout motif classifier underperformed fair modal slot geometry in every main slot and PB. Therefore no global motif edge is accepted.

On 14 testable mechanical-era targets, the frozen legacy PB-direction motif rule scored 9/14 versus 7/14 for the fair modal direction. This remains a challenger signal only.

## 5. Pair-of-Pairs + Anchor synthesis

The v33.3 assembler remains the preferred Stage-C synthesizer.

$$L=P_A\cup\{a\}\cup P_B$$

where `P_A` and `P_B` are supported disjoint pairs and `a` is a compatible anchor.

A soft pair score may retain evidence from void, shadow, adjacency, pair bridge, stale-hot, expert consensus, role complementarity and directional-scenario compatibility. Preserve all provenance.

Do not reject dual-cluster lines merely for containing two compact pairs. The retrospective 2026-07-31 structure `(10,11)+37+(45,46)` remains the canonical assembly example.

## 6. 20-line portfolio protocol

Default v33.4 experimental allocation:

- 8 `core_coalition` lines;
- 4 `rescue_coalition` lines;
- 4 `directional_scenario` lines;
- 2 `maximum_coverage_rescue` lines;
- 2 `random_control` lines.

The 20-line denominator is immutable after freeze.

A 10-line v33.3 slate may still be generated as a separate reduced-budget benchmark.

## 7. Matrix B — PowerBall hierarchy

### B1 Direction

For current PB `p` in the 1–16 pool:

$$P(L)=\frac{p-1}{16},\quad P(R)=\frac1{16},\quad P(H)=\frac{16-p}{16}$$

Score every directional prediction against this conditional null.

### B2 VVD / displacement

A VVD hypothesis may select likely displacement magnitudes after direction is chosen. Its definition must be explicit. Do not silently equate the director's intuitive VVD with simple absolute numeric delta.

### B3 Exact PB

Rank exact candidates using frozen features such as recurrence, capped absence, stale-hot and local shadow. Report exact selection separately from direction and VVD.

## 8. 2026-08-04 diagnostic

Actual main result: `16,24,29,34,38 | PB15`.

Frozen v33.3 hierarchy contained `16` only: candidate recall 1/5. The frozen 20-line slate achieved best main overlap 1/5. This is a candidate-discovery failure, not an assembly failure.

The pre-draw director HLR template `L-H-L-L-H | H` matched actual `H-H-L-L-L | H` in S2, S3, S4 and PB. The PB direction `H (>11)` was a prospective directional hit. The later exact VVD/HLR primary PB13 missed the main PB15; PB13 appearing in XTRA is cross-game diagnostic only.

## 9. Next-target scenario state after 2026-08-04

Current main: `16,24,29,34,38`; PB15.

- null-geometry modal template: `L-L-L-H-H | L`;
- frozen legacy HLR motif template: `L-L-H-H-H | L`.

Only S3 differs in the main-field scenarios. PB direction does not discriminate: both predict lower than 15, and the fair null already assigns `P(L)=14/16=87.5%`.

## 10. PowerBall/XTRA and machine metadata

Main PowerBall and PowerBall XTRA are separate draws. Cross-game matches receive no prospective credit unless the game was explicitly targeted before the draw.

Track machine names when trustworthy metadata are available. Do not infer swaps from result similarity. The alleged 2026-06-22 PowerBall primary-RNG cutover is not accepted as established.

## 11. Post-draw attribution order

1. core-pool recall;
2. rescue-pool recall;
3. HLR/null scenario accuracy with base rates;
4. pair-edge capture;
5. coalition generation;
6. final routing;
7. PB direction;
8. PB VVD/displacement;
9. PB exact hit;
10. Main/XTRA cross-score as retrospective diagnostic only;
11. matched-null comparison.

Do not automatically retune from one target. Claims of predictive advantage require substantially more prospective data and matched random/null controls.
