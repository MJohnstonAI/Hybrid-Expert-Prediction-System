# PowerBall XTRA — Post-Draw Audit — 2026-08-28

**Result (director supplied, independently corroborated by non-official public source):** `3,4,16,35,38 | PB15`  
**Mode:** `paper_trading_only`  
**Status:** post-draw audit; official single-source repository verification still pending before canonical ledger append.

## 1. Frozen artifacts scored

This audit preserves all pre-draw artifacts unchanged and scores:

1. `cycles/2026-08-28/powerball_xtra_pre_draw.md` — original incumbent forecast;
2. `cycles/2026-08-28/xtra_e0016_working_state_shadow.json` — late Richardson-integrated working-state challenger;
3. `cycles/2026-08-28/xtra_pb_director_repeat_vvd10_shadow.md` — director PB16/PB6 shadow.

No retrospective prediction credit is assigned to formulas or coordinates not frozen before the draw.

## 2. Realized state transition

Previous working state: `4,7,15,18,29 | PB16`.

Actual transition:

- main HLR: `L,L,H,H,H`;
- PB HLR: `L`;
- main VVD: `[1,3,1,17,9]`;
- PB VVD: `1`;
- main sum: `96`;
- terminal-digit sum: `3+4+6+5+8 = 26`.

The frozen primary direction was `H,H,H,H,H | L`. It therefore hit main direction in S3-S5 = 3/5 and PB LOW, but missed S1 and S2.

Exact enumeration of the legal 5/50 space gives `P0(LLHHH) ≈ 0.03465046` from the previous state. Including PB LOW from16 gives about `0.03248480`. Thus the realized directional vector was uncommon but not remotely negligible; a full distribution-first system should preserve it.

Conditional on the exact `LLHHH` event, the realized sum96 is around the 26.5th percentile. The failure was therefore not that the draw was an extreme morphology outlier after conditioning on its actual direction vector.

## 3. Original incumbent candidate acquisition

Frozen Broad Acquisition K25:

`{5,6,7,11,12,16,17,18,19,20,21,23,27,28,29,31,32,35,39,40,43,45,46,48,50}`

Actual winner intersection:

`{16,35}` = **2/5**.

Random K25 expectation is 2.5 winners, so this is below matched-exposure expectation and is a candidate-acquisition failure.

Original nine-line slate best overlap:

- `5,8,16,19,30 | PB10` -> `{16}` = 1/5;
- `19,30,38,43,48 | PB5` -> `{38}` = 1/5;
- all other original lines = 0/5.

Best original line quality: **1/5**.

## 4. Richardson late challenger scoring

The late challenger was frozen separately and did not alter the original forecast.

### Frozen standalone E0016 structural-base Richardson ranking

Reproducing the frozen h=5, kappa=8 formula from the pre-draw working state gives actual-winner Richardson global ranks:

- 3 -> rank **14**;
- 4 -> rank **16**;
- 16 -> rank **50**;
- 35 -> rank **31**;
- 38 -> rank **36**.

Mean winner rank: **29.4**.

Frozen Richardson-only diagnostics therefore score:

- K13: **0/5**;
- K20: **2/5** (`3,4`);
- K13 3+/5: no;
- catastrophic exclusion: yes.

This target is a clear negative prospective-style observation for Richardson. Formal E0016 league credit remains provenance-qualified until the 2026-08-25 working state is canonicalized under repository rules.

### Actual pair-message compatibility

For the realized line, nine of ten Richardson pair residuals were negative versus the exact pair-separation null. Only the full S1-S5 span had positive residual support.

Approximate residual likelihood ratios `exp(C_ab)` for realized separations:

- S1-S2: 0.483;
- S1-S3: 0.509;
- S1-S4: 0.659;
- **S1-S5: 1.983**;
- S2-S3: 0.460;
- S2-S4: 0.496;
- S2-S5: 0.431;
- S3-S4: 0.446;
- S3-S5: 0.458;
- S4-S5: 0.656.

Thus Richardson was harmful for most of the realized pair geometry on this target, with only the full-span relation helpful.

Do **not** use this one result to select a long-span-only Richardson derivative retrospectively. Any pair-family ablation must be separately preregistered before a future target.

## 5. Late revised slate performance

Frozen revised lines scored as follows:

- `7,19,29,39,48 | PB5` -> 0/5;
- `7,21,29,39,50 | PB5` -> 0/5;
- `7,18,29,39,50 | PB10` -> 0/5;
- `7,19,28,39,48 | PB10` -> 0/5;
- `5,19,29,38,49 | PB5` -> `{38}` = 1/5;
- `6,20,30,40,50 | PB2` -> 0/5;
- `11,17,27,37,47 | PB10` -> 0/5;
- `12,21,31,41,50 | PB6` -> 0/5;
- `5,22,24,42,47 | PB16` -> 0/5;
- `4,17,27,38,50 | PB12` -> `{4,38}` = **2/5**;
- extra `7,21,29,38,49 | PB16` -> `{38}` = 1/5;
- extra `5,19,28,39,50 | PB6` -> 0/5.

Best upgraded line quality: **2/5**, an improvement over the original best 1/5, but still a poor end-to-end result.

The upgraded 12-line union exposed 28 unique coordinates and captured only `{4,38}` = 2/5. Broad original K25 plus upgraded-line union exposed 35 unique coordinates and contained `{4,16,35,38}` = 4/5; this receives no positive edge claim because exposure is very large and the only omitted winner was3.

## 6. Winner-by-winner Physics of Failure

### Winner 3

