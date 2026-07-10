# HEPS Master Architecture

## Active branch

HEPS v33.2 — External IDE Mechanical Research Workspace

## Purpose

HEPS is a file-based, multi-agent, paper-trading prediction research system for South African PowerBall. It uses a canonical draw ledger, markdown strategy files, external AI contribution files, red-team reviews, and structured prediction/post-game outputs.

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

## Matrix B — PowerBall field

PowerBall operates on a 1–16 coordinate system.

Active modules:

- 16-ball fulcrum center = 8.5;
- upper-tier resonance / ramp tracker;
- provisional circuit-breaker threshold `tau = 6.8`;
- stiction and ±1/±2 shadow support;
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
- 1–100 score-band reporting for long-term calibration.

## Rejected or downgraded claims

- Macro-sum 193 for `21, 26, 40, 42, 44` is rejected. Correct sum is 173.
- Sorted slots are not physical draw order.
- Cross-chamber coupling is not accepted without stronger evidence.
- Tri-cluster cannot be forced on every prediction line.
- >4 hit efficiency is tracked but too sparse to be the current primary KPI.

## Current portfolio allocation

For a top-10 prediction slate:

| Lane | Count | Purpose |
|---|---:|---|
| Tri-cluster / high-register continuation | 3 | Preserve mechanical cluster hypothesis |
| Void-bridge / canyon-fill | 3 | Cover starvation gaps between recent clusters |
| Stiction-shadow continuation | 2 | Carry repeats and ±1/±2 shadows |
| Sorted-position momentum | 1 | Track order-statistic drift |
| Chaos / random-baseline hedge | 1 | Protect against overfit |

## Required prediction report sections

1. Dataset state and latest draw.
2. Active architecture branch.
3. Prediction slate.
4. Lane rationale.
5. Risk and uncertainty notes.
6. Baseline comparison plan.

## Required post-game report sections

1. Actual draw.
2. Hit counts by slate.
3. Best overlap.
4. PowerBall hit status.
5. ±1 drift support.
6. Macro-sum/spread comparison.
7. Expert contribution notes.
8. Recommended parameter changes.
9. Merge/no-merge decision.

## Current primary KPIs

- exact 3, 4, and 5 main-number outcomes per submitted line and per game;
- same-line 3+ main numbers plus PowerBall;
- same-line 4+ main numbers plus PowerBall;
- same-line 5 main numbers plus PowerBall as the ultimate game outcome;
- Top-10 3+ main-number overlap;
- Top-100 3+ main-number overlap;
- Top-100 4+ main-number overlap;
- PowerBall exact hit rate;
- ±1 drift support;
- macro-sum pass/fail;
- random-filtered baseline comparison.

All outcome rates must retain their submitted-line denominator. A single
ultimate outcome is a valid project milestone, but it is not evidence of a
durable predictive edge unless performance also survives walk-forward and
random/null comparison.
