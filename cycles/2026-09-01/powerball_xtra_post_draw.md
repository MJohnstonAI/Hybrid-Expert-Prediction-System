# PowerBall XTRA Post-Draw Audit — 2026-09-01

**Result supplied by project director:** `4,18,31,34,40 | PB10`  
**Status:** post-draw audit; result not silently canonicalized while official-source provenance gate remains unresolved.  
**Frozen forecast source:** `cycles/2026-09-01/powerball_xtra_pre_draw.md`  
**E0018 field:** `cycles/2026-09-01/xtra_e0018_pre_draw_field.json`  
**Terminal shadow:** `cycles/2026-09-01/xtra_terminal_motif_shadow.md`

## 1. Realized state

Previous working draw: `3,4,16,35,38 | PB15`.

Actual main HLR:

`H,H,H,L,H` = **HHHLH**

Actual main VVD by sorted slot:

- S1: `3 -> 4`, VVD1
- S2: `4 -> 18`, VVD14
- S3: `16 -> 31`, VVD15
- S4: `35 -> 34`, VVD1
- S5: `38 -> 40`, VVD2

PowerBall:

- `15 -> 10` = **LOW**
- PB VVD = 5

Actual terminal vector:

`S1=4, S2=8, S3=1, S4=4, S5=0, PB=0`

## 2. HLR audit

Frozen E0018 joint hierarchy:

1. HHHHH ~28.17%
2. **HHHLH ~12.65%**
3. HHHLL ~10.51%
4. HHLLL ~4.83%

The realized HHHLH was therefore represented as the second-ranked joint regime.

However, exact enumeration over all `C(50,5)=2,118,760` legal next draws relative to `3,4,16,35,38` gives:

`P0(HHHLH) = 307,224 / 2,118,760 = 14.5002%`.

Thus E0018 assigned less probability to the realized joint state than the exact exchangeable structural null:

- model: 12.6531%
- exact structural null: 14.5002%
- model/null ratio: ~0.873

The exact structural per-slot modal directions are also `H,H,H,L,H`.

**Verdict:** directional realization is diagnostically correct but earns **no incremental predictive-credit claim** on this target. Structural geometry already preferred the same vector, and E0018 underweighted the realized joint state.

The Director hedge `HHLLL | H` did not realize. Main was HHHLH and PB was LOW.

## 3. E0018 candidate-acquisition audit

Actual winners: `{4,18,31,34,40}`.

### K13

- Full-mixture K13: `[3,1,2,4,5,7,8,6,9,10,15,14,13]` -> **1/5** (`4`)
- Richardson K13: `[1,2,3,4,7,8,5,9,6,10,11,12,14]` -> **1/5** (`4`)
- 50/50 blend K13: same winner capture -> **1/5** (`4`)

Exact random K13 expectation is **1.3 winner coordinates/target**. All three K13 fields are below expectation on this first E0018 target.

### K20

- Full-mixture K20 -> **2/5** (`4,34`)
- Richardson K20 -> **1/5** (`4`)
- 50/50 blend K20 -> **1/5** (`4`)

Exact random K20 expectation is **2.0**. Full-mixture K20 equals expectation; Richardson/blend are below expectation.

**Key attribution:** Richardson removed useful upper-register exposure at K20 on this target. It did not improve candidate acquisition.

No promotion or retuning is justified from one target. E0018 remains `INSUFFICIENT_EVIDENCE`; Richardson remains shadow/provisional only.

## 4. Final 10-line portfolio score

Frozen line overlaps with `{4,18,31,34,40}`:

1. `4,11,23,37,50 | PB12` -> **1/5** (`4`)
2. `5,10,24,38,49 | PB12` -> **0/5**
3. `6,12,22,40,48 | PB5` -> **1/5** (`40`)
4. `4,10,23,34,50 | PB12` -> **2/5** (`4,34`)
5. `5,12,24,33,49 | PB14` -> **0/5**
6. `4,11,23,34,37 | PB5` -> **2/5** (`4,34`)
7. `6,10,24,33,36 | PB4` -> **0/5**
8. `4,11,15,34,37 | PB16` -> **2/5** (`4,34`)
9. `5,10,14,33,36 | PB16` -> **0/5**
10. `1,11,23,37,50 | PB15` -> **0/5**

Best submitted overlap: **2/5** on lines 4, 6 and 8.

The 10-line union contains 21 distinct main coordinates and captures **3/5** winners: `{4,34,40}`. A random K21 has expected recall 2.1 and probability ~34.6% of capturing at least 3/5, so union capture is not evidence of predictive lift.