- Actual slot: S1, `4 -> 3`, LOW, VVD1.
- Primary HHHHH routing assigned insufficient LOW mass.
- Absent from original K25 and all submitted/revised slates.
- Frozen standalone Richardson rank14, narrowly outside K13 but inside K20.
- Classification: **candidate-acquisition failure; HLR branch collapse harmful; Richardson mildly helpful in rank but insufficient for K13.**

### Winner 4

- Actual slot: S2, `7 -> 4`, LOW, VVD3.
- Coordinate4 was the previous S1 coordinate and reappeared in the draw as S2: a clean coordinate-mobility event.
- It survived only through the frozen direction-dissent slate and paired with38 there.
- Frozen standalone Richardson rank16: outside K13, inside K20.
- Classification: **mobility/dissent helpful; primary HHHHH branch harmful; Richardson mildly helpful but insufficient for K13.**

### Winner 16

- Actual slot: S3, `15 -> 16`, HIGH, VVD1.
- The earlier frozen S3 algebraic grammar explicitly generated `d1 -> 16`, but16 was not elevated into the slot primary slate; it did survive the original broad K25.
- Frozen standalone Richardson rank50.
- Classification: **acquisition success in broad incumbent field, compression/assembly failure; Richardson strongly harmful.**

### Winner 35

- Actual slot: S4, `18 -> 35`, HIGH, VVD17.
- 35 was a frozen S4 alternative and present in original broad K25, but disappeared from final/revised lines.
- Frozen standalone Richardson rank31.
- Classification: **acquisition success in incumbent broad field, downstream preservation failure; Richardson harmful.**

### Winner 38

- Actual slot: S5, `29 -> 38`, HIGH, VVD9.
- 38 was absent from original K25 but appeared in the late Richardson/residual slates, principally from S4 support and global coordinate mobility.
- It occurred on the best revised line together with4.
- Frozen standalone Richardson global rank36, so the pure standalone field itself did not protect it at K20.
- Classification: **late residual/mobility integration helpful at portfolio level; pure Richardson global field not sufficient.**

## 7. Core architecture failure discovered

The largest methodological error in the late upgraded run was **premature collapse of the full HLR distribution into the primary `HHHHH` branch before Richardson refinement**.

The repository architecture requires:

`full HLR probability distributions -> full VVD distributions -> base slot marginals -> Richardson messages -> global field`.

The late working-state challenger instead gave excessive authority to the point `HHHHH` scenario. Because S1 LOW still had about27.6% structural probability and S2 LOW about10.3%, their branches should have retained explicit probability mass. The realized joint `LLHHH` event had about3.47% exact structural probability and should not have been effectively eliminated.

Required correction for future XTRA targets:

- build a **mixture over HLR states**, not one primary HLR state;
- propagate each HLR/VVD scenario into legal slot marginals;
- aggregate scenario-weighted base marginals before Richardson;
- only then apply Richardson residual pair messages and fixed-K compression;
- preserve a bounded direction-dissent/rescue surface at identical total exposure.

This is an implementation correction to the already-approved distribution-first doctrine, not retrospective evidence for a new predictive strategy.

## 8. PowerBall audit

Actual PB: **15**.

All frozen exact PB primaries/challengers missed:

- old incumbent PB10: miss;
- E0015 working leader PB5: miss;
- director PB16 repeat: miss;
- director PB6 LOW/VVD10: miss.

E0015 assigned PB15 probability approximately **0.03604647**, rank **11/16**.

Single-target multiclass scoring:

- E0015 log loss: **3.32295**;
- uniform log loss: **2.77259**;
- delta E0015-uniform: **+0.55036** (worse);
- E0015 Brier: **1.01565**;
- uniform Brier: **0.93750**;
- delta: **+0.07815** (worse).

PB direction LOW was correct, but exact magnitude was VVD1, not the protected VVD10/11/14 branches. This is a clean E0015 prospective-style failure and must remain in its cumulative record.

## 9. Terminal-digit sum hypothesis

Actual terminal digits:

`3,4,6,5,8`

Sum = **26**.

The director's proposed terminal-digit-sum32 morphology hypothesis therefore missed. No retrospective line construction receives credit.

## 10. Evidence verdict

- Original main-number candidate acquisition: `FAIL` on this target (K25 2/5).
- Late upgraded slate: `FAIL`, though best line improved 1/5 ->2/5.
- `XTRA_RICHARDSON_PAIR_DISPERSION`: negative target observation; retain `PROVISIONAL_SIGNAL / shadow` pending cumulative prospective evidence, no promotion.
- HHHHH point-scenario routing before Richardson: **falsified as an acceptable implementation of distribution-first routing**; restore full HLR mixture.
- Coordinate mobility/dissent preservation: useful diagnostic on winner4 and portfolio capture of38; still `INSUFFICIENT_EVIDENCE` as predictive edge.
- E0015 PB convergence: negative target observation; retain `PROVISIONAL_SIGNAL` only until cumulative prospective record justifies reclassification.
- PB16 repeat director shadow: miss.
- PB6 LOW/VVD10 director shadow: miss.
- terminal-digit sum32: miss / diagnostic only.

## 11. Next research priority

The next XTRA target should freeze a **true full-distribution Richardson integration**:

`HLR mixture -> VVD mixture -> slot marginals -> Richardson residual messages -> global inclusion field -> fixed-K Core/Rescue -> assembly`.

Primary KPI remains 5/5 initial main-coordinate acquisition at fixed exposure. Do not retune Richardson h=5, kappa=8, or the 50/50 shadow blend from this result.
