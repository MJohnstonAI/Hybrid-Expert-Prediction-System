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

For the physics-derived candidate shadow introduced on 2026-08-28, also read:

- `core/xtra_richardson_pair_dispersion.md`;
- `experiments/E0016/`;
- `knowledge/PHYSICS_SHADOW_INTEGRATION_HANDOFF_2026-08-28.md`.

For the post-2026-08-28 acquisition correction, also read:

- `experiments/E0018/`;
- `experiments/E0011/xtra_power_budget.md`;
- `experiments/E0011/xtra_redundancy_protocol.md`;
- `scripts/xtra_full_mixture_base.py`;
- `scripts/xtra_e0018_pipeline.py`.

## Exchangeability and acquisition doctrine

Under the exact exchangeable IID 5/50 null, every target-blind fixed K basket has the same winner-overlap distribution:

`H ~ Hypergeometric(N=50, K, n=5)` and `E[H]=5K/50`.

Therefore candidate-basket composition can improve expected recall only if HEPS identifies reproducible non-exchangeable residual information. Mathematical novelty alone is not a reason to expect lift.

Binding consequences:

- all acquisition comparisons use identical K;
- enlarged unions are exposure, not lift;
- K13 remains the primary acquisition research frontier and K20 a diagnostic frontier;
- a 20-target review is an early calibration/futility checkpoint, not a proof threshold;
- the default K13 minimum effect of interest is +0.20 winner coordinates/target, with an approximate 137-target planning horizon at one-sided alpha 0.05 and 80% power under the simple independence approximation;
- new acquisition families must declare K, minimum effect, testing-family exposure and power horizon before confirmatory use.

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

`XTRA_HLR_SLOT` forecasts `LOW | REPEAT | HIGH` for Slot1-Slot5 using only the XTRA ledger.

Sorted slots are order statistics, not physical draw order. Direction forecasts are probability fields, not hard scenario gates.

#### Full-support HLR mixture — binding E0018 rule

For targets from 2026-09-01 onward, the E0018 shadow must preserve the complete legal HLR mixture before Richardson or exact-coordinate compression:

1. derive the current slotwise HLR state from the latest two XTRA draws;
2. estimate per-slot successor HLR probabilities conditioned on the current slot state;
3. shrink each successor distribution toward the exact 5/50 order-statistic HLR mass at the current coordinate;
4. enumerate every legal `C(50,5)=2,118,760` sorted combination;
5. reweight legal combinations by a conservative geometric pool of HLR residual likelihood ratios;
6. require strictly positive mass for every legal combination;
7. marginalize the full legal space back to per-slot and global coordinate fields.

Canonical implementation: `scripts/xtra_full_mixture_base.py` with frozen E0018 `tau=6`.

A modal HLR vector may be reported for interpretation but may **not** eliminate alternative branches before candidate acquisition. The 2026-08-28 use of a preferred `HHHHH`-conditioned Richardson base is explicitly superseded by this rule.

### Stage 2 — Candidate Funnel

XTRA-local counterparts may evaluate:

- stiction / exact repeat / +/-1 or +/-2 support;
- void/canyon support;
- sorted-slot density;
- harmonic/boundary exposure;
- GPR-8-style residual features;
- VVD movement conditioned on the full XTRA HLR distribution;
- `XTRA_RICHARDSON_PAIR_DISPERSION` as a post-June-only shadow refinement of pair-separation probability structure.

All scores and sufficient statistics are XTRA-local.

#### Richardson distribution-first integration

`XTRA_RICHARDSON_PAIR_DISPERSION` does **not** predict a hard gap vector and does not prune exact coordinates from one preferred expansion/contraction scenario.

It operates as follows:

1. represent all ten sorted-slot pair separations `R_ab=S_b-S_a`;
2. estimate the next separation distribution from prior XTRA transitions only;
3. shrink that estimate toward the exact IID 5/50 pair-separation distribution;
4. convert only residual information beyond exact geometry into pair-compatibility messages;
5. propagate those messages into the full-support XTRA slot-marginal probability field;
6. preserve exact-slot and global-anywhere coordinate probabilities separately;
7. generate Richardson-only and incumbent/Richardson blended **shadow** K13/K20 baskets at identical exposure.

The canonical frozen v1 formula is in `core/xtra_richardson_pair_dispersion.md`. E0018 freezes `h=5`, `kappa=8`, and a 50/50 base/Richardson diagnostic blend for its prospective comparison.

Richardson currently has zero production weight. It may not alter the authoritative XTRA candidate universe until a later promotion decision.

#### Candidate-preservation rule

Acquisition is scored before assembly. If Core/Reserve/Rescue lanes are shown, confirmatory comparisons must keep total K fixed. A `Core13` may be compared with `Core12+Rescue1` or `Core11+Rescue2`; the union may not be credited as K13 performance.

### Stage 3 — Coalition Assembly

Pair, pair-of-pairs, anchor, graph, and related interaction models may be reused algorithmically, but they must be trained and scored from XTRA observations only.

Richardson pair-separation compatibility is a candidate-funnel probability refinement. Do not count the same Richardson pair information again as an independent coalition vote unless a future residualization experiment demonstrates incremental coalition information.

### Spectral acquisition moratorium

Ordinary historical co-occurrence graph -> spectral transform -> global candidate ranking is under research moratorium after the negative/insufficient acquisition record across E0012, E0014 and E0017, with E0013 retaining coalition authority only.

