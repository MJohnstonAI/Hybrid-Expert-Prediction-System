# E0016 — Physics-Derived Shadow Integration and XTRA Richardson Dispersion

**Experiment ID:** `E0016`  
**Status:** director-approved shadow integration  
**Evidence classification:** component-specific; see `decision.md`  
**Mode:** `paper_trading_only`

## Purpose

Preserve only the physics-derived operators that survived the post-June-2026 taste test strongly enough to justify cheap prospective shadow evaluation, while explicitly excluding the operators that added complexity without useful lift.

The experiment implements three distinct roles:

1. `MAIN_NONEQUILIBRIUM_CURRENT` — Main candidate-funnel shadow score measuring directed residual transition current.
2. `MAIN_LEVY_TAIL_DIAGNOSTIC` — Main tail-risk diagnostic measuring whether a heavy-tailed displacement alternative deserves attention relative to `NULL_VVD_STRUCTURAL`; it has no candidate authority.
3. `XTRA_RICHARDSON_PAIR_DISPERSION` — XTRA candidate-funnel shadow expert modelling expansion/contraction of pair separations and translating residual pair compatibility back into XTRA slot/global candidate marginals.

## Hard data boundary

The physics shadow programme is **post-June-2026 only**.

- Main uses `data/draw_history.jsonl` from 2026-06-02 onward.
- XTRA uses `data/powerball_xtra_history.jsonl` from 2026-06-02 onward.
- No 2018-2025 PRNG-era workbook state, weights, gaps, transitions, fitted parameters, or validation results may enter these experts.
- Main and XTRA fitted state remain independent.

This boundary is director-mandated for the physics programme because the active research target is the post-June-2026 mechanical-drum regime.

## Why these three survived

A post-June-only walk-forward taste test compared physics-derived challengers at matched candidate exposure.

### Main nonequilibrium current

The residual-current blend improved K13 coordinate capture in the exploratory current-era replay and improved the two final replay holdouts from one to two captured winner coordinates at K13. Absolute evidence remained underpowered, so the expert is admitted only as a shadow score.

### Main Lévy tail diagnostic

The heavy-tail model strongly described the 2026-08-21 Main tail draw but did not show stable enough full-window lift to justify routine candidate scoring. It is retained only as a diagnostic because it may identify when HEPS is under-allocating probability to legal extreme displacements without letting one memorable tail draw inflate authority.

### XTRA Richardson dispersion

The XTRA-only pair-dispersion replay improved candidate rank and K13/K20 winner capture relative to the simple baseline over the active XTRA window and improved combined K13 capture on the two final canonical replay holdouts. The absolute sample remains small, so Richardson is admitted as a prospective shadow expert rather than a production selector.

## Rejected physics additions

The following are not integrated into routine HEPS execution from this championship:

- general drift/diffusion tensor;
- optimal-transport main-number flow;
- nucleation augmentation of E0013;
- ordinary heat-kernel/diffusion augmentation of E0013;
- Lévy as a normal Main candidate ranker;
- physics-derived XTRA PowerBall models from this family.

Rejected operators may be revisited only through a materially new preregistered experiment; do not silently reintroduce them under new terminology.

## Falsifiable hypotheses

### H1 — Main current

At fixed candidate exposure, `MAIN_NONEQUILIBRIUM_CURRENT` adds prospective coordinate-ranking information beyond simple recency/frequency and the incumbent Main candidate field.

### H2 — Main Lévy diagnostic

A preregistered heavy-tail displacement family identifies excess tail pressure relative to `NULL_VVD_STRUCTURAL` often enough to improve calibration or justify a separately tested fixed-K rescue rule. Until that is shown, it remains diagnostic only.

### H3 — XTRA Richardson

At fixed XTRA candidate exposure, residual pair-separation dynamics improve prospective coordinate rank and K13/K20 winner survival beyond simple recency/frequency and the incumbent XTRA candidate field.

## Authority principle

No component in E0016 may hard-eliminate candidates. Main Lévy has no candidate-scoring authority. XTRA Richardson and Main current may produce shadow scores and frozen counterfactual K13/K20 baskets only. Production influence requires a later promotion decision based on prospective evidence.