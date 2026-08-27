# E0016 Findings — HEPS-Evolve v0.2

## Executive result

**No predictive breakthrough was found.**

The stage-separated evolutionary search successfully falsified several attractive combinations. The strongest surviving current-regime lead remains the already-isolated E0013 positive-PMI spectral coalition ranker, which E0016 independently reproduced numerically. E0016 does **not** upgrade E0013 beyond `PROVISIONAL_SIGNAL` because the 17-target mechanical replay was already part of the discovery history and the first prospective target has not yet been scored.

## 1. Candidate acquisition still fails the decisive test

Evolve searched an 85-feature library spanning classical HEPS signals, structural-null residuals, graph diagnostics, drift-diffusion and one-dimensional optimal-transport fields.

The 470-target discovery champion combined:

- negative period-6 gap phase;
- negative structural-null-residualized VVD field, 50-transition window / shrinkage 5;
- positive discrete drift-diffusion field, 40-draw scale / half-step drift.

Discovery looked encouraging:

- mean winner rank 24.744;
- Top-13 recall 29.02%;
- Top-13 3+/5 draw rate 15.11%;
- Top-20 recall 42.51%.

The later 311-target block rejected the apparent gain:

- mean winner rank 25.537;
- Top-13 recall 24.63%;
- Top-13 3+/5 8.04%;
- Top-20 recall 38.97%.

Simple recency was better on the main rank/recall measures. This is classic evolutionary overfit and is the correct reason to kill the lineage.

## 2. Current-regime transfer also rejects the legacy-evolved candidate genome

Without retuning, the frozen legacy champion was applied to 17 current Main targets with at least eight prior mechanical-era draws.

It produced:

- mean winner rank 26.44;
- Top-13 recall 24.71%;
- Top-10 recall 16.47%.

The current sample is small, but there is no evidence of a transferable acquisition edge.

A simple historical successor-transition feature (`transition_w50_d1`) was one of the more stable single historical features, but it also failed current transfer (mean rank 26.75, Top-13 25.88%). It therefore receives no current HEPS authority.

## 3. Generalized coalition evolution also overfits

A 17-feature coalition library combined raw pair counts, PPMI, spectral coherence, diffusion distance, additive candidate fields and soft morphology.

The legacy discovery champion used:

- positive raw-pair support;
- negative 5-eigenvector spectral coherence;
- negative short-time diffusion coherence.

It reached approximately 0.540 discovery winner percentile and 0.549 morphology-matched percentile, but the later 311-target block returned to approximately random:

- mean percentile 0.4996;
- morphology-matched percentile 0.5078.

Applied without retuning to the current 2026 regime, it reversed badly to mean percentile ~0.374. It is rejected as a general coalition predictor.

## 4. E0013 is independently reproduced

E0016 rebuilt the E0013 operator from the written formula only:

1. positive-PMI adjacency with the frozen +0.5/+1 smoothing;
2. normalized graph Laplacian;
3. three smallest strictly positive eigenvectors;
4. line score = negative mean pairwise Euclidean distance in the 3D embedding.

Across the same 17 current expanding-history targets, using 3,000 newly sampled random legal lines per target, E0016 obtained:

- mean future-winning-line percentile **0.6588**;
- **14/17** targets above the random median;
- one-sided sign-test p≈**0.00636** before search/multiple-testing correction.

This essentially reproduces E0012/E0013's reported ~0.657 and 14/17 result using an independent implementation and independently sampled comparator lines.

That is the strongest positive result in E0016.

## 5. Diffusion dynamics do not improve E0013

To test the stochastic-transport idea, E0016 replaced/traded the truncated spectral embedding for diffusion distance using heat-kernel weights `exp(-2*tau*lambda)`.

Current-regime mean winner percentiles were approximately:

- tau 0.1: 0.567;
- tau 0.25: 0.565;
- tau 0.5: 0.569;
- tau 1: 0.562;
- tau 2: 0.476;
- tau 4: 0.402;
- tau 8: 0.400.

None approaches E0013's ~0.659.

Simple convex mixtures of E0013 spectral coherence and tau=0.5 diffusion coherence monotonically improved as the diffusion weight was removed. Pure E0013 was best. The same occurred when mixing E0013 with raw-pair support.

Therefore the advanced diffusion analogy is scientifically useful as a tested operator, but it does not currently add incremental predictive information to E0013.

## 6. Important stage-specific conclusion

The new repo research is internally consistent with the Evolve result:

- graph/spectral methods do **not** solve candidate acquisition;
- candidate discovery remains the primary bottleneck;
- E0013's signal exists only at coalition ranking after a candidate universe is already frozen;
- hard morphology/pruning compounds exclusion risk;
- distribution-first HLR/VVD methodology is safer than point motifs, but the tested learned residuals still do not beat exact structural geometry reliably;
- fixed-K rescue can improve a weak core selector without creating absolute edge.

The most important synergy is therefore architectural rather than numerical: keep acquisition broad/probabilistic, then use E0013 only to rank coalitions inside the surviving universe.

## 7. What counts as the leading survivor

**Leading current Main survivor:** `E0013 PPMI spectral coalition coherence`.

Status remains `PROVISIONAL_SIGNAL`, not `BREAKTHROUGH`.

Why it survives:

- strongest current replay signal among tested graph operators;
- reproduced independently from the written formula;
- survives random-line and morphology-matched diagnostics in the repository;
- E0012 also reports a draw-order permutation diagnostic;
- E0016's diffusion extensions fail to explain away or improve it.

Why it is not a breakthrough:

- discovered after broad graph/model search;
- only 17 current targets;
- no genuinely prospective post-discovery result yet;
- no evidence it can rescue missing candidate coordinates;
- exact formulation failed to transfer positively into XTRA E0014.

## 8. Recommended next move

Do **not** evolve more candidate formulas against the same historical targets now. That would merely increase search exposure.

Instead:

1. freeze E0013 unchanged;
2. score the already-frozen 2026-08-28 shadow target after the result is known;
3. accumulate prospective coalition ranks over a preregistered window;
4. maintain acquisition and coalition scorecards separately;
5. if E0013 survives, only then evolve small residual additions around it using prospective-safe nested evaluation;
6. continue candidate-acquisition research through distribution-first/full-field probability and fixed-K rescue, but demand prospective matched-exposure evidence before calling any coordinate selector an edge.

## Confidence

High confidence that E0016 found **no validated candidate breakthrough**. High confidence in the numerical reproduction of E0013's current replay. Moderate confidence that E0013 is a worthwhile prospective shadow lane. Low confidence that it represents a durable non-random lottery edge until future frozen targets accumulate.