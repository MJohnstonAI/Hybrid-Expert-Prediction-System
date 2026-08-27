# E0015 Findings — Discovery Freeze

Evidence classification: `PROVISIONAL_SIGNAL`.

## Discovery result

E0014 found that the strongest tested XTRA PowerBall probability model was not exact-state recurrence alone and not VVD/HLR recurrence alone. A shrinkage-weighted geometric pool of the two distributions at `tau=4` produced the best aggregate calibration:

- convergence tau4 log loss: **2.6600**;
- uniform: **2.7726**;
- simple global frequency: **2.8726**;
- exact-state tau4 alone: **2.7568**;
- VVD+HLR tau4 alone: **2.8437**.

The convergence model also produced **4/16 Top-1 hits** and mean exact rank **7.5**.

## Interpretation

This is compatible with the HEPS PowerBall doctrine:

`direction distribution -> VVD distribution -> exact-state transition -> legal exact-ball translation -> residual convergence`.

The result does **not** establish that the components are statistically independent. The geometric pool is therefore treated as a calibrated ensemble operator, not as multiplication of independent evidence.

## Strongest counterarguments

1. Only 16 expanding-history targets were available.
2. Tau4 was selected after comparing tau4 and tau8 plus several component variants.
3. The active XTRA PB process may be nonstationary or the 4 Top-1 hits may be concentrated in a small number of recurring states.
4. The comparison with the incumbent XTRA PB engine is incomplete because historical frozen cycles do not uniformly contain full 1..16 probability fields.
5. The current canonical XTRA ledger lags the latest provenance-qualified working cycle, preventing a clean E0015 target-specific freeze for 2026-08-28 without changing data provenance rules.

## Required next evidence

Freeze the tau4 formulation unchanged. For each eligible future XTRA target, store the complete 1..16 distribution before the draw and score log loss, Brier, rank, Top1/Top3, direction and VVD rank against uniform, frequency and incumbent frozen PB fields.

No retrospective tuning from future results is allowed.
