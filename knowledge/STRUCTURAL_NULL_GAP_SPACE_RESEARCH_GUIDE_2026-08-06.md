# HEPS Structural Null + Gap-Space Research Guide

**Date:** 2026-08-06  
**Status:** methodological baseline + experimental research  
**Primary experiment:** `experiments/E0001/`  
**Related experiment:** `experiments/CANDIDATE_LATTICE_V01/`

## 1. Why this guide exists

Claude Sonnet's corrected red-team review identified a critical confound in HEPS slot forecasting: `MAIN_HLR_SLOT` and `MAIN_VVD_DELTA` may appear informative because sorted 5/50 order statistics already create strong conditional LOW/HIGH and displacement probabilities even when consecutive draws are completely independent.

Gemini independently proposed reparameterizing sorted lines into gap space. After correcting the internal-gap formula, that representation gives HEPS an exact and compact structural null.

The combined research question is:

> After removing everything implied by exact IID sorted-5/50 geometry, is any residual temporal information left for HEPS to exploit?

Until this question is answered prospectively, HLR, VVD, joint-flow ranking, and gap-residual models remain experimental.

## 2. Exact sorted-slot null

For slot `j` and legal coordinate `n`:

`P0(X_(j)=n) = C(n-1,j-1) * C(50-n,5-j) / C(50,5)`.

This is exact under uniform independent 5-from-50 sampling.

Given previous same-slot coordinate `p`:

- `P0(LOW|p,j)` is the sum below `p`;
- `P0(REPEAT|p,j)` is the probability at `p`;
- `P0(HIGH|p,j)` is the sum above `p`.

This baseline must be used before crediting HLR with temporal signal.

## 3. Friday 2026-08-07 structural-null audit

Frozen previous main draw:

`16, 24, 29, 34, 38`

Frozen committed HLR vector:

`HLHHL`

The exact slot-direction null is:

| Slot | Prev | P0(LOW) | P0(REPEAT) | P0(HIGH) | Committed call | Frozen model p(call) |
|---:|---:|---:|---:|---:|---|---:|
| 1 | 16 | 0.846782 | 0.021888 | 0.131330 | HIGH | 0.6051 |
| 2 | 24 | 0.771385 | 0.028224 | 0.200391 | LOW | 0.7366 |
| 3 | 29 | 0.616156 | 0.037465 | 0.346379 | HIGH | 0.6773 |
| 4 | 34 | 0.440341 | 0.041201 | 0.518458 | HIGH | 0.6472 |
| 5 | 38 | 0.205732 | 0.031172 | 0.763096 | LOW | 0.5807 |

The fitted model therefore makes strong anti-null calls at Slots 1, 3, and 5. This is not evidence of an edge; it is a high-risk hypothesis that must be scored prospectively.

## 4. Exact joint 243-vector null

Per-slot HLR states cannot be multiplied independently because sorted slots are dependent.

For a fixed previous draw, enumerate all `C(50,5)=2,118,760` legal next draws and count the resulting HLR vector.

For the 2026-08-07 previous state, the highest-probability IID vectors begin:

| Null rank | Vector | Count | Probability |
|---:|---|---:|---:|
| 1 | LLLLH | 405720 | 0.191489 |
| 2 | LLLLL | 358608 | 0.169254 |
| 3 | LLLHH | 323760 | 0.152807 |
| 4 | LLHHH | 253350 | 0.119574 |
| 5 | LHHHH | 170535 | 0.080488 |
| 6 | HHHHH | 151070 | 0.071301 |

Several Candidate Lattice rescue vectors are already top structural-null vectors. That overlap must not be credited as learned predictive skill without incremental evidence.

The committed Friday vector `HLHHL` has:

- count: `336`;
- exact probability: `0.0001585833` = `0.01585833%`;
- exact structural-null rank: `109 / 243` using competition rank by probability mass.

## 5. Retrospective joint-flow diagnostic

Previously reported Candidate Lattice actual-vector ranks were `3/243`, `8/243`, `8/243` for 2026-07-28, 2026-07-31, and 2026-08-04.

Against the exact joint structural null:

| Target | Actual vector | Candidate Lattice rank | Exact null rank | Exact null probability |
|---|---|---:|---:|---:|
| 2026-07-28 | LHHHH | 3 | 2 | 0.109843 |
| 2026-07-31 | HLHHL | 8 | 26 | 0.006938 |
| 2026-08-04 | HHLLL | 8 | 3 | 0.138727 |

Two of the three apparently strong flow ranks are better explained by the exact geometry. The 2026-07-31 residual remains interesting but is one post-hoc example and therefore `INSUFFICIENT_EVIDENCE`.

## 6. Exact VVD null

For previous coordinate `p` in slot `j`, the exact null displacement distribution is obtained by summing the slot probability at legal `p-d` and `p+d` coordinates, counting `d=0` once.

A learned VVD distribution receives predictive credit only if it improves proper probability score against this exact comparator.

## 7. Correct gap-space representation

For sorted main numbers `S1 < S2 < S3 < S4 < S5`, define the six gaps as counts of unselected numbers:

`G = (S1-1, S2-S1-1, S3-S2-1, S4-S3-1, S5-S4-1, 50-S5)`.

The four `-1` terms on internal gaps are mandatory. Without them the components sum to 49 rather than 45.

Every legal gap vector satisfies:

- `G_i >= 0`;
- `sum(G_i)=45`.

The sorted coordinates reconstruct as:

- `S1 = G1 + 1`;
- `S2 = G1 + G2 + 2`;
- `S3 = G1 + G2 + G3 + 3`;
- continuing analogously.

