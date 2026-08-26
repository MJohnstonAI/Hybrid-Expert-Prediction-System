# E0011 — XTRA Joint HLR-Conditioned Magnitude Regimes

**Status:** PROTOCOL / ZERO RETROSPECTIVE CREDIT  
**Mode:** `paper_trading_only`  
**Motivation target:** XTRA 2026-08-25  
**Do not treat the motivating draw as validation.**

## Objective

Test whether XTRA HEPS can improve candidate acquisition by conditioning magnitude and morphology jointly on the prospectively frozen HLR vector before applying residual experts.

The motivating failure had the correct HLR vector `LLLLL|H` but selected main VVD magnitudes `[10,2,13,3,2]` while the actual magnitudes were `[13,16,22,21,19]`. Core and Specialist candidate surfaces each captured only one winner.

## Gate A — Freeze HLR probability field

For S1-S5 and PB, freeze directional probabilities and a primary H/L/R vector before any exact coordinates are selected.

Human/director shadow analysis remains a named independent expert and must be frozen separately.

## Gate B — Exact joint HLR conditional field

For the five main numbers, enumerate or exactly sample the legal 5/50 combination space conditional on the frozen HLR event.

Derive:

1. slot PMFs conditional on the full HLR vector;
2. conditional coordinate means, modes and quantiles;
3. conditional VVD PMFs from the current vector;
4. conditional sum, spread, gap and parity distributions;
5. covariance/dependence between slot movements.

This becomes the structural control field for the target draw.

Independent per-slot structural baselines are not sufficient when the entire vector is constrained jointly.

## Gate C — Magnitude regime mixture

Represent the main draw as a mixture of at least three prospectively defined magnitude regimes:

- **R0 Stiction:** small VVD / near-coordinate movement;
- **R1 Central:** ordinary conditional displacement around the joint HLR structural field;
- **R2 Expansion/Compression:** coordinated large displacement into conditional tail regions.

Regime definitions must be numerical and frozen from historical walk-forward data, not invented after a target.

Each target receives frozen mixture weights `w0,w1,w2` summing to1.

## Gate D — Residual experts inside regimes

Run XTRA VVD transition, lane algebra, Coulomb/stiction, terminal-digit, exact-state, slot-density and GPR8-style experts as **residual modifiers within each regime**.

An expert may alter local probability but may not collapse the whole field to one VVD point unless prospectively promoted by proper-score evidence.

## Gate E — Outcome-space dependency

Measure expert dependence not only by shared source features but by overlap in outcome space:

- sum bands;
- average VVD;
- coordinate quantiles;
- gap morphology.

Experts producing different exact numbers but all occupying the same central regime receive a dependency penalty.

## Gate F — Controlled tail exposure

Reserve a fixed small portfolio budget for structurally legal tail regimes when the frozen HLR vector supports them.

Initial experimental proposal:

- central/regime lines remain majority exposure;
- up to **3 deep-compression/expansion lines** per 20-line slate;
- tail lines drawn from pre-defined conditional 5–15th or 85–95th percentiles depending on HLR direction.

This cap and percentile band must be frozen before prospective testing.

## Gate G — Candidate surfaces

Maintain:

1. Core K13 from the principal joint probability field;
2. Specialist Reserve K<=12 from orthogonal residual experts;
3. Regime Chaos K<=8 from tail-conditioned acquisition.

Do not merge these into an uncontrolled large basket.

Report individual and union exposure/recall.

## Gate H — Assembly

E0010 Triad–Pair Fusion remains available only after candidate acquisition.

If Core+Reserve+Regime surfaces omit the winners, fusion receives no blame. Physics-of-Failure must classify acquisition versus assembly explicitly.

## PowerBall

PB remains a separate 1/16 field.

For tiny exact-state samples, freeze a ranked top-k distribution and score:

- direction;
- VVD magnitude/band;
- exact rank;
- log/Brier where a full PMF is available.

Do not promote a unique exact primary solely because one category leads another by a single historical observation.

## Walk-forward evaluation

Replay all eligible targets using only prior XTRA data.

Compare E0011 against:

- exact structural unconditional field;
- exact HLR-conditioned structural field;
- current beta=0.20 VVD-FCPC field;
- E0010 Core/Reserve architecture;
- matched random candidate surfaces with equal exposure.

Primary metrics:

1. full-field composite log loss and Brier;
2. K13 / Reserve / Regime recall;
3. union recall at explicit exposure size;
4. catastrophe rate 0/1 winners captured;
5. best-line 3+/4+/5 rates;
6. calibration by magnitude regime;
7. incremental gain from tail exposure.

## Promotion rule

No promotion from one or two successful targets.

Require multiple prospective draws, proper-score non-deterioration, and measurable acquisition or line-quality gain versus matched structural/random controls.

## Scientific interpretation

The motivating 2026-08-25 draw showed that HEPS can predict the direction vector correctly while still fail because the displacement regime is wrong.

E0011 tests whether the correct unit of magnitude forecasting is the **joint HLR-conditioned draw regime**, not five independent VVD point forecasts.