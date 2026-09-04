# E0029 Decision — K13 Pattern-Constraint Triage and Spectral Rescue

## Decision

`ACCEPT AS PROSPECTIVE SHADOW ARCHITECTURE / NO PRODUCTION HARD-PRUNING AUTHORITY`

Evidence classification: `INSUFFICIENT_EVIDENCE`.

Paper trading only.

## What survived the blind replay

The strongest risk-controlled architecture was:

`frozen K13 -> enumerate all 1,287 lines -> Pattern-OR top-80% gate -> preserve E0013 spectral top-5% -> rank retained lines by E0013 spectral -> fixed-budget portfolio`

Canonical shadow name:

`MAIN_PATTERN80_SPECTRAL5_RESCUE`

Across 19 target-excluded oracle-K13 replay targets with 30 random-decoy replicates per target and two independent decoy seeds, the two-seed average was approximately:

- mean exact-winner percentile: `0.63675`;
- median exact-winner percentile: `0.70811`;
- Top-100 rate: `0.16316`;
- above-median rate: `0.69035`;
- mean fraction of K13 lines retained: `0.80273`;
- mean fraction eliminated: `0.19727`;
- winning-line gate survival: `0.92807`.

A random gate retaining the same fraction of lines would retain the winner only about 80.3% of the time. The observed gate survival/space-retention ratio is about `1.16x`.

## Why the 80% gate is preferred over the apparently stronger 50% gate

A 50% Pattern-OR gate produced a slightly higher mean replay percentile, but winner survival fell too far for a system whose objective is to avoid catastrophic elimination.

HEPS therefore chooses the **conservative 80% gate** for prospective shadowing.

The top-5% E0013 spectral rescue is retained because it costs little compression while protecting elite coalition lines that Pattern-OR can reject. It is a bounded preservation rule, not an extra candidate basket or line-budget expansion.

## Pattern-OR interpretation

`Pattern-OR = max(midrank(HLR residual), midrank(LDSAD residual), midrank(SUMAD residual), midrank(SPANAD residual))`.

This is one robustness/meta-pattern operator. It is **not** a product of independent probabilities and must not be described as four independent experts voting together.

The pattern lanes showed sufficiently low target-level dependence in replay to justify continued shadow study, but dependency remains a governance concern.

## Fixed historical bands

The fixed discovery bands:

- LDSAD `11..13`;
- SUMAD `8..9`;
- SPANAD `5..6`;

produced stronger-looking retrospective tiering, especially when followed by E0013 spectral ranking.

They are **not promoted** because the bands were identified after inspecting the same historical outcomes. They remain prospective frozen diagnostics only.

## E0013 and E0022 implications

E0013 spectral remains useful as the downstream ranker. E0029 does not replace its coalition role; it adds a conservative pre-ranking line triage layer.

E0022 Dissent-OR was approximately random in this replay and gains no new authority. E0022 four-plus-first Johnson geometry remains valid downstream portfolio geometry.

## Production boundary

E0029 has:

- zero K13 candidate authority;
- zero PowerBall authority;
- zero production hard-pruning authority;
- zero authority to regenerate historical slates.

For the first fresh target, 2026-09-04, freeze E0029 as a counterfactual shadow against the already frozen K13. Do not change the official slate merely because the discovery replay is favorable.

## Promotion gate

Promotion beyond shadow requires multiple fresh prospective draws showing:

1. winning-line gate survival remains materially above fraction of lines retained;
2. exact-winner rank remains better than E0013 alone and simple/random controls;
3. effect survives independent decoy/randomization reproduction;
4. no post-hoc band retuning;
5. multiplicity/search exposure is controlled;
6. catastrophic pruning remains acceptably low.

## Architecture consequence

Add a new **candidate-frozen Pattern Constraint Triage** shadow stage between K13 enumeration and final coalition ranking:

`Frozen K13 -> enumerate 1,287 -> Pattern Constraint Triage shadow -> E0013 spectral -> optional E0022 four-plus-first Johnson`.

This is the preferred evolved HEPS research architecture from E0029, subject to prospective confirmation.
