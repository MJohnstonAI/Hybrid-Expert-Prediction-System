# HEPS Aggressive Expert Lab - 2026-07-10

## Outcome

This experiment found one useful discovery candidate but no validated
predictive improvement. A 20-line union of two complementary blended experts
reached 3 main numbers on two historical targets. Its first genuinely unseen
holdout, 7 July 2026, failed with only one main-number match.

The candidate remains paper-trading research only and does not replace the
accepted HEPS lane allocation.

## Data State

The canonical mechanical-era ledger now contains 11 draws from `2026-06-02`
through `2026-07-07`. The 7 July result was confirmed by two independent result
histories before being appended through `scripts/append_draw.py`:

- main numbers: `16, 18, 21, 29, 47`;
- PowerBall: `11`;
- macro-sum: `131`;
- machine: `SIZWE`.

## Algorithms Tested

The lab evaluated 12 base main-number experts, six fixed synergy experts, five
PowerBall experts, and three orchestration families:

- recency-shrunk Bayesian frequency and coordinate kernels;
- executable sorted-slot EWMA and sorted-slot trend experts;
- gap-shape echo projection;
- existing void, stiction, pair, residue, midfield, and high-register features;
- online Hedge score averaging;
- line-level specialist allocation;
- a two-tier hot/high plus structural-synergy union.

Every historical target used only earlier rows. The online ensemble updated its
weights only after scoring each target.

## Main Findings

| Path | Lines/game | 2+ games | 3+ games | 4+ games | Same-line 3+PB |
|---|---:|---:|---:|---:|---:|
| Online score-average ensemble | 10 | 1 | 0 | 0 | 0 |
| Documented specialist allocation | 10 | 2 | 0 | 0 | 0 |
| Orthogonal specialist allocation | 10 | 2 | 0 | 0 | 0 |
| Dual-synergy coverage core | 10 | 5 | 0 | 0 | 0 |
| Dual-synergy expansion | 20 | 5 | 2 | 0 | 0 |

The score-average ensemble was the clearest failure: averaging incompatible
experts erased their specialist candidate pools.

The strongest standalone blends were:

- `structural_synergy`: midfield + sorted-slot EWMA + gap echo;
- `hot_high_synergy`: Bayesian hot frequency + high register;
- `hot_void_high_synergy`: Bayesian hot + void + high register.

Structural synergy and hot/high each found one 3-hit target, but on different
dates. Their full 20-line union preserved both events:

- 30 June: hot/high line matched `40, 42, 44`;
- 3 July: structural line matched `27, 32, 34`.

## Random and Multiple-Search Audit

For the 20-line union, a 20,000-trial target simulation was run separately for
each historical portfolio, preserving the generated lines' actual overlap. The
mean random 3+ game rate was approximately `6.18%`. Observing two or more 3+
games across the eight targets had an unadjusted portfolio-specific null tail
of approximately `8.33%`.

That is not statistically compelling, and it does not account for every model,
blend, and orchestration variant explored. All number-ranking paths had a
Bonferroni-adjusted probability of `1.0`.

## Genuine Holdout

The two-tier strategy was selected using rows through 3 July. The 7 July result
was located and verified only afterward, making it a useful unseen check:

- 10-line coverage core: best overlap `1`;
- 20-line expansion: best overlap `1`;
- PowerBall `11` was covered, but not with a qualifying main line;
- joint 3+ main plus PowerBall: `0`.

This failure is retained in the machine-readable report and materially weakens
the retrospective discovery.

## Prospective Paper-Trading Test

The hypothesis is frozen in
`outputs/predictions/prediction_slate_2026-07-10_dual_synergy.json`, generated at
the pre-draw timestamp recorded in that artifact from the 11-row ledger. It
contains a marked 10-line core and 20-line total expansion. It is an
experimental slate, not a production architecture change, and it must be scored
after the 10 July result is appended.

## Decision

Keep the lab, executable sorted-slot experts, and prospective slate as research
infrastructure. Do not merge the dual-synergy allocation or its weights into
the master architecture. Require prospective results and retain submitted-line
denominators before reconsideration.
