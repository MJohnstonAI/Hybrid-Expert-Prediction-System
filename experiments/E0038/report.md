# E0038 — Latest-draw update and HEPS backtest

**Review date: 2026-11-05. Evidence: INSUFFICIENT_EVIDENCE. Status: experimental.**

The ledgers are complete through 2026-11-03. The new six-draw block does **not** establish better future prediction matches. Candidate acquisition remains the first binding failure. No predictive model or architecture change is promoted.

## Data update

Six rows were appended to each ledger, taking both from 39 to 45 active-era draws. All original ledger bytes were preserved. There are no missing Tuesday/Friday dates between 2026-06-02 and 2026-11-05; the latest completed draw is 3 November.

| Date | Main | PB | XTRA | PB |
|---|---|---:|---|---:|
| 2026-10-16 | 15,33,38,42,49 | 4 | 13,33,34,35,47 | 11 |
| 2026-10-20 | 1,18,21,41,47 | 5 | 3,8,18,37,39 | 13 |
| 2026-10-23 | 2,4,6,40,45 | 5 | 14,19,21,31,50 | 6 |
| 2026-10-27 | 3,4,5,38,48 | 3 | 5,15,32,33,34 | 13 |
| 2026-10-30 | 7,9,21,27,30 | 8 | 6,24,29,36,37 | 2 |
| 2026-11-03 | 13,15,32,34,43 | 12 | 1,7,10,16,24 | 15 |

