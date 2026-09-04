# HEPS v35.3 — Cross-Session Prediction Handoff — 2026-09-04

## Purpose

This handoff is for ChatGPT/Claude/Codex/Gemini agents producing South African PowerBall **Main** or **PowerBall XTRA** prediction slates for the 2026-09-04 draw cycle.

Read this before revising any slate.

## Binding read order

1. `AGENTS.md`
2. `governance/current_method_doctrine.md`
3. `governance/methodology_deprecations.md`
4. `core/heps_architecture.md`
5. `experiments/E0026/hypothesis.md`
6. `experiments/E0026/protocol.yaml`
7. `experiments/E0026/decision.md`
8. `experiments/E0028/hypothesis.md`
9. `experiments/E0028/protocol.yaml`
10. `experiments/E0028/results.json`
11. `experiments/E0028/decision.md`
12. `experiments/E0029/hypothesis.md`
13. `experiments/E0029/protocol.yaml`
14. `experiments/E0029/results.json`
15. `experiments/E0029/decision.md`
16. `knowledge/PATTERN_CONSTRAINT_K13_HANDOFF_2026-09-04.md`
17. `knowledge/LAST_DIGIT_ABS_DELTA_HANDOFF_2026-09-04.md`
18. `knowledge/ASSEMBLY_EVOLUTION_HANDOFF_2026-09-02.md`

## Current architecture

HEPS is now:

`HEPS v35.3 — Joint-Distribution-First Staged Mixture-of-Experts with Candidate-Frozen Pattern Triage`

The operational Main flow is:

`slot/signed-transition state -> E0026 scenario-constrained slot-routed K13 acquisition -> freeze K13 -> enumerate all C(13,5)=1,287 lines -> E0029 candidate-frozen Pattern Constraint Triage -> E0013 spectral coalition ranking -> optional E0022 four-plus-first Johnson portfolio -> separate PB model`.

Do not use pattern morphology to silently change K13 membership unless a separately governed acquisition experiment authorizes it.

## E0026 acquisition doctrine

Do not collapse candidate evidence to unrestricted anywhere probability.

Preserve:

`candidate coordinate + admissible slot provenance + transition-scenario probability`.

HLR is a scenario distribution, not a certainty. Adjacent-slot migration is allowed only when a non-negligible pre-draw scenario, signed displacement, exact order-statistic support, and legal sorted-line geometry permit it.

K remains fixed for matched comparisons. K expansion receives no predictive credit.

## E0029 pattern-triage discovery

E0029 tested pattern recognition **after K13 freeze** using target-excluded Main Mechanical-Era replay.

Adaptive pattern lanes:

- BARP/HLR residual relative to exact structural HLR null;
- LDSAD residual: absolute change in the sum of the five last digits;
- SUMAD residual: absolute change in total Main-number sum;
- SPANAD residual: absolute change in draw span `S5-S1`.

Define:

`MAIN_PATTERN_OR = max(midrank_pct(HLR), midrank_pct(LDSAD), midrank_pct(SUMAD), midrank_pct(SPANAD))`.

This is one robustness/meta-pattern operator, not four independent expert votes and not a product of likelihoods.

Preferred discovery cascade:

`MAIN_PATTERN80_SPECTRAL5_RESCUE`

1. enumerate all 1,287 legal lines inside frozen K13;
2. retain top 80% by adaptive Pattern-OR;
3. rescue any line in the top 5% of E0013 spectral;
4. rank retained lines by E0013 spectral;
5. keep excluded lines in the audit artifact;
6. apply fixed-budget portfolio geometry only afterward.

Discovery replay summary across 19 target-excluded oracle-K13 targets, 30 decoy reps/target and two seeds:

- mean exact-winner percentile approximately `0.637`;
- median approximately `0.708`;
- winner above median approximately `69%`;
- Top-100 approximately `16.3%`;
- mean fraction lines retained approximately `0.803`;
- mean fraction lines eliminated approximately `0.197`;
- winning-line gate survival approximately `0.928`.

A same-size random gate would retain the winner only approximately 80.3% of the time, so the discovery retention/compression ratio is about `1.16x`.

Evidence remains `INSUFFICIENT_EVIDENCE`: E0029 is prospective shadow, not confirmed production hard pruning.

## E0028 LDSAD discovery

Canonical statistic:

`SLD_t = sum(n mod 10 for the five main numbers)`

`LDSAD_t = abs(SLD_t - SLD_(t-1))`.

Main discovery band through 2026-09-01:

`LDSAD 11..13`

Observed `11/26 = 42.31%`; exact IID 5/50 expectation approximately `10.94%`.

Broader frozen challengers:

- `10..13`;
- `9..13`.

These bands were identified post-hoc and therefore have **zero historical confirmation credit**. They may be reported as frozen prospective diagnostics but may not receive automatic hard-pruning authority.

