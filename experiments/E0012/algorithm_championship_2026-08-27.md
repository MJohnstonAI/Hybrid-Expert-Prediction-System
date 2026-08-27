# E0012 Algorithm Championship — 2026-08-27

Evidence status: exploratory/post-hoc unless explicitly frozen prospectively below.
Canonical Main ledger cutoff: 2026-08-25, 25 draws.

## Objective

Test every operationally meaningful idea supplied in the Gemini contribution/report at the stage where it could plausibly add HEPS value. Distinguish candidate acquisition, regime routing, morphology/compression, coalition assembly and exposure management.

## 1. SGCE as candidate acquisition

The supplied Jaccard/eigenvector-row-norm implementation did not show acquisition lift in expanding-history replay across 17 targets:

- K10: 16 winner coordinates total; exact-null expectation 17; simple frequency also 16; recency 15.
- K13: 18 winners; exact-null expectation 22.1.
- K18: 25 winners; exact-null expectation 30.6.

Disposition: `INSUFFICIENT_EVIDENCE` for candidate-funnel authority.

## 2. Spectral graph as coalition assembly

Several pair/graph scores were compared by asking whether the future winning line ranked above matched random legal lines using only prior draws.

Raw pair counts, raw Jaccard and simple residual pair scores showed no edge. A positive-PMI spectral construction was materially different:

1. For each pair, form a smoothed positive pointwise-mutual-information adjacency
   `A_ij = max(0, log(((C_ij+0.5)*N)/((C_i+1)*(C_j+1))))`.
2. Compute normalized Laplacian `L = I - D^-1/2 A D^-1/2`.
3. Use the three smallest strictly positive eigenvectors as a node embedding.
4. Score a five-number line by negative mean Euclidean distance over its ten embedded node pairs; higher score means a more spectrally coherent coalition.

Exploratory results, minimum eight prior draws:

- future winning-line mean percentile versus matched random legal lines: ~0.657;
- 14/17 targets above the random median; one-sided sign p≈0.0064 before search/multiple-testing correction;
- morphology-matched control (same odd count, decade count, target sum ±10): mean percentile ~0.648; 13/17 above median; sign p≈0.0245;
- 300 draw-order permutation test: observed mean percentile ~0.657 versus permuted mean ~0.564; empirical p≈0.0133;
- oracle-K13 isolation test (actual five winners + eight random decoys, ranking all 1,287 5-of-13 lines): mean winner percentile ~0.620; 13/17 targets had mean percentile >0.5; sign p≈0.0245; Top-20 rate ~3.9%, Top-100 rate ~17.5% across random decoy universes.

Simple frequency and raw pair scoring were below the random median in the same oracle-K13 test.

This is the strongest Gemini-derived result found. It was discovered after testing several graph variants, so it receives no retrospective confirmatory credit. It warrants a separately frozen prospective shadow experiment.

Disposition: `PROVISIONAL_SIGNAL` as a coalition-only research lead; no candidate-pruning authority.

## 3. PCA/SVD latent regimes as prediction router

Two walk-forward three-cluster PCA/KMeans regime models were tested: raw sorted-coordinate states and an expanded state using coordinates, signed/absolute slot deltas and sum.

Raw-state regime model:
- next total-VVD MAE ~20.70 versus unconditional prior-mean baseline ~19.64;
- next-sum MAE ~25.59 versus baseline ~23.62.

Expanded-state regime model:
- next total-VVD MAE ~20.34 versus baseline ~19.79;
- next-sum MAE ~24.86 versus baseline ~23.69.

A direct Alpha/Beta-versus-Gamma style eigenspace cut retained 13/17 winners (76.5%) while retaining ~71.3% of legal lines on average; compression lift ~1.07, Poisson-binomial upper-tail p≈0.43.

Disposition: `INSUFFICIENT_EVIDENCE`.

## 4. Dynamic sum bounds

Walk-forward rolling-five-draw mean ± alpha*SD was evaluated against exact legal-line sum retention.

