# E0035 Decision — Bayesian-Bootstrap Uncertainty-Aware Fixed-K13 Compression

## Decision

`ACCEPT EXPERIMENT / HOLD PREDICTIVE PROMOTION / FREEZE PROSPECTIVE SHADOW`

Evidence classification: `INSUFFICIENT_EVIDENCE`.

Paper trading only.

## Data and implementation integrity

The Main canonical ledger was updated and validated through `2026-09-11` before the replay. The E0035 protocol uses only the active series beginning `2026-06-02` and keeps `K=13` fixed.

GitHub Actions reproduced the experiment under Python 3.12 and the repository validation suite passed with 69 tests. The E0035 replay used 25 target-excluded forecasts and 16 deterministic-seed Bayesian-bootstrap replicates per target.

## Replay result

Across 25 post-June walk-forward targets:

| Arm | Winner coordinates | Mean hits | H<=1 catastrophes | H>=3 draws | H>=4 | 5/5 |
|---|---:|---:|---:|---:|---:|---:|
| POINT_MEAN | 31 | 1.24 | 18 | 3 | 0 | 0 |
| POINT_ROBUST | 32 | 1.28 | 18 | 3 | 0 | 0 |
| BB_MEAN | 30 | 1.20 | 17 | 1 | 0 | 0 |
| BB_ROBUST | 30 | 1.20 | 17 | 1 | 0 | 0 |

Relative to `POINT_MEAN`, `BB_ROBUST` was better on 4 targets, equal on 17, and worse on 4, with net `-1` winner coordinate (`-0.04` hits/draw).

The Bayesian-bootstrap arm reduced the retrospective catastrophe count by one draw, but this came with lower total recall and fewer 3+ outcomes. No arm produced a 4+/5 K13 target in this replay.

`BB_ROBUST` and `BB_MEAN` produced identical summary performance, and for the 2026-09-15 frozen state they converge to the same basket. Thus the present posterior-predictive field does not provide evidence that the nonlinear robust optimizer adds value beyond posterior-predictive marginal ranking.

## Important upstream warning

The held-fixed E0030 point field remains slightly worse than uniform on historical proper score: mean exact-line log-loss delta model-minus-uniform is approximately `+0.001466` nats/target.

Therefore E0035 cannot establish a predictive edge even if compression metrics improve. The experiment tests decision robustness under field uncertainty, not new predictive information.

## Recent-draw diagnostic

Post-hoc only, with zero prospective credit:

- 2026-09-04: POINT_MEAN 0/5, BB_ROBUST 1/5;
- 2026-09-08: both 1/5;
- 2026-09-11: POINT_MEAN 1/5, BB_ROBUST 2/5.

This recent pattern motivated preserving the challenger prospectively, but it may not be used as evidence for promotion because E0035 was designed after these results existed.

## Prospective decision for 2026-09-15

Freeze both matched-K controls before result availability:

- `POINT_MEAN`: `[4,8,9,13,14,16,19,22,27,31,37,38,40]`
- `BB_ROBUST`: `[4,9,13,14,16,19,22,27,31,34,37,38,40]`

The uncertainty-aware challenger replaces `8` with `34`. All other 12 seats are identical.

This is a clean one-seat prospective comparison. Neither basket has production authority.

## Forward rule

1. Continue `BB_ROBUST` only as a prospective matched-K shadow.
2. Do not replace the incumbent K13 from this retrospective replay.
3. Score every future eligible target on winner count, H<=1 catastrophe, 3+/4+/5 survival, and seat-level wins/losses.
4. Do not change bootstrap count, seed rule, E0030 formulas, or robust objective based on 2026-09-15 outcome.
5. Reassess after multiple prospective targets; one draw cannot promote or reject the uncertainty-aware compressor.
6. Continue upstream probability-field research independently because compression cannot compensate for an uninformative field.
