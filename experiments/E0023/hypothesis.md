# E0023 — Slot-1 Anchored Decade-Shell Echo

## Hypothesis

For South African PowerBall Main Mechanical-Era draws, a completed five-number line may carry residual coalition information when its decade-occupancy shell is unusually recurrent **conditional on its Slot 1 minimum**, after exact 5/50 order-statistic geometry is removed.

This is not a claim that repeated decade patterns or repeated Slot 1 values are predictive by themselves.

## Motivation

Two Main pairs showed the same Slot 1 and the same five-decade occupancy shell while the other exact coordinates largely rotated:

- `3,12,27,36,47` and `3,14,26,40,48` -> shell `(1,1,1,1,1)`
- `9,14,27,32,34` and `9,13,21,36,40` -> shell `(1,1,1,2,0)`

The research question is whether `P(shell | Slot1)` contains residual information beyond the exact IID 5/50 null, not whether historical coordinates should repeat.

## Primary score

For a legal sorted line `C`:

- `m = Slot1(C)`
- `d(C)` = decade-count signature over `1-10,11-20,21-30,31-40,41-50`
- `P0(d|m)` = exact combinatorial probability under uniform 5-of-50 conditional on minimum `m`
- `c(m,d)` = prior post-June count of state `(m,d)`
- `c(m)` = prior count of Slot1 `m`

With frozen `kappa=20`:

`P_hat(d|m) = (c(m,d) + 20*P0(d|m)) / (c(m) + 20)`

`R_shell(C) = log(P_hat(d|m) / P0(d|m))`

If Slot1 `m` has never occurred, the score is neutral.

## Data boundary

- Main only.
- Active history begins `2026-06-02`.
- No pre-June history may enter fitting, calibration, replay or ranking.
- No fitted state transfers to XTRA.

## Authority requested

Coalition/winner-float diagnostic shadow only. It may score completed lines after K13 is frozen, but it may not change candidates, K, pruning, morphology or line budget.

## Falsification

Reject forward predictive authority if prospective winner-rank performance remains near random, is redundant with E0013/frequency/recency, or increases catastrophic burial.