Reopening spectral **candidate acquisition** requires materially new information or an exogenous covariate plus a preregistered matched-K protocol. Renaming a Laplacian/centrality transform does not constitute a new family.

### Stage 4 — Combination Morphology

Sum, spread, gaps, parity/register, terminal digits, SLDV, and related morphology are computed from XTRA combinations only. Structural commonness must not be confused with higher exact-line probability.

Morphology may rank or diversify assembled lines but may not hard-delete candidate coordinates before candidate-acquisition scoring in E0018.

### Stage 5 — Winner-Float Ranking

Rank surviving XTRA combinations using frozen XTRA-only expert outputs. Evaluate exact winning-line rank and Top-K survival against random/simple baselines.

### Stage 6 — Portfolio Optimization

Compress ranked XTRA combinations into the final paper-trading slate while preserving exposure and diversity. Keep a chaos/random control lane.

## Expert redundancy and convergence

Agreement is an incremental-information question, not a vote count.

Until `experiments/E0011/xtra_redundancy_protocol.md` has sufficient genuinely frozen field coverage:

- HLR/VVD/order-statistic/recency-derived experts are conservatively treated as potentially redundant;
- unknown redundancy reduces confidence;
- no expert-vote multiplier is permitted in the E0018 target pipeline;
- missing historical expert fields remain missing and are never reconstructed after the result.

Use `scripts/xtra_expert_redundancy.py` for the frozen-field audit.

## Machine provenance

`machine_name` is retained in the XTRA schema and should be backfilled only from verifiable source records. `unknown` is a valid state and is preferable to inference.

Machine identity is diagnostic-only unless the machine assignment/state is demonstrably available **before** the target draw. If machine identity is only learned after the draw, it may be used for heterogeneity, stationarity and pooled-model falsification but not to condition the same target prediction.

No ball-set, maintenance, chamber or environmental state may be invented from a machine label.

## Matrix X-B — XTRA PowerBall 1-16

The XTRA PowerBall is a separate 1-16 model from both:

1. XTRA main numbers; and
2. Main PowerBall's 1-16 model.

It may use XTRA-local direction, VVD, stiction/shadow, gap/recency, fulcrum, conditional transition/convergence, and hedge diagnostics. No Main PowerBall transition history or exact-ball ranking is imported.

E0015 conditional PB convergence remains the principal prospective shadow. It must publish the full 1..16 probability field and be scored by actual-ball rank, log loss and Brier score. Director hypotheses may be frozen separately but are not merged into E0015 after the fact.

The E0016 physics championship did not justify adding Richardson, Lévy, drift/diffusion, or optimal-transport authority to the XTRA PowerBall field. Keep the PowerBall research lane separate from Richardson main-number evidence.

## State namespace

Every mutable or fitted item must use an `XTRA_` namespace or live in an XTRA-specific artifact. Examples:

- `XTRA_HLR_SLOT`
- `XTRA_HLR_FULL_MIXTURE_BASE`
- `XTRA_VVD_DELTA`
- `XTRA_STICTION_SHADOW`
- `XTRA_VOID_BRIDGE`
- `XTRA_SORTED_SLOT_DENSITY`
- `XTRA_GPR8`
- `XTRA_RICHARDSON_PAIR_DISPERSION`
- `XTRA_COALITION_PAIR_OF_PAIRS_ANCHOR`
- `XTRA_MORPH_SLDV`
- `XTRA_RANK_WINNER_FLOAT`
- `XTRA_PORTFOLIO_CHAOS_BASELINE`
- `XTRA_PB_ACTIVE_MATRIX`
- `XTRA_PB_CONDITIONAL_CONVERGENCE_E0015`
- `XTRA_MACHINE_PROVENANCE_DIAGNOSTIC`

## Per-draw XTRA cycle

For every target draw, freeze separately from Main:

1. XTRA canonical ledger state and any explicitly separate working-state extension;
2. provenance status of every noncanonical row used;
3. XTRA architecture/expert versions;
4. full-support HLR/slot probability field;
5. fixed-K base candidate baskets;
6. Richardson pair-separation state, residual field and counterfactual shadow K13/K20 when enabled;
7. XTRA coalition/morphology/ranking outputs;
8. XTRA full PowerBall probability field;
9. machine-provenance/knowability status;
10. final XTRA paper-trading slate.

Post-draw, score only against the XTRA result and run XTRA-specific Physics of Failure.

For Richardson, score base, Richardson and blend baskets separately. Never rewrite the authoritative pre-draw XTRA basket after seeing the result.

## Evidence doctrine

The XTRA sample is short. All pattern claims remain subject to matched null controls, walk-forward testing, exposure denominators, explicit minimum effects and power horizons. Reusing an algorithm from Main does not transfer its evidence status to XTRA.

`XTRA_RICHARDSON_PAIR_DISPERSION` currently carries only `PROVISIONAL_SIGNAL` / `shadow` status. The post-June replay justified prospective attention, not production authority.

E0018 carries `INSUFFICIENT_EVIDENCE` / prospective-shadow status. A single strong target cannot promote it because its acquisition power horizon is long.

## Data-update doctrine

Read the canonical local XTRA ledger first. Do not rescan historical web sources. For each new draw, use the single source configured in `data/powerball_xtra_manifest.json` to obtain only the newest missing XTRA result, validate date/range/order, append it, then update the manifest.

When the newest result is known from the project director but official-source verification is still pending, a target-cycle **working-state extension** may be frozen separately from the canonical ledger. Scripts must disclose that the extension was used. Never silently promote a working row to canonical status.

All outputs remain `paper_trading_only`.
