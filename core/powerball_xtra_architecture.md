# HEPS PowerBall XTRA Architecture

## Status

Operational target-specific HEPS lane authorized for South African **PowerBall XTRA** research and paper trading.

This lane reuses the **architecture shape and scientific governance** of the Main PowerBall system but maintains completely independent data, state, fitted parameters, expert outputs, candidate baskets, rankings, and PowerBall forecasts.

## Hard isolation boundary

- Active XTRA history starts at **2026-06-02**.
- Canonical ledger: `data/powerball_xtra_history.jsonl`.
- Manifest: `data/powerball_xtra_manifest.json`.
- Schema: `data/powerball_xtra_schema.json`.
- No pre-June 2026 PowerBall Plus/XTRA history enters active XTRA state.
- No Main PowerBall learned state or fitted parameter may be copied into XTRA.
- Main and XTRA may share code/formulas only where the formula itself is target-agnostic.
- Every XTRA expert must be fitted/evaluated using XTRA observations only.

## Matrix X-A — XTRA Main Numbers

The five sorted XTRA main-number slots use the same staged HEPS decomposition:

```text
XTRA Data
  -> XTRA Slot Forecast
  -> XTRA Candidate Funnel
  -> XTRA Coalition Assembly
  -> XTRA Combination Morphology
  -> XTRA Winner-Float Ranking
  -> XTRA Portfolio Optimization
```

### Stage 1 — Slot Forecast

`XTRA_HLR_SLOT` forecasts `LOW | REPEAT | HIGH` independently for Slot1-Slot5 using only the XTRA ledger.

Sorted slots are order statistics, not physical draw order. Direction forecasts are soft evidence unless separately promoted.

### Stage 2 — Candidate Funnel

XTRA-local counterparts may evaluate:

- stiction / exact repeat / +/-1 or +/-2 support;
- void/canyon support;
- sorted-slot density;
- harmonic/boundary exposure;
- GPR-8-style residual features;
- VVD movement conditioned on the XTRA HLR forecast.

All scores and sufficient statistics are XTRA-local.

### Stage 3 — Coalition Assembly

Pair, pair-of-pairs, anchor, graph, and related interaction models may be reused algorithmically, but they must be trained and scored from XTRA observations only.

### Stage 4 — Combination Morphology

Sum, spread, gaps, parity/register, terminal digits, SLDV, and related morphology are computed from XTRA combinations only. Structural commonness must not be confused with higher exact-line probability.

### Stage 5 — Winner-Float Ranking

Rank surviving XTRA combinations using frozen XTRA-only expert outputs. Evaluate exact winning-line rank and Top-K survival against random/simple baselines.

### Stage 6 — Portfolio Optimization

Compress ranked XTRA combinations into the final paper-trading slate while preserving exposure and diversity. Keep a chaos/random control lane.

## Matrix X-B — XTRA PowerBall 1-16

The XTRA PowerBall is a separate 1-16 model from both:

1. XTRA main numbers; and
2. Main PowerBall's 1-16 model.

It may use XTRA-local direction, VVD, stiction/shadow, gap/recency, fulcrum, and hedge diagnostics. No Main PowerBall transition history or exact-ball ranking is imported.

## State namespace

Every mutable or fitted item must use an `XTRA_` namespace or live in an XTRA-specific artifact. Examples:

- `XTRA_HLR_SLOT`
- `XTRA_VVD_DELTA`
- `XTRA_STICTION_SHADOW`
- `XTRA_VOID_BRIDGE`
- `XTRA_SORTED_SLOT_DENSITY`
- `XTRA_GPR8`
- `XTRA_COALITION_PAIR_OF_PAIRS_ANCHOR`
- `XTRA_MORPH_SLDV`
- `XTRA_RANK_WINNER_FLOAT`
- `XTRA_PORTFOLIO_CHAOS_BASELINE`
- `XTRA_PB_ACTIVE_MATRIX`

## Per-draw XTRA cycle

For every target draw, freeze separately from Main:

1. XTRA ledger state;
2. XTRA architecture/expert versions;
3. XTRA slot forecast;
4. XTRA candidate basket;
5. XTRA coalition/morphology/ranking outputs;
6. XTRA PowerBall forecast;
7. final XTRA paper-trading slate.

Post-draw, score only against the XTRA result and run XTRA-specific Physics of Failure.

## Evidence doctrine

The XTRA sample is short. All pattern claims remain subject to matched null controls, walk-forward testing, and exposure denominators. Reusing an algorithm from Main does not transfer its evidence status to XTRA.

## Data-update doctrine

Read the canonical local XTRA ledger first. Do not rescan historical web sources. For each new draw, use the single source configured in `data/powerball_xtra_manifest.json` to obtain only the newest missing XTRA result, validate date/range/order, append it, then update the manifest.

All outputs remain `paper_trading_only`.