- alpha=1.0: winner retention 50.0%, legal-space retention ~50.96%, lift ~0.98, p≈0.63.
- alpha=1.5: winner retention 55.0%, legal-space retention ~67.26%, lift ~0.82, p≈0.94.
- alpha=2.0: winner retention 70.0%, legal-space retention ~78.10%, lift ~0.90, p≈0.90.

The PDF corridor [95,155] retains 64% of the 25 historical winners while retaining ~66.4% of the exact legal line space: lift ~0.96.

Disposition: no detected predictive edge; soft morphology only if retained.

## 5. Static parity/decade/gap filters

Gemini parity 2:3/3:2 + supplied decade spread + max adjacent gap <=25 retained 15/25 historical winners = 60%, versus exact legal-space retention ~54.88%; one-sided p≈0.38.

Disposition: `INSUFFICIENT_EVIDENCE`; useful only as an engineering/morphology challenger, not hard pruning.

## 6. VVD / slot-drift retention envelopes

A family of walk-forward signed-delta envelopes was tested.

At an 80% central empirical envelope:
- per-slot realized coverage ~70.6% versus average exact structural-null mass ~66.3%; lift ~1.07; p≈0.21;
- requiring all five target slots inside their envelopes retained 6/17 winning lines =35.3% while retaining ~23.4% of legal lines; lift ~1.51; p≈0.17.

This is suggestive but not significant and was part of a multi-width exploratory family.

A shrunk empirical VVD probability model also failed proper-score testing: at shrinkage beta=10, mean log loss ~3.215 versus `NULL_VVD_STRUCTURAL` ~2.924. Other tested shrinkages were also worse than the exact structural null.

Disposition: `INSUFFICIENT_EVIDENCE`; continue E0005/E0009 rather than promote an envelope veto.

## 7. Adaptive K

A prospectively computable exploratory controller used rolling-five macro-sum volatility terciles to select K13/K16/K18 and simple frequency ranking.

Across 17 targets:
- average K ~16.76;
- observed winner coordinates 25;
- matched null expectation from exposure 28.5.

No evidence that volatility-directed K expansion adds information. Increased K remains exposure management, not a predictive edge.

Disposition: `INSUFFICIENT_EVIDENCE`.

## 8. Core + Rescue at fixed K

A deterministic fixed-K test used frequency Core10 plus three `MAIN_STICTION_SHADOW`-style rescue seats (repeat, ±1, ±2 support) and compared it with frequency Top13.

Across 17 targets:
- frequency K13: 20 winner coordinates;
- Core10 + Shadow3: 22 winner coordinates;
- rescue version improved four targets, worsened two, tied eleven; paired non-tie sign p≈0.344;
- one target reached 4/5 versus 3/5 for the pure frequency basket.

However 22 hits is essentially the K13 exact-null expectation of 22.1 over 17 draws. The architecture-preservation idea may improve a particular core selector without yet creating an absolute edge.

Disposition: `INSUFFICIENT_EVIDENCE`, but continue E0007/E0009/E0011 fixed-K rescue.

## 9. Combined hard-pruning pipeline

A combined exploratory pipeline applied static morphology + rolling sum alpha=2 + 80% joint slot-drift envelope + PCA Alpha/Beta cut.

- winner retention: 2/17 = 11.8%;
- mean legal-space retention: ~10.16%;
- compression lift ~1.16; p≈0.54.

The combined suite therefore compounds catastrophic exclusions without detected disproportionate winner retention.

Disposition: `REJECT` as a hard integrated pruning architecture at current evidence.

## Overall synthesis

Most Gemini ideas do not currently add predictive information once structural geometry and exposure are controlled.

The important exception is **positive-PMI spectral coalition coherence**. Its signal appears in line/coalition ranking, not coordinate acquisition. It survives random-line, morphology-matched and draw-order permutation diagnostics, but was found through exploratory model search and has no untouched validation.

Action: create a separate prospective shadow experiment for the PPMI spectral coalition ranker. Do not alter the already frozen 2026-08-28 Main slate or K13.