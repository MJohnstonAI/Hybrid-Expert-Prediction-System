# HEPS Post-2026-08-14 Research Synthesis

## Status

Research synthesis only. No active architecture promotion is authorized by this document.

Evidence classification for all newly proposed predictive experts: `INSUFFICIENT_EVIDENCE` unless explicitly stated otherwise.

## 1. Draw outcome and immediate lesson

Director-reported 2026-08-14 result pending approved-source verification:

`14,15,19,39,44 | PB3`

Previous state:

`3,14,26,40,48 | PB10`

Actual HLR: `HHLLL`  
Actual VVD: `[11,1,7,1,4]`

The first failure stage of the frozen E0004 challenger was candidate acquisition: only winner44 survived its candidate union.

## 2. Structural-null result

For prior state `[3,14,26,40,48]`, the exact marginal HLR modal directions were `HHLLL`, matching all five actual slot directions. The exact joint `HHLLL` vector had probability about 9.798% and rank 3 among 243 HLR vectors.

This is a mathematical baseline success, not predictive lottery edge. It reinforces the requirement that learned HLR/VVD models demonstrate residual information beyond sorted-order geometry.

## 3. VVD first prospective failure and research direction

E0003 froze:

- Slot1 VVD9 -> 12; actual VVD11 -> 14.
- Slot3 VVD5 -> 21/31; actual VVD7 -> 19.
- Slot5 VVD2 -> 46/50; actual VVD4 -> 44.

All three exact point hypotheses missed. The common post-draw residual was `actual = forecast + 2`. This is not a success and must not be retrospectively absorbed into E0003.

The preferred research response is **VVD-R**, a distributional residual model:

`P(D_j=d | state) proportional to NULL_VVD_STRUCTURAL(d | previous slot) * R_j(d)`

where `R_j(d)` is learned with strong shrinkage and frozen walk-forward rules. Any `+2` residual hypothesis must be a preregistered sub-challenger with zero historical credit.

## 4. Grok contribution: BARP

Grok proposed Boundary-Adjusted Run Persistence (BARP): state-duration modelling of HLR persistence versus flip after partial structural-null adjustment.

Before 14 August, Slot2 ended in a double-LOW run. Historical active-era transition counts and the exact structural null both favoured a HIGH next state. A later conversation-stage challenger therefore preferred Slot2 HIGH and nearest coordinate15; actual Slot2 was15.

Because this synthesis was not durably frozen as the E0004 prediction and BARP has essentially no prospective sample, BARP remains `INSUFFICIENT_EVIDENCE`.

BARP must be formalized with:

- deterministic H/L run-length definition;
- explicit REPEAT handling;
- hierarchical shrinkage for sparse run lengths;
- full LOW/REPEAT/HIGH probabilities;
- paired Brier/log-loss comparison against `NULL_HLR_STRUCTURAL` and plain empirical HLR.

## 5. Candidate-coordinate versus slot-assignment separation

Friday strengthens the need to distinguish:

- global candidate inclusion: `P(n appears anywhere)`;
- exact-slot assignment: `P(n occupies Slot j)`.

Examples:

- winner14 was an exact repeat of prior coordinate14 but migrated from prior Slot2 to actual Slot1;
- winner39 was a `-1` shadow of prior40;
- winner15 was `+1` from prior14.

Coulomb candidate support existed for several actual winners but concentrated slot-lattice consensus did not preserve all of them.

## 6. Proposed Coordinate Mobility / Slot Migration expert

New research question: can a coordinate with strong global support survive while changing sorted slot?

Required outputs:

1. global appearance score for number `n`;
2. conditional distribution over slot assignment given appearance;
3. mobility feature describing historically observed slot transitions without treating sorted slots as physical trajectories.

The expert must beat recency/frequency/Coulomb-only controls at matched basket exposure before receiving authority.

## 7. Expert-preservation / Core+Rescue architecture

Friday supports testing a candidate basket with controlled dissent. A prior design concept is `Core9 + Rescue4 = K13`, but quotas are not fixed production doctrine.

Potential rescue families:

- exact structural rescue;
- Coulomb repeat/shadow preservation;
- coordinate-mobility rescue;
- adversarial/diversity rescue.

Success must be measured by 3+/4+/5/5 winner-coordinate survival at identical K against incumbent, recency, frequency, and random controls.

