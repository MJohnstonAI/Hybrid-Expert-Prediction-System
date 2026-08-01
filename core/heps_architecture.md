# HEPS Master Architecture

## Active branch

HEPS v33.3 — Coalition Assembly Breakthrough

## Purpose

HEPS is a file-based, multi-agent, paper-trading prediction research system for South African PowerBall. It uses a canonical draw ledger, markdown strategy files, external AI contribution files, red-team reviews, structured prediction/post-game outputs, and an expert-preserving coalition synthesizer.

## Active data doctrine

The active dataset is the post-May/June 2026 mechanical-era South African PowerBall dataset.

Earlier HEPS strategies and algorithms may be reused, but parameters must be recalibrated on the active dataset. The system should not depend on old pre-transition draw history for active modelling.

## Core storage doctrine

- Canonical draw ledger: `data/draw_history.jsonl`
- Current dataset manifest: `data/draw_manifest.json`
- Agent operating rules: `configs/agent.md`
- Master architecture: `core/heps_architecture.md`
- External AI proposals: `workspace/contributions/`
- Red-team reviews and merge decisions: `workspace/reviews/`
- Prediction and analysis outputs: `outputs/`

## Matrix A — Main field

Main numbers operate on a 1–50 coordinate system.

Active strategy modules:

### 1. Coulomb Stiction / Shadow

Tracks exact repeats, ±1, and ±2 shadow shifts from recent draws.

### 2. Coulomb Void Potential

Tracks under-filled canyons between recent clusters. A coordinate may gain attractiveness because it lies in a starvation gap, not only because it sits near a recent winner.

### 3. Sorted-Position Momentum

Tracks movement of sorted Slot1–Slot5 positions as order statistics. Do not describe this as physical ball-path tracking unless true drawn-order data is available.

### 4. Harmonic Boundary Governor

Detects high-register persistence and decides whether to allow continuation, bridge the middle, or hedge downward correction.

### 5. Tri-Cluster Lane

Generates some slates with 3 numbers inside a 6-number span. This is a portfolio lane, not a universal rule.

### 6. Sum/Spread Governor

Prevents all slates from collapsing into over-tight or over-wide structures.

### 7. Chaos / Baseline Lane

Maintains diversity and protects against overfitting by keeping baseline-style coverage in the portfolio.

### 8. Coulomb Pair-of-Pairs + Anchor Coalition Assembler

This is the accepted HEPS **synthesizer-stage** module for joining complementary expert evidence into coherent five-number lines. It is not a standalone expert and must preserve the provenance of the contributing experts.

The assembler searches for a topology of:

- supported pair A;
- supported, disjoint pair B;
- one anchor with consensus, stale-hot, structural, or cross-expert support.

The canonical form is:

`pair_A + anchor + pair_B`

Dual-cluster structures are explicitly legal. A low pair and a high pair may coexist when supported by different experts and joined by a compatible anchor. The synthesizer must not automatically reject such lines as over-clustered.

Candidate pairs may be supported by one or more of:

- Coulomb void / temporal-starvation evidence;
- stiction or ±1/±2 shadow evidence;
- adjacency or short-span geometry;
- stale-hot / return-horizon support;
- pair-bridge history;
- sorted-position compatibility;
- cross-expert agreement;
- complementary role structure.

The assembler should produce a broad challenger set, then select the final portfolio jointly using maximum-coverage / redundancy control rather than ranking each line independently and taking the first ten.

### Breakthrough evidence — 2026-07-31

The frozen pre-draw 17-number candidate hierarchy contained all five eventual winning mains `10,11,37,45,46`, but the previous HEPS final portfolio assembled at most **2/5** on one line.

The coalition-assembly research produced the retrospective graph line `02,10,11,37,46`, containing **4/5** winning mains. The pair-of-pairs + anchor challenger set also contained the exact winning line `10,11,37,45,46`, ranked **19th among 417 generated coalitions**. The winning topology can be expressed as `(10,11) + 37 + (45,46)`.

This is accepted as an **architectural breakthrough in coalition assembly relative to the previous HEPS synthesizer**. It is not evidence of a proven exact 5/5 predictive edge because the 4/5 and exact-line-rank results were obtained retrospectively after the target result was known.

## Matrix B — PowerBall field

PowerBall operates on a 1–16 coordinate system.

Active modules:

- 16-ball fulcrum center = 8.5;
- upper-tier resonance / ramp tracker;
- provisional circuit-breaker threshold `tau = 6.8`;
- stiction and ±1/±2 shadow support;
- stale-hot recurrence / return-horizon support;
- low-collapse hedge.

## Accepted strategy imports

These strategies are accepted as provisional HEPS modules:

