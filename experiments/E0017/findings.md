# E0017 Findings — Initial Red-Team Audit

## Bottom line

The supplied Gemini post-draw claim does not currently qualify as HEPS predictive evidence.

The broad candidate result (36 mains + 11 PBs) is weak at that exposure: a random K36 contains all five mains about 17.79% of the time, and a random K11 contains the PB 68.75% of the time; joint capture is about 12.23%.

The potentially important claim would be the stated 4/5 capture inside the 12-number spectral Primary Tier. Independent implementation of the written formula using XTRA-only history through 2026-08-25 does not reproduce it.

### Spectral reproduction

Using weighted pair-frequency adjacency, normalized Laplacian, the three smallest positive eigenvectors, and `sum(abs(v_k(i))/lambda_k)`, the Top12 is:

`36,1,23,26,22,17,7,18,19,4,3,12`

This captures only `3,4` = 2/5.

Using the prompt's contradictory "unweighted" wording as binary ever-cooccurred adjacency gives:

`36,1,26,22,41,18,17,4,23,43,12,19`

This captures only `4` = 1/5.

Thus the claimed spectral Primary Tier `3,4,16,35` is not reproduced under either natural interpretation.

### Gap residual contradiction

Under the standard recurrence-gap definition, only four coordinates satisfy `R>=1.20`: `3,16,40,32`.

More importantly, number38 had appeared only once in the post-June XTRA ledger before the target, so completed recurrence intervals do not provide a defined mean and standard deviation for38. The claim that38 had `R_i>=+1.20` therefore requires an unstated smoothing/fallback rule, extra history, or post-hoc construction.

### PB contradiction

From current PB16, completed first-order successors in the active XTRA history were only16 and10. PB15 is not a first-order Markov successor from16 in the available sample. The external prompt says to combine Markov probability with "modular recurrence gap decay" but supplies no formula, weight, normalization, or tie-break, so PB15 cannot be independently reproduced as the top attractor.

### Target leakage

The supplied prompt itself explicitly names the realized target numbers as intended outcomes: `03,04,16,35`, `38`, and PB15. Unless an identical timestamped pre-draw prompt/output exists, these clauses constitute direct target leakage.

## Scientific disposition

- Reject retrospective predictive credit for the supplied 2026-08-28 success claim as currently documented.
- Preserve the mathematical idea as a clean derivative audit only.
- Require target-independent implementation and blind expanding-history/prospective freezing before judging spectral centrality or gap-residual acquisition.
- Do not increase XTRA production authority or alter Richardson/E0015 from this claim.
