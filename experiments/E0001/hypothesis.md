# E0001 — Structural Null and Gap-Space Residual Audit

**Experiment ID:** `E0001`  
**Title:** Exact Structural Null Championship and Gap-Space Residual Audit  
**Originating contributors:** Claude Sonnet red-team review; Gemini gap-space proposal; ChatGPT synthesis/reproduction  
**Self-selected role:** meta-research auditor / state-space modeller  
**Target stages:** methodology, slot_forecast, candidate_funnel  
**Architecture status:** experimental

## 1. Primary question

Do `MAIN_HLR_SLOT` and `MAIN_VVD_DELTA` contain predictive information beyond the exact order-statistic geometry of independent uniform 5/50 draws?

## 2. Secondary question

Does the corrected six-component `MAIN_GAP_VECTOR` provide a cleaner state representation in which any temporal residual can be shown to outperform the exact `NULL_GAP_DM` baseline prospectively?

## 3. Why this matters

HEPS previously treated encouraging HLR-vector ranks as possible evidence of useful flow structure. Claude's corrected red-team review showed that strong LOW/HIGH probabilities arise automatically from sorted order-statistic geometry. Independent exact enumeration further showed that several high-ranked Candidate Lattice rescue vectors are also among the highest-probability vectors under the IID structural null.

If HLR/VVD cannot beat these exact free baselines with proper prospective probability scores, further architecture built on them risks amplifying noise and post-hoc degrees of freedom.

## 4. Falsifiable hypotheses

### H1 — HLR incremental information

A frozen learned HLR probability model will achieve lower prospective draw-level multiclass Brier score than `NULL_HLR_STRUCTURAL` across a preregistered sequence of future targets.

### H2 — VVD incremental information

A frozen learned VVD displacement distribution will achieve lower prospective negative log likelihood than `NULL_VVD_STRUCTURAL`.

### H3 — Joint-flow incremental information

The learned 243-vector flow ranker will assign systematically greater probability/rank to realized future vectors than `NULL_HLR_JOINT_243`, after accounting for its additional fitting freedom.

### H4 — Gap-space residual information

A preregistered low-complexity model of future `MAIN_GAP_VECTOR` or `MAIN_GAP_RESIDUAL` will outperform `NULL_GAP_DM` prospectively under a proper scoring rule.

### H5 — Candidate compression lift

Any candidate basket/meta-lattice derived from learned state will preserve realized future winners more often than the exact probability mass/exposure retained by its matched null.

## 5. Exact structural facts used as baselines

For sorted slot `j` and coordinate `n`:

`P0(X_(j)=n) = C(n-1,j-1) * C(50-n,5-j) / C(50,5)`.

Given previous coordinate `p`, obtain exact `LOW`, `REPEAT`, `HIGH` probabilities by summing below, at, and above `p`.

For VVD displacement `d`, sum the exact slot probability at legal `p-d` and `p+d`, counting `d=0` once.

For the full five-slot HLR vector, enumerate all `C(50,5)=2,118,760` legal next draws because sorted slots are dependent.

For sorted line `S1<S2<S3<S4<S5`, use the corrected gap vector:

`G = (S1-1, S2-S1-1, S3-S2-1, S4-S3-1, S5-S4-1, 50-S5)`.

Every legal `G` is a weak composition of 45 into six nonnegative parts. Under the IID 5/50 null:

`G ~ DirichletMultinomial(45, [1,1,1,1,1,1])`,

which is exactly uniform over the `C(50,5)` legal gap compositions.

## 6. Relationship to existing research

- `CANDIDATE_LATTICE_V01` remains `INSUFFICIENT_EVIDENCE` and its 2026-08-07 slate is immutable.
- Q001 and Q002 are refined by requiring exact structural-null comparators.
- This experiment does not promote `MAIN_GAP_VECTOR` or `MAIN_GAP_RESIDUAL` as predictive experts.
- Meta-basket, safe-exclusion, and portfolio-coverage research should remain downstream until this audit establishes whether learned slot dynamics add information beyond geometry.

## 7. Falsification summary

If learned HLR/VVD/gap models fail to outperform their exact structural nulls across the preregistered prospective window, downgrade or retire their predictive authority and retain only deterministic structural constraints and null diagnostics.

## 8. Evidence classification at creation

`INSUFFICIENT_EVIDENCE`
