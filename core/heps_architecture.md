# HEPS Master Architecture

## Active branch

HEPS v33.4 — Candidate Recall Guard + Directional Scenario Routing

## Purpose

HEPS is a file-based, multi-agent, paper-trading prediction research system for South African PowerBall. It uses a canonical draw ledger, expert-preserving candidate discovery, directional scenario routing, coalition synthesis, red-team reviews, structured prediction/post-game outputs, and matched-null controls.

## Active data doctrine

The active dataset is the post-May/June 2026 South African PowerBall 5/50 + PB 1/16 regime.

Earlier HEPS strategies and algorithms may be used as diagnostic priors, but active parameters must be recalibrated and evaluated on the current regime. Legacy spreadsheets must not silently become active training dependencies.

The 2026-06-22 PowerBall primary electronic-RNG cutover claim is not established. Szrek's deployment announcement described Trusted Draw as primary for Daily Lotto and backup for Lotto/PowerBall. HEPS must therefore treat PowerBall draw mechanism as `mechanical-primary-or-unconfirmed` until direct operator evidence resolves machine usage. Do not zero physical-feature lanes solely from the June 22 date.

## Core storage doctrine

- Canonical draw ledger: `data/draw_history.jsonl`
- Current dataset manifest: `data/draw_manifest.json`
- Agent operating rules: `configs/agent.md`
- Master architecture: `core/heps_architecture.md`
- External AI proposals: `workspace/contributions/`
- Red-team reviews and merge decisions: `workspace/reviews/`
- Prediction and analysis outputs: `outputs/`

# Pipeline

HEPS v33.4 is explicitly staged:

**Expert Discovery → Recall Guard → Directional Scenarios → Coalition Intelligence → Portfolio Covering → Frozen Prediction → Post-Draw Attribution**

A downstream stage must never receive credit for a failure or success caused upstream.

## Stage A — Matrix A candidate discovery

Main numbers operate on a 1–50 coordinate system.

Active expert lanes:

### 1. Coulomb Stiction / Shadow

Tracks exact repeats, ±1 and ±2 numerical shadows from recent draws. Sorted values are not physical draw order.

### 2. Coulomb Void Potential

Tracks prolonged absence and under-filled regions as temporal/spatial starvation features. This is a research score, not an overdue-number law.

### 3. Sorted-Position Momentum

Tracks distributions of sorted Slot1–Slot5 order statistics. It may nominate structurally compatible coordinates but cannot be described as ball trajectory.

### 4. Harmonic Boundary Governor

Tracks register persistence and correction scenarios. High-register continuation is a lane, not a mandatory scalar bias.

### 5. Tri-Cluster Lane

Generates some compact three-number structures. It must not be forced on every line.

### 6. Stale-Hot / Return-Horizon

Nominates recurring but rested coordinates. Keep distinct from pure cold/overdue logic.

### 7. Midfield / Structural Rescue

Maintains central-field candidates that may be erased when hot/high/void experts dominate. Its purpose is recall robustness, not a claim that central numbers are intrinsically more likely.

### 8. Chaos / Baseline Lane

Supplies mandatory null/control candidates and lines.

## Stage A2 — Dual-Pool Candidate Recall Guard

The 2026-08-04 prospective target exposed a Stage-A failure: the frozen 22-number hierarchy contained only `16` from actual `16,24,29,34,38`. Pair-of-Pairs assembly could not recover the four omitted winners.

HEPS therefore maintains two candidate sets:

- **core_pool** — compact model-selected candidates for dense coalition search;
- **rescue_pool** — broader specialist/structural union intended to reduce catastrophic omission risk.

Recommended research ranges for 20-line slates:

- core pool: 13–18;
- rescue union: approximately 22–26.

These sizes are not assumed optimal. Report pool size with every recall statistic because larger pools mechanically improve recall under the null.

Candidate discovery must preserve expert provenance. Do not average all expert scores into one scalar before nominations are recorded.

Mandatory Stage-A KPIs:

- core-pool winner recall;
- rescue-pool winner recall;
- recall by expert source;
- recall relative to the uniform hypergeometric expectation for the same pool size.

Current evidence boundary: single-feature 22-number mechanical-era walk-forward recall is approximately null-equivalent; no expert currently has a demonstrated Stage-A edge.

## Stage B — Directional Scenario Router

H/L/R means whether the next sorted slot is Higher, Lower or Repeat relative to the current sorted slot value. These states are not equiprobable.

HEPS must preserve at least two scenario families:

1. **null_geometry** — modal H/L/R state from the exact fair 5/50 order-statistic distribution conditional on the current slot value;
2. **hlr_motif_challenger** — a symbolic motif-continuation hypothesis frozen before the target draw.

An explicitly stated director/human HLR template may be added as a third challenger if it is frozen pre-draw.

HLR is a routing/scenario feature, not a hard veto. When scenarios disagree, preserve separate lines rather than forcing one consensus state.

### Evidence boundary for HLR

The user-provided 811-draw legacy main workbook was used as a diagnostic prior only. A 600-train/211-holdout motif classifier underperformed exact fair modal geometry in all five sorted slots and PB. Therefore global HLR predictive edge is not accepted.

On the much smaller mechanical sample, the frozen legacy motif PB-direction rule scored 9/14 testable targets versus 7/14 for fair modal direction. This remains challenger-level evidence only.

## Stage C — Coulomb Pair-of-Pairs + Anchor Coalition Assembler

This remains the accepted HEPS synthesizer-stage module from v33.3.

Canonical topology:

`pair_A + anchor + pair_B`

Candidate pairs may be supported by:

- void/starvation;
- stiction/shadow;
- adjacency/short-span geometry;
- stale-hot return horizon;
- pair-bridge evidence;
- sorted-position compatibility;
- cross-expert agreement;
- complementary expert roles;
- directional-scenario compatibility.

Dual-cluster structures are legal. The assembler must retain pair and anchor provenance.

### Breakthrough evidence — 2026-07-31

The frozen pre-draw hierarchy contained all five actual mains `10,11,37,45,46`, while the published portfolio assembled at most 2/5. Retrospective coalition research produced `02,10,11,37,46` = 4/5 and contained the exact winning line `10,11,37,45,46` at rank 19 of 417 generated challengers, naturally represented as `(10,11) + 37 + (45,46)`.

This is an assembly architecture improvement, not proof of durable predictive edge.

## Stage D — Portfolio covering and 20-line research slate

For a 20-line prospective slate, the v33.4 default experimental allocation is:

| Class | Count | Purpose |
|---|---:|---|
| Core-pool Pair-of-Pairs coalitions | 8 | Highest-supported expert-preserving coalitions |
| Rescue-pool specialist coalitions | 4 | Protect minority/omitted candidate hypotheses |
| Directional-scenario lines | 4 | Split null-geometry and HLR/director motif scenarios |
| Maximum-coverage rescue lines | 2 | Improve marginal pair/triple coverage |
| Matched random/control lines | 2 | Null comparison and anti-overfit control |

All 20 submitted/frozen lines remain in the denominator. Never report only the best subset after the draw.

For a 10-line slate, v33.3 allocation remains a valid reduced-budget benchmark and must be labeled separately.

Maximum-coverage optimization can improve conditional 3+/4+ coverage when winners are already inside the candidate set, but cannot improve exact 5/5 probability under a uniform coalition posterior except by increasing the number of distinct lines.

## Matrix B — Hierarchical PowerBall field

PowerBall operates on a 1–16 coordinate system.

Prediction is now explicitly hierarchical:

### B1. Direction classifier

Predict `H`, `L` or `R` relative to the current PB value. Report the exact fair conditional base rate:

- `P(L) = (current_pb - 1) / 16`
- `P(R) = 1 / 16`
- `P(H) = (16 - current_pb) / 16`