Notably, line 4 was explicitly allocated to the actual **HHHLH** regime and achieved 2/5. This shows that regime preservation worked operationally, but exact-coordinate acquisition/assembly remained the bottleneck.

## 5. Winner-by-winner attribution

### 4
Captured broadly. Present in every E0018 K13 field and several submitted lines. **Acquisition success.**

### 18
Absent from all K13/K20 research baskets and all final lines. S2 made a large `4 -> 18` HIGH move, VVD14. **Primary acquisition failure.**

### 31
Absent from K13/K20 baskets and final lines. S3 made a large `16 -> 31` HIGH move, VVD15. The terminal shadow correctly predicted S3 residue `1`, and HLR HIGH retained `{21,31,41}`, but sparse VVD resolution selected 21 rather than 31. **Terminal-residue success; VVD exact-resolution failure.**

### 34
Captured by full-mixture K20 and several assembled lines, including actual-regime line 4. Richardson/blend K20 omitted it. **Base-field/preservation success; Richardson harmful at fixed K20.**

### 40
Absent from research K13/K20 fields, but appears in final line 3 as a global coordinate. **Assembly-level rescue only; slot-specific acquisition weak.**

## 6. Terminal-motif shadow audit

Frozen primary terminal vector:

`1,2,1,8,9 | PB2`

Actual:

`4,8,1,4,0 | PB0`

Terminal-digit score:

- S1: miss
- S2: miss
- **S3: hit** (`1`)
- S4: miss
- S5: miss
- PB: miss

Main terminal Top1 = **1/5**; all six fields = **1/6**.

Exact-coordinate shadows `11,12,21,28,39 | PB12` scored **0 exact hits**.

The important nested result is S3:

- motif-only predicted terminal `1`: **correct**;
- motif + HLR HIGH produced `{21,31,41}`: **actual 31 survived**;
- VVD-based exact resolution selected `21`: **wrong**.

Therefore on this target the terminal motif plus HLR preserved the winner, while the sparse VVD resolver degraded it. This is exactly why future terminal-motif work must score nested M1/M2/M3 layers rather than only the final exact coordinate.

No new algebraic rule is added post-draw.

## 7. PowerBall E0015 audit

Actual PB = **10**.

Frozen E0015 convergence field ranked PB10 **10th of 16** with probability ~0.0373179.

Scores:

- E0015 log loss: **3.2883**
- uniform log loss: **2.7726**
- delta: **+0.5157** (worse)
- E0015 multiclass Brier: **1.04274**
- uniform Brier: **0.93750**
- delta: **+0.10524** (worse)

PB direction LOW was correct, but from current PB15 the exact uniform structural probability of LOW is `14/16 = 87.5%`; E0015 assigned only 53.125% to LOW. Therefore the direction hit does not establish model lift.

The exact-ball miss exposes the brittleness of the single historical `VVD1 -> VVD3` continuation that heavily favored PB12. Actual next VVD was 5.

**Verdict:** clean negative E0015 working-state target observation. No post-draw retuning.

## 8. Physics of Failure / architecture verdict

1. **Distribution-first repair succeeded operationally:** the actual HHHLH regime was not hard-pruned and was represented in the submitted portfolio.
2. **Acquisition still failed:** E0018 K13 captured only 1/5; full-mixture K20 only 2/5.
3. **Richardson was harmful at K20 on this target:** 1/5 versus base 2/5.
4. **Assembly could not recover omitted 18 and 31**, despite representing the correct HLR regime.
5. **Terminal symbolic dynamics produced one genuine pre-draw residue hit (S3)**, and the nested audit shows HLR helped preserve the exact winner while sparse VVD over-resolution removed it.
6. **PB conditional convergence failed exact-ball scoring and underperformed uniform proper-score controls.**

## 9. Evidence status after target

- E0018 full-mixture architecture: retain as **INSUFFICIENT_EVIDENCE / prospective shadow**; architecture repair is methodologically valid, predictive lift not shown.
- E0016 Richardson XTRA: retain shadow/provisional only; this target is negative at fixed K.
- E0015 PB convergence: retain provisional shadow with another negative proper-score observation; no promotion.
- Terminal motif constraint solver: **INSUFFICIENT_EVIDENCE**, but retain as a new prospective shadow because the S3 nested result is informative and genuinely pre-draw.
- Director `HHLLL | H`: target miss; no retrospective adjustment.

Paper trading/research only.