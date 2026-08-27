# E0013 — Positive-PMI Spectral Coalition Ranking

## Status

`PROPOSED PROSPECTIVE SHADOW`

Evidence classification: `PROVISIONAL_SIGNAL`

Paper trading only.

## Origin

Derived from the Gemini SGCE idea after E0012 showed that raw/Jaccard spectral coordinate selection did not improve candidate acquisition, while a residual positive-PMI spectral graph showed exploratory line-ranking signal.

All retrospective discovery evidence is hypothesis-generation only. First prospective scoring begins with the already-frozen 2026-08-28 Main K13, without changing its candidates or submitted portfolio.

## Hypothesis

Conditional on an identical frozen candidate universe, a spectral graph built from positive residual pair association can rank the true five-number coalition above matched random/simple coalition rankers more often than chance.

The proposed expert has **zero candidate-discovery authority**. It acts only after K is frozen.

## Frozen graph definition

For prior Main draws only:

- `N` = number of prior draws.
- `C_i` = draws containing coordinate i.
- `C_ij` = draws containing both i and j.
- pair adjacency:

`A_ij = max(0, log(((C_ij + 0.5) * N) / ((C_i + 1) * (C_j + 1))))`, with `A_ii=0`.

Compute normalized Laplacian:

`L = I - D^(-1/2) A D^(-1/2)`.

Take the three eigenvectors corresponding to the three smallest strictly positive eigenvalues as the 50-node embedding.

For legal line C of five coordinates, score:

`S(C) = - mean_{i<j in C} ||u_i - u_j||_2`.

Higher score = stronger coalition coherence.

No target-dependent tuning is permitted.

## Baselines

- random ordering within the same frozen candidate universe;
- raw historical pair-count coalition score;
- simple smoothed pair-PMI score without spectral projection;
- additive simple frequency line score;
- incumbent frozen HEPS line ordering when available.

## Primary metrics

Conditional on all five actual winners surviving the frozen universe:

- exact winning-line rank among `C(K,5)` combinations;
- winning-line percentile;
- Top-100 / Top-20 survival;
- paired rank improvement versus baselines.

When 5/5 candidates do not survive, record acquisition failure separately and do not blame or credit E0013.

## Falsification

Downgrade/reject if prospective winner percentile does not exceed matched random/incumbent ranking over the preregistered review window, or if the signal disappears after expert-redundancy/frequency controls.

## Authority

Diagnostic/shadow ranking only. No candidate addition, removal, pruning or portfolio alteration from retrospective evidence.