Sources: [Main archive](https://www.lottery.co.za/powerball/results/2026), [XTRA archive](https://www.lottery.co.za/powerball-xtra/results/2026), [combined archive](https://www.powerball.net/southafrica/results/history/2026), corroborating [Main results](https://za.national-lottery.com/powerball/results) and [XTRA results](https://za.national-lottery.com/powerball-xtra/results). These are public result archives, not the official operator. Official National Lottery Main and configured XTRA endpoints returned 403. XTRA remains pending official verification under its existing manifest exception. Machine/method are unknown for all appended rows. Main training mixes recorded mechanical, electronic RNG and unknown rows; no machine-specific inference is made.

## What “blind” means here

For each target, only its prior 39–44 draws enter fitted state. Forecast parameters, baskets and portfolios are serialized and hashed before the scoring step. Mutation of target and future outcomes leaves the forecast unchanged. Main and XTRA are fitted independently.

This audit was written after public results were available and inspected. It is a **target-excluded post-hoc replay**, not twelve genuinely pre-result paper-trading slates. It must not be added to the official frozen-slate record.

E0037 is separately identifiable: its unchanged code and protocol were committed on 14 October, before these six targets, with prospective start 16 October. Its results are delayed execution of that previously frozen algorithm. E0038 does not claim that a forecast artifact was saved on each historical draw date. E0037's frozen four-lane threshold and weights are unchanged; it remains a scoring-only monitor with zero slate authority.

## Architecture tested

The latest saved Main slate (9 October) uses E0030's adaptive uniform/frequency/recent5 mixture, top-marginal K13 and a 20-line Johnson four-plus-first portfolio. This audit reproduces that acquisition/portfolio membership structure using ascending coordinate ties. PPMI reordering of the same twenty lines does not alter their all-20 match counts and was not credited as a rank improvement.

The same mathematical comparator was fitted separately to XTRA; it is **not** a claim to reproduce XTRA's historical v35.3 pipeline. No E0026 slot-routed acquisition claim is made for marginal baskets. E0029 pattern triage was not hard-applied, and no oracle winner injection was used.

Four candidate arms were compared at exactly K13: incumbent point, its original same-field four-plus swap optimizer, cumulative frequency and recent5. Every basket enumerates all 1,287 legal lines. Each portfolio submits twenty unique lines; random same-basket and full-field controls use the declared single seed. These random realizations are descriptive; the exact null is the primary matched-exposure reference.

## Acquisition and ticket results

| Lane / K13 arm | Winning coordinates retained / 30 | Targets with <=1 retained / 6 | Targets with >=3 / 6 | Targets with >=4 / 6 | All 5 / 6 |
|---|---:|---:|---:|---:|---:|
| Main incumbent | 7 | 5 | 1 | 0 | 0 |
| Main same-field four-plus | 7 | 5 | 1 | 0 | 0 |
| Main frequency | 9 | 3 | 1 | 0 | 0 |
| Main recent5 | 8 | 3 | 0 | 0 | 0 |
| XTRA comparator | 4 | 5 | 0 | 0 | 0 |
| XTRA same-field four-plus | 4 | 5 | 0 | 0 | 0 |
| XTRA frequency | 7 | 3 | 0 | 0 | 0 |
| XTRA recent5 | 5 | 5 | 0 | 0 | 0 |
| Exact random-K13 expectation per lane | 7.8 | 3.666 | 0.618 | 0.0786 | 0.00364 |

The four-plus optimizer made zero swaps on all twelve targets. Changing this compression objective therefore did not rescue acquisition on this field.

Main incumbent K13 hits by date: **1,1,0,3,1,1**. Its Johnson portfolio achieved one 3-match line among **120 submitted lines** (six sets of twenty), and zero 4- or 5-match lines. Its random same-K13 control had zero 3+ lines. XTRA comparator hits: **1,1,0,2,0,0**; both portfolio methods had zero 3+ lines among 120 each. Full-field random control had zero Main 3+ lines and one XTRA 3-match line among 120 per lane. No portfolio in these four acquisition arms produced 4+.

K20 is a separate diagnostic: incumbent retained 9 Main and 8 XTRA winning coordinates, versus 12 expected per lane. It provides no K13 improvement credit.

No incumbent K13 contained the full winner. Exact-winning-line ranking and pruning success are therefore unscoreable downstream. Even a perfect ranker cannot recover a coordinate excluded upstream. Zero 4+ tickets across such a small exposure is not itself surprising under the null.

## Probability-field and PB gates

Joint log-loss delta is model minus uniform, in nats/draw; **negative is better**. The incumbent lost slightly to uniform in both lanes:

| Model | Main mean delta | XTRA mean delta |
|---|---:|---:|
| E0030 incumbent | +0.003916 | +0.002630 |
| Cumulative frequency | +0.041113 | +0.056037 |
| Recent5 | +0.071249 | +0.116089 |
| E0037 repeat/anti-repeat RP | -0.025308 | -0.009343 |
| E0036 M1 | +0.018542 | +0.189042 |
| E0036 M2a | +0.087386 | +0.218472 |
| E0036 M2b | +0.014985 | +0.192812 |

All nine frozen E0037 forecasters, all comparators, Brier scores and descriptive SEs are reported in `results.json`. No model was hidden because it lost. Main M2a retained 13 winning coordinates but worsened proper score: precisely the sort of basket-only result that cannot earn predictive authority.

RP's favorable point estimates have descriptive SE 0.056796 Main and 0.015775 XTRA, larger than their respective improvements. It remains a monitoring lead, not a new selector. The existing low-shrinkage Main ball-bias forecasters were approximately neutral; they also do not establish an edge.

| E0037 frozen monitor | Final E | Maximum E including initial 1 | Required threshold |
|---|---:|---:|---:|
| Main five-number field | 0.938674 | 1.000000 | 80 |
| XTRA five-number field | 0.773001 | 1.000000 | 80 |
| Main PB | 0.519497 | 1.201382 | 80 |
| XTRA PB | 1.157698 | 1.157698 | 80 |

No evidence gate passed. All four Main PB strengths lost to uniform and had zero top-1 hits in six. All four XTRA PB strengths improved mean log score slightly and had the same one top-1 hit; those correlated variants are not four independent successes. XTRA PB remains a weak monitoring lead. Six draws cannot resolve a small durable advantage.

## Improvements supported by this work

1. **Make validation windows explicit.** The E0035 regression test read the growing live ledger while asserting a 30-row September snapshot. The test now supplies only the original through-11-September prefix. Historical experiment files remain unchanged.
2. **Preserve forecast-before-score evidence.** The new reusable harness records prefix hashes, source-code/protocol hashes, full model parameters, baskets and portfolios, then scores targets. The verifier checks all twelve forecasts against unchanged E0037 code and tests target/future mutation. This is code reproduction, not an independent model implementation.
3. **Prioritize probability information over more compression/ranking changes.** The incumbent probability field fails the proper-score gate and its four-plus objective makes no changes. Do not select the better-looking frequency basket, M2a basket or PB strength after seeing these six outcomes.
4. **Continue the frozen E0037 monitor without reweighting.** RP and XTRA PB can accumulate evidence under their existing weights. No new feature family, K expansion or retuned threshold is justified by this block. At the declared 100-target futility checkpoint, review power and information adequacy; no promotion now.
5. **Retain exhaustive enumeration and accepted Johnson geometry.** Reproduced 788/1,287 conditional 4+ coverage at twenty lines. This is deterministic geometry, not evidence of better future winning-number forecasts. It cannot solve upstream exclusions.

No new predictive architecture can honestly be presented as better from this sample. The useful improvement is a reproducible evidence trail and removal of a live-data dependency from historical regression testing.

## Artifacts and reproduction

- `data_update_receipt.json`: sources, ledger hashes, additions and date-completeness checks.
- `protocol.md`: pre-evaluation specification, scope, exposure and authority.
- `forecasts/`: twelve serialized target-excluded forecasts, clearly labelled replay.
- `results.json`: complete metrics, per-target outcomes and e-process paths.
- `verification.json`: temporal isolation, source-code reproduction, legal portfolios and prefix preservation.
- `structural_null_before_new_block.json`, `stationarity.json`, `null_simulation.json`: controls.
- New `cycles/<date>/post_draw/e0038_*_replay.json`: result scores and forecast pointers. No historical `pre_draw` files changed.

Commands: `python experiments/E0038/update_ledgers.py`; `python experiments/E0038/replay.py`; `python experiments/E0038/verify.py`; the validation commands in AGENTS.md; `python -m unittest discover -s tests -v`. On this Windows sandbox set TEMP and TMP to a writable workspace directory for the temporary-file test.

The first full test run exposed the stale historical cutoff and a sandbox temporary-directory permission error. Final validation status is recorded in `validation.md`; the original failure log is retained rather than erased.