## 8. Gemini contribution and JOS-HDR red team

Gemini correctly identified a weakness in evaluating slots independently: independently plausible slot coordinates can form poor joint states.

However its proposed Joint Order-Statistic Highest Density Region (JOS-HDR) under the exact 5/50 null is mathematically invalid as an exact-line density selector.

For legal sorted line `S`, the six-gap vector

`G=(S1-1,S2-S1-1,S3-S2-1,S4-S3-1,S5-S4-1,50-S5)`

is a one-to-one mapping to weak compositions of45 into6 parts. Under `NULL_GAP_DM = DirichletMultinomial(45,[1,1,1,1,1,1])`, all `C(50,5)=2,118,760` exact gap compositions are equally probable. There is therefore no exact-line high-density subset under this null.

For a fixed K22 with no predictive information:

`P(5/5 in K22)=C(22,5)/C(50,5)≈1.243%`, not 90%.

Gemini's reported 7/10 K22 5/5 backtest is rejected as evidence because several target winning vectors did not match the canonical HEPS ledger, including 24 Jul, 28 Jul, 04 Aug, 11 Aug, and 14 Aug.

The useful derivative idea is retained: model **joint feature-class residuals**, not exact-line density.

## 9. Joint VVD-Gap Residual research direction

Candidate features for exact-null-adjusted joint compatibility include:

- total span and span change;
- boundary gaps;
- min/max internal gap;
- gap entropy / imbalance;
- full gap-vector displacement;
- signed five-slot movement vector;
- joint VVD magnitude pattern.

For feature class `phi`, compare observed frequency with its exact combinatorial base rate, using heavy shrinkage:

`R(phi)=P_observed(phi)/P_null(phi)`.

Initial authority: diagnostic/soft compatibility score only. No hard pruning.

## 10. Pari-mutuel hypergraph proposal

Gemini's crowd co-occurrence hypergraph may be relevant to payout-sharing optimization if actual South African ticket-selection data can be obtained. It does not increase winning probability and must not prune predictive candidates.

Without empirical crowd data, birthday/grid/arithmetic weights are speculative.

## 11. Main/XTRA cross-game rescue observation

The director reported that an independently generated XTRA prediction happened to contain Main winners14,39,44.

Do not infer that XTRA predicts Main. Treat it as a possible orthogonal diversification/rescue observation.

Prospective protocol:

- freeze Main and XTRA independently;
- measure cross-game winner-coordinate rescue;
- preserve exposure denominators;
- compare against matched random baskets;
- do not let cross-game information affect target-game prediction until evidence accumulates.

## 12. PowerBall research lesson

Conversation-stage reasoning favoured a LOW PowerBall from prior10, with exact shortlist5/8/9. Actual PB3 was LOW, so the direction worked and exact-ball selection failed.

Future PB research should score direction/state separately from exact-number probability and should not infer main-field evidence from PB performance.

## 13. Proposed candidate architecture under research

Conceptual challenger only:

`Exact Structural Null`

`+ BARP direction`

`+ VVD-R magnitude`

`+ Coulomb coordinate field`

`+ Coordinate Mobility`

`-> Multi-expert candidate field`

`-> Expert-preservation rescue`

`-> Joint VVD/Gap residual compatibility`

`-> frozen K`

`-> Johnson assembly`

`-> morphology/ranking`

No part of this synthesis is promoted to `core/heps_architecture.md` until experiment, reproduction, red-team and promotion requirements are met.

## 14. Research priorities after 14 August

1. BARP proper-score championship versus exact HLR null.
2. VVD-R distributional residual versus exact VVD null.
3. Coordinate Mobility / Slot Migration candidate survival.
4. Expert-preservation Core+Rescue basket at matched K.
5. Joint VVD-Gap residual compatibility.
6. Main/XTRA orthogonal rescue control.
7. Prospectively test the observed `+2` VVD residual without modifying E0003.

## 15. Scientific guardrails

- Do not rewrite E0003/E0004 frozen files.
- Do not count wrong-slot coordinate retention as exact-slot success.
- Do not promote Friday's structural HLR success as predictive edge.
- Do not transform the post-draw `+2` residual into retrospective VVD credit.
- Do not treat expert consensus itself as an independent source of probability.
- Candidate acquisition remains the current bottleneck; Johnson begins only after K is frozen.