## Main 2026-09-04 state

Canonical Main cutoff: `2026-09-01`.

Previous Main result:

`14,16,31,34,40 | PB4`.

Current frozen Main K13 from the existing cycle artifact:

`3,8,18,19,20,23,32,34,35,39,40,48,50`.

Existing E0029 pre-draw shadow artifact:

`cycles/2026-09-04/pre_draw/e0029_pattern_constraint_shadow.json`.

It retains 1,043/1,287 K13 lines and shadow-eliminates 244.

E0029 current top six from that frozen K13:

1. `18,32,34,35,50`
2. `8,19,20,39,48`
3. `3,19,20,39,48`
4. `3,8,19,39,48`
5. `8,19,20,23,39`
6. `19,20,23,39,48`

The director-assisted line `19,20,23,39,48` is protected by the top-5% E0013 spectral rescue despite weak Pattern-OR support.

## Slate revision rule for Main

The director has authorized replacing an earlier frozen slate **only if there is a genuine pre-draw improvement**.

Therefore a Main session may issue a revised slate for 2026-09-04 if it can document, before outcome knowledge:

- the exact canonical cutoff;
- the unchanged or explicitly justified K13 acquisition state;
- E0026 slot/scenario provenance;
- all 1,287 lines enumerated;
- E0029 Pattern-OR scores;
- E0013 spectral rescue/rank;
- the fixed line budget;
- why the revision is materially stronger than the previous slate rather than merely different.

Do not revise from post-hoc intuition or because a newly discovered fixed morphology band happens to favor a desired line.

## K13 versus larger reserve pools

K13 remains the preferred primary acquisition pool because larger K increases winner-coordinate coverage but causes combinatorial dilution:

- K13 -> 1,287 lines;
- K15 -> 3,003;
- K17 -> 6,188;
- K20 -> 15,504.

Do not flatten a K17/K20 reserve into the primary assembly universe without a separately governed same-budget experiment.

A future architecture may use `K13 core + bounded reserve escape lines`, but that is not yet production authority for tonight.

## PowerBall

PowerBall remains a separate 1..16 prediction problem. Main-number pattern success does not transfer PB authority.

Use the latest strongly-shrunk PB model/baselines for the relevant lane. Do not multiply PB HLR/VVD/terminal/exact-state projections as independent evidence.

## XTRA transfer rule

**Transfer method, not fitted Main state.**

For XTRA:

- use only the canonical XTRA Mechanical-Era ledger beginning 2026-06-02;
- do not import Main candidates, HLR motifs, E0013 graph state, LDSAD band 11..13, SUMAD bands, SPANAD bands, pair counts, or fitted weights;
- fit XTRA HLR/signed-transition state independently;
- derive an XTRA-specific K13;
- enumerate all 1,287 XTRA K13 lines;
- compute XTRA-specific adaptive LDSAD/SUMAD/SPANAD residuals from only prior XTRA draws;
- form an XTRA Pattern-OR only as a new shadow unless already frozen prospectively;
- do not assume Main E0013 spectral transfers: previous XTRA tests did not reproduce the Main spectral signal;
- use XTRA-appropriate coalition/ranking controls and optional Johnson geometry only after the candidate universe is frozen;
- fit XTRA PowerBall independently.

If fixed XTRA LDSAD/SUMAD/SPANAD bands are discovered now from historical outcomes, label them post-hoc discovery and do not claim confirmation.

## Required prediction output — Main and XTRA

Each session should return:

1. canonical cutoff and data provenance;
2. HLR/signed-transition scenario distribution;
3. frozen K13 with candidate-slot provenance;
4. any bounded reserve candidates, clearly separated from K13;
5. total number of legal K13 lines = 1,287;
6. Pattern-OR triage summary;
7. coalition/ranking method and tie rule;
8. Top 20 ranked Main-number lines before portfolio compression;
9. final recommended slate at the declared line budget;
10. separate PowerBall ranking/selection;
11. evidence/authority labels for every new component;
12. comparison with the prior frozen slate and explicit statement whether a supersession is justified.

## Evidence language

Do not call v35.3 or E0029 a predictive breakthrough yet.

Current interpretation:

- E0026 slot-routed acquisition: `INSUFFICIENT_EVIDENCE / prospective shadow design`;
- E0028 LDSAD fixed bands: `INSUFFICIENT_EVIDENCE / prospective shadow`;
- E0029 Pattern Constraint Triage: `INSUFFICIENT_EVIDENCE / prospective shadow architecture`;
- E0013 Main spectral: `PROVISIONAL_SIGNAL / coalition shadow`;
- E0022 four-plus-first Johnson: accepted deterministic portfolio geometry, not prediction.

The objective for tonight is not to manufacture confidence. It is to use the strongest pre-draw architecture currently available while preserving auditability and avoiding known HEPS failure modes.
