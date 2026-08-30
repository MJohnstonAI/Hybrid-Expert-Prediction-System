# E0011 XTRA Acquisition Power Budget

## Status

Methodology execution artifact. No predictive authority.

## Exact fixed-K null

For a target-blind fixed basket of `K` main numbers under the exact exchangeable 5/50 null, winner-coordinate overlap is Hypergeometric:

`H ~ Hypergeometric(N=50, K, n=5)`

Therefore:

`E[H] = 5K/50`.

At `K=13`:

- null mean = **1.30 winners/target**;
- null SD = **0.93993 winners/target**.

Basket composition cannot change this expectation under the exchangeable null. Candidate acquisition can outperform only if a reproducible non-exchangeable signal exists.

## Planning horizons

Using a one-sided `alpha=0.05`, target power `0.80`, normal approximation on mean overlap, one planned family comparison, and roughly two XTRA targets/week:

| Minimum true K13 lift | Alternative mean | Approx targets | Approx months |
|---:|---:|---:|---:|
| +0.10 | 1.40 | 547 | 62.9 |
| +0.15 | 1.45 | 243 | 28.0 |
| **+0.20** | **1.50** | **137** | **15.8** |
| +0.25 | 1.55 | 88 | 10.1 |
| +0.30 | 1.60 | 61 | 7.0 |

These are planning approximations, not proof thresholds. Paired comparisons may reduce variance; temporal dependence, adaptive model changes, and multiple testing may increase the required horizon.

## Binding interpretation

1. The default XTRA acquisition minimum effect of interest is **+0.20 winner coordinates/target at K13** until governance explicitly changes it.
2. The corresponding first-order resolution horizon is approximately **137 frozen prospective targets**.
3. A 20-target review is a **first-look/futility/calibration checkpoint only**. It is not a promotion threshold and must not be described as adequate power for a +0.20 effect.
4. Every new acquisition family must declare K, minimum effect of interest, family-wise testing exposure, and approximate target horizon before its first eligible target.
5. All candidate-basket comparisons must use identical K. Enlarging the union is exposure, not predictive lift.
6. The script `scripts/xtra_acquisition_power.py` is the canonical calculator for these planning values.

## Multiple-testing discipline

When more than one acquisition family is treated as confirmatory over the same target stream, the planning calculation must increase `family_tests` and use the script's Bonferroni planning adjustment unless a different preregistered correction is approved.

Exploratory shadows may continue in parallel, but they do not consume confirmatory alpha and cannot be promoted from the same exploratory sample without a fresh validation/prospective phase.

## Consequence for HEPS

HEPS XTRA is currently **data-starved rather than algorithm-starved**. A sequence-derived method is not authorized simply because it is mathematically novel. New candidate-acquisition research should identify a plausible source of non-exchangeability or incremental residual information before consuming scarce prospective targets.