- Physics-of-Failure hypothesis layer;
- Dual-Matrix Engine;
- Coulomb Void Potential;
- sorted-position momentum;
- Harmonic Boundary Governor;
- gamma compression throttling after high-register persistence;
- Tri-Cluster Matrix as a lane;
- PowerBall circuit-breaker model;
- stale-hot PowerBall ranking as a research feature;
- 1–100 score-band reporting for long-term calibration;
- **Coulomb Pair-of-Pairs + Anchor Coalition Assembler**;
- **joint maximum-coverage final-line selection**.

## Rejected or downgraded claims

- Macro-sum 193 for `21, 26, 40, 42, 44` is rejected. Correct sum is 173.
- Sorted slots are not physical draw order.
- Cross-chamber coupling is not accepted without stronger evidence.
- Tri-cluster cannot be forced on every prediction line.
- >4 hit efficiency is tracked but too sparse to be the current primary KPI.
- A retrospective 4/5 coalition is not proof of a durable predictive edge.
- Maximum-coverage optimization cannot improve exact 5/5 probability if all candidate coalitions are equally likely; exact improvement requires validated non-uniform coalition evidence.

## Current portfolio allocation

The previous architecture treated lane outputs too independently. HEPS v33.3 retains expert diversity but adds a coalition synthesis stage before final publication.

### Candidate-generation quotas

Expert lanes continue to supply diversified seeds and candidate evidence:

| Expert source | Seed emphasis |
|---|---|
| Tri-cluster / high-register | Cluster and upper-register candidates |
| Void-bridge / canyon-fill | Temporal void and starvation candidates |
| Stiction-shadow | Repeat and ±1/±2 candidates |
| Sorted-position momentum | Order-statistic-compatible candidates |
| Stale-hot / return-horizon | Recurring but rested candidates |
| Chaos / random control | Null/control candidates |

### Final top-10 line allocation

| Final line class | Count | Purpose |
|---|---:|---|
| Pair-of-pairs + anchor coalition champion | 3 | Join complementary expert pairs around a strong anchor |
| Void-led coalition | 2 | Preserve Coulomb temporal-void specialist evidence |
| Tri-cluster / high-register coalition | 2 | Preserve cluster and high-register hypotheses |
| Stiction or sorted-structure coalition | 1 | Preserve local shadow/order-statistic evidence |
| Cross-expert maximum-coverage coalition | 1 | Maximize non-redundant 3+/4+ conditional coverage |
| Chaos / matched-random baseline | 1 | Protect against overfit and provide a null comparison |

All nine model-driven lines should pass through coalition redundancy checks. The chaos line must remain outside the optimized model selection process.

## Coalition synthesis requirements

For each generated model-driven line, record:

1. `pair_a` and its contributing experts;
2. `pair_b` and its contributing experts;
3. the selected `anchor` and its support sources;
4. candidate-level scores before line assembly;
5. coalition / pair interaction score;
6. line geometry and register profile;
7. portfolio redundancy contribution;
8. whether the line was selected by champion rank or maximum-coverage need.

Candidate recall and assembly success must be reported separately after every draw.

## Required prediction report sections

1. Dataset state and latest draw.
2. Active architecture branch/version.
3. Candidate hierarchy and expert provenance.
4. Pair-of-pairs + anchor challenger summary.
5. Final prediction slate.
6. Lane / coalition rationale.
7. Coverage and redundancy summary.
8. Risk and uncertainty notes.
9. Baseline comparison plan.

## Required post-game report sections

1. Actual draw.
2. Candidate-pool recall: how many of the five winners were available before assembly.
3. Hit counts by slate.
4. Best overlap.
5. PowerBall hit status.
6. Pair and anchor attribution.
7. Assembly-stage success/failure diagnosis.
8. ±1 drift support.
9. Macro-sum/spread comparison.
10. Expert contribution notes.
11. Comparison with prior selector and matched random control.
12. Recommended parameter changes.
13. Merge/no-merge decision for further architecture changes.

## Current primary KPIs

- candidate-pool recall of winning main numbers;
- exact 3, 4, and 5 main-number outcomes per submitted line and per game;
- best assembled overlap conditional on candidate recall;
- same-line 3+ main numbers plus PowerBall;
- same-line 4+ main numbers plus PowerBall;
- same-line 5 main numbers plus PowerBall as the ultimate game outcome;
- Top-10 3+ main-number overlap;
- Top-100 3+ main-number overlap;
- Top-100 4+ main-number overlap;
- PowerBall exact hit rate;
- pair-of-pairs exact-pair capture;
- anchor hit rate;
- portfolio unique-pair / unique-triple coverage;
- ±1 drift support;
- macro-sum pass/fail;
- matched-random baseline comparison.

All outcome rates must retain their submitted-line denominator. A single ultimate outcome is a valid project milestone, but it is not evidence of a durable predictive edge unless performance also survives walk-forward and random/null comparison.