For the 2026-08-04 line `16,24,29,34,38`, the gap vector is:

`15, 7, 4, 4, 3, 12`.

## 8. Exact gap null

Under uniform independent 5/50 sampling, each legal five-number combination maps one-to-one to a weak composition of 45 into six nonnegative gaps.

The number of such compositions is:

`C(45+6-1,6-1) = C(50,5) = 2,118,760`.

Therefore every legal gap vector is equally probable.

This is exactly:

`G ~ DirichletMultinomial(N=45, alpha=[1,1,1,1,1,1])`.

It is **not** an ordinary multinomial with fixed `p_i=1/6`, which would incorrectly favor balanced gaps.

The exact null mean of each gap is `45/6 = 7.5`.

## 9. Conservation and HLR interpretation

Because every draw has `sum(G)=45`, consecutive gap changes obey:

`sum(Delta G_i)=0`.

Slot movement is cumulative gap movement:

`Delta S_j = sum_{i=1..j} Delta G_i`.

Thus the five HLR states are not independent primitive states; they are signs of cumulative changes in a constrained six-component composition.

This helps explain why joint HLR vectors can be strongly shaped by geometry even under IID draws.

## 10. Gap-residual research

Under IID independence:

`E[G_i,t+1]=7.5`.

The expected change from current gap `G_i,t` is:

`E[Delta G_i | G_i,t] = 7.5 - G_i,t`.

A null-adjusted residual may be written:

`R_i,t+1 = Delta G_i - (7.5 - G_i,t)`.

This simplifies algebraically to `G_i,t+1 - 7.5`; the residual form is useful only because it makes the removed structural mean-reversion term explicit.

Predictive research must ask whether prior information can forecast this residual or the next gap distribution better than `NULL_GAP_DM`.

## 11. Dirichlet alternatives and overfitting guardrail

Do not fit six unconstrained Dirichlet parameters with only ~19 active draws and then interpret in-sample fit as prediction.

A defensible first diagnostic alternative is one symmetric concentration parameter:

`alpha_1 = ... = alpha_6 = c`.

Null: `c=1`.

Interpretation:

- `c<1`: more extreme gap allocations / clustering than the uniform-composition null;
- `c>1`: more balanced gap allocations.

This remains descriptive until frozen prospective evidence exists.

A later boundary-vs-interior model may use `alpha_edge` for G1/G6 and `alpha_internal` for G2-G5, but only after sample size and preregistration justify the added degrees of freedom.

## 12. Candidate-exposure implications

The frozen Candidate Lattice v0.1 union has 38 distinct main numbers. For a flat fixed 38-number basket under exchangeability:

- exact `P0(5/5 survival) = 0.23690366`;
- exact `P0(4+/5 survival) = 0.65496894`.

Therefore a 5/5 or 4+/5 candidate-union survival on one target is not evidence by itself. Evaluate lift against retained exact probability mass.

The 12 excluded Friday coordinates are:

`1,2,14,15,16,24,28,29,32,39,41,42`.

Three excluded coordinates (`16,24,29`) were in the immediately preceding draw. Under IID sampling, the probability at least one of those three specific numbers appears in the next five-number draw is approximately `0.27602041`. This exclusion risk should be scored explicitly; it is not proof repeats are favored.

## 13. Gemini candidate-engineering proposals retained as research notes

### Skip-state partitioning

Potential weak feature only. Do not impose hard 5/4/3/1 quotas. Active-era unseen numbers are left-censored and should not be assigned a precise overdue skip count.

### Spatial deciles

Reject hard `<=3 candidates per decile` pruning. It can destroy 5/5 recall by construction. Decile concentration may remain a diagnostic or portfolio-diversity measure.

### Multi-model consensus

Keep stage separation. Recency may be candidate-level; co-occurrence is coalition-level; last-digit and consecutive-pair structure are morphology/assembly features. Do not mix them into one unqualified Top-13 coordinate score.

### Meta-basket cascading

Worth later testing, but 13 is not a privileged basket size. Measure the recall/compression frontier for K such as `13,16,18,20,22,25,30` and compare exact matched-exposure nulls. Multiple scenario-conditioned sub-baskets are more defensible than an arbitrary 18-to-one-13 truncation.

## 14. Current research gate

Before expanding Candidate Lattice predictive complexity, run `E0001`:

1. `NULL_HLR_STRUCTURAL` vs learned HLR;
2. `NULL_VVD_STRUCTURAL` vs learned VVD;
3. `NULL_HLR_JOINT_243` vs joint flow ranker;
4. `NULL_GAP_DM` vs any learned gap model;
5. exact matched-exposure candidate survival vs candidate/meta-lattice methods.

Use proper probability scores and prospective freezes.

## 15. Evidence status

- Exact structural-null formulas: methodological facts / required baselines, not predictive edge.
- Candidate Lattice v0.1 predictive value: `INSUFFICIENT_EVIDENCE`.
- HLR incremental information beyond exact geometry: `INSUFFICIENT_EVIDENCE`.
- VVD incremental information beyond exact geometry: `INSUFFICIENT_EVIDENCE`.
- Gap-space representation as a coordinate system: mathematically valid.
- Gap-residual predictive information: `INSUFFICIENT_EVIDENCE`.
- Meta-basket/safe-exclusion architecture: experimental; evaluate only after matched-exposure controls.

## 16. Reproducibility

Use:

```bash
python scripts/structural_null.py --draw-id 19 --basket-size 13 --basket-size 18 --basket-size 38
```

The script computes exact per-slot HLR/VVD nulls, corrected gap-space representation, fixed-basket survival probabilities, and the exact joint HLR-vector distribution by enumerating all legal next draws.
