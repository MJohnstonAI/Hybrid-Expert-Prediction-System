# Physics of Failure — Main 2026-09-11

Result status: user-reported, pending external verification. Canonical draw ledger is not updated by this artifact.

Actual Main: `9, 11, 13, 38, 43`; PB `13`.

## Stage 1 — Candidate acquisition

Frozen K13: `4, 8, 13, 14, 16, 19, 22, 27, 31, 34, 37, 39, 40`.

Only `13` survived: **1/5**. This is the first binding failure. The same fixed-K13 research target has now produced 1/5 on 2026-09-04, 2026-09-08 and 2026-09-11. Three consecutive <=1 outcomes are not by themselves statistically extraordinary under a random K13 benchmark, but they are operationally unacceptable for a system whose downstream assembly needs 4+/5 survival.

The near-null E0030 field itself again did not badly miss the exact line in proper-score terms: target log-loss delta model minus uniform was about `-0.00253` nats, a tiny improvement. The failure is therefore best described as **weak/non-identifiable probability differences amplified by hard K13 compression**, not as a large probability-field calibration collapse.

A useful diagnostic is that the frozen anywhere ranking placed three winners in its Top20: `13` rank 8, `38` rank 19, `43` rank 20. The other two were `9` rank 25 and `11` rank 42. This gets zero K13 credit, but it shows that the 13-seat cutoff discarded two winners that were still near the broader high-ranked region.

## Stage 2 — Assembly

Because K13 contained only one winner, E0033 cannot be judged on its declared objective of floating a covered 4+/5 line into the Top10. Johnson membership and PPMI ordering receive neither credit nor blame for exact 4+/5 or 5/5 assembly on this target.

The best Main overlap in the 20-line slate was therefore necessarily 1/5. Any attempt to infer assembly failure from this target would violate stage isolation.

## PowerBall

PB primary `11` missed. Actual PB `13` was inside the six-ball shortlist `[11,4,15,6,1,13]` and was assigned to ranks 6, 12 and 18. Rank 12 also contained Main `13`, producing one Main hit plus the correct PB. This is a shortlist hit, not a primary-model success; evidence remains `INSUFFICIENT_EVIDENCE`.

## Transition diagnostics

From 2026-09-08 `[4,8,13,37,49]` to 2026-09-11 `[9,11,13,38,43]`:

- signed delta: `[+5,+3,0,+1,-6]`
- HLR: `HHRHL`
- VVD: `[5,3,0,1,6]`
- SUMAD: `3`
- LDSAD: `7`
- SPANAD: `11`
- PB: `7 -> 13`, VVD `6`

No post-result retuning is permitted from these values.

## Research implication

The immediate bottleneck remains **uncertainty-aware fixed-K compression**. When anywhere marginals differ by only tiny amounts, deterministic rank-13 inclusion can make a categorical decision unsupported by the estimation uncertainty. Future work should compare the current point-estimate K13 against preregistered uncertainty-aware or robust-seat allocation at the same K=13, without using 2026-09-11 outcomes to tune thresholds.

E0033 geometry-first assembly should remain frozen as a prospective shadow until a future target gives K13 at least four winners and therefore actually exposes the assembly stage.