A direction hit is interpreted relative to that base rate. Example: after PB15, `L` already has 87.5% fair probability and is therefore weak evidence by itself.

### B2. VVD / displacement challenger

A displacement or VVD hypothesis may narrow the balls within the predicted direction. Its definition must be explicit and frozen pre-draw. Intuitive VVD and absolute numerical delta must not be silently conflated.

### B3. Exact-ball ranking

Rank exact PB candidates using recurrence, capped return horizon, stale-hot, local shadow and other frozen features. Score exact-ball success separately from B1 direction success.

Current Matrix-B research modules:

- 16-ball fulcrum center = 8.5;
- upper/lower register routing;
- provisional circuit-breaker diagnostic;
- stiction ±1/±2 support;
- stale-hot / return-horizon support;
- HLR directional motif challenger;
- VVD/displacement challenger;
- low-collapse/high-rise hedge.

## Machine / PowerBall XTRA doctrine

PowerBall and PowerBall XTRA are separate draws. A prediction targeted at the main game cannot receive prospective XTRA credit merely because it matches the XTRA result.

Track machine identity when a trustworthy source provides it. Do not infer a machine swap from numerical resemblance between Main and XTRA. Machine-specific modelling remains disabled until sufficient authoritative metadata are collected.

## Rejected or downgraded claims

- Macro-sum `193` for `21,26,40,42,44` is rejected; correct sum is 173.
- Fixed macro-sum admissibility bands are rejected; sum is diagnostic/soft only.
- Sorted slots are not physical draw order.
- Cross-chamber coupling is not accepted without stronger evidence.
- Tri-cluster cannot be forced on every line.
- Hard entropy, parity, adjacency or decade vetoes are not accepted.
- HLR motif recurrence is not a demonstrated global predictive edge.
- A retrospective 4/5 coalition is not proof of a durable exact-line edge.
- Candidate-pool inflation cannot be described as predictive improvement without matched pool-size nulls.
- A PowerBall electronic-primary cutover on 2026-06-22 is not accepted as established fact.

## Required prediction report

1. Data cutoff and source state.
2. Architecture version.
3. Core candidate pool with provenance.
4. Rescue candidate pool with provenance.
5. Null-geometry HLR scenario.
6. HLR/director challenger scenarios.
7. Pair-of-Pairs challenger summary.
8. Frozen 10- or 20-line slate with line classes.
9. Portfolio coverage/redundancy diagnostics.
10. Matrix-B direction probabilities, VVD hypothesis and exact PB ranking.
11. Matched-null/control plan.
12. `paper_trading_only` evidence boundary.

## Required post-draw attribution

Score in this order:

1. candidate discovery — core and rescue pool recall;
2. directional scenario accuracy versus exact conditional null;
3. pair discovery;
4. coalition generation;
5. final portfolio routing;
6. PB direction;
7. PB displacement/VVD;
8. exact PB selection;
9. Main/XTRA cross-score recorded only as retrospective diagnostic;
10. matched random/null comparison;
11. recommended change with merge/no-merge decision.

Failure labels include:

- candidate failure;
- scenario-routing failure;
- pair-edge failure;
- anchor failure;
- coalition-generation failure;
- final-selection failure;
- regime/machine-metadata uncertainty;
- PB-direction failure;
- PB-VVD failure;
- PB-exact failure;
- null-equivalent result.

## Current primary KPIs

- core-pool and rescue-pool candidate recall with pool-size null;
- exact 3/4/5 main outcomes per submitted line and per game;
- best assembled overlap conditional on recall;
- Top-10 and Top-20 3+/4+ main overlap;
- pair-of-pairs exact-pair capture and anchor hit rate;
- unique-pair / unique-triple portfolio coverage;
- H/L/R direction accuracy versus exact conditional null;
- PowerBall exact hit rate;
- same-line main + PB outcomes;
- ±1/±2 shadow support;
- matched-random baseline comparison.

Every result retains its submitted-line and candidate-pool denominators. Architectural improvement and predictive edge are separate claims.
