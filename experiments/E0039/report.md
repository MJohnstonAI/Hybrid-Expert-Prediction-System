# E0039 — Can decade patterns, VVD or initial K13 improve prediction?

**2026-11-05 — INSUFFICIENT_EVIDENCE / experimental / paper trading only.**

I implemented and tested a finite set of these ideas. None establishes improved Main prediction. There is a limited XTRA decade-selection lead, but its full-line probability model fails the primary proper-score test over the complete window. Do not promote it or tune it on these outcomes.

This is a negative result for the exact specifications tested, not proof that every possible decade or movement model must fail.

## Experiment

Each lane has 45 draws. Using the first six as initial history gives **39 expanding-window targets per lane**, with no target/future row in its own forecast. All 78 forecasts were saved before the scoring step. Main and XTRA fitted state never transfers.

All outcomes were already available, including the six recently added draws: **post-hoc replay**, not an untouched holdout or prospective trial. The last-six view is diagnostic only. Main history mixes recorded mechanisms/machines; XTRA retains pending official-source verification flags. Neither ledger changed during E0039.

Five models plus one fixed mixture were declared before evaluation, with one shrinkage concentration (20), one decade definition (1–10, 11–20, 21–30, 31–40, 41–50), fixed movement bins and no parameter search:

1. **GROUP:** learn occupancy shapes such as 2+2+1, without specifying which decades.
2. **SHELL:** learn the full five-decade count vector, with exact combinatorial shrinkage.
3. **SHELL_TRANS:** predict that count vector conditional on the previous draw's occupancy shape, shrinking toward SHELL.
4. **VVD_RESIDUAL:** learn whether absolute sorted-slot movements exceed their exact random-draw expectations, using four bins.
5. **SIGNED_RESIDUAL:** seven signed movement bins, retaining direction and magnitude as one information family.
6. **SAFE_MIX:** fixed 50% uniform plus 10% of each model. The name describes a uniform probability floor, not proven predictive safety.

All distributions have full legal-line support and are normalized. VVD and signed displacement are alternatives, not multiplied independent votes. Transition fields retain slot marginals; their top-marginal K13 is a benchmark and is not labelled E0026 routed acquisition. E0023's downstream-only authority is unchanged: these are new experimental full-field models, not an upstream promotion of that expert.

## Main results

Joint log-loss delta is model minus uniform; **negative is better**. K13 capture counts are out of 195 winning coordinates across 39 targets; random K13 expectation is **50.7**.

| Model | Mean log-loss delta | Descriptive SE | K13 coordinates retained |
|---|---:|---:|---:|
| Group shape | +0.05294 | 0.04147 | 54* |
| Decade-specific occupancy | +0.51788 | 0.10446 | 49 |
| Occupancy transition | +0.75806 | 0.11955 | 51 |
| VVD residual | +0.08632 | 0.04888 | 48 |
| Signed movement residual | +0.17829 | 0.07714 | 45 |
| Half-uniform mixture | +0.08351 | 0.02637 | 39 |
| E0030 incumbent | +0.00157 | 0.00162 | 45 |
| Simple frequency | +0.04584 | 0.03929 | 49 |
| Recent five draws | +0.00969 | 0.01949 | 51 |
| Uniform | 0 | 0 | 54* |

*GROUP is symmetric across decades and within decades. Its coordinate marginals are exactly 0.1 for every number, so its K13 is the **same random tie-control basket as uniform**, not evidence of predictive candidate ranking.

All five new fields and their mixture lost joint log score to uniform on Main. Their coordinate Brier scores were also no better than uniform. No model gains authority because of an isolated 4/5 basket. On the newest six Main targets, every new field again lost joint log score; the mixed field produced one 4/5 basket but had worse probabilities and poor whole-window capture.

## Why same-decade patterns look convincing

The exact random 5-of-50 distribution already has:

| Decade group sizes, ignoring decade labels | Chance probability |
|---|---:|
| 2+1+1+1 | 42.4777% |
| 2+2+1 | 28.6724% |
| 3+1+1 | 16.9911% |
| 3+2 | 5.0973% |
| 1+1+1+1+1 | 4.7197% |
| 4+1 | 1.9823% |
| 5 | 0.0595% |

Thus **95.2803% of random draws contain a same-decade pair**. Recognizing that pattern does not establish an advantage. A useful model must predict which group configuration/decades will occur better than these baseline rates, and ultimately which numbers within them.

Even perfect knowledge of an unlabelled occupancy shape leaves every individual number equally likely by symmetry. It can change joint grouping or basket-tail probabilities, but it cannot rank individual numbers. The implemented GROUP field failed to improve full-line probability anyway.

## K13 selection: exact allocation test

For each SHELL and SHELL_TRANS forecast, I exhaustively evaluated all **2,305 legal allocations of 13 seats across five decades**, with no decade receiving more than ten. Exact conditional hypergeometric calculations give the whole 0–5 hit distribution. Four objectives were tested, each at fixed K13:

- maximize expected winning coordinates;
- maximize probability of at least four;
- maximize all-five containment;
- minimize zero/one-hit catastrophes.

Within a decade these models cannot distinguish its ten numbers. Tied coordinates use the same predeclared seeded permutation; the allocation objectives use deterministic allocation ties. These are global optima **under the fitted shell model**, not guarantees about the next draw.

| Field / K13 objective | Main total hits /195 | XTRA total hits /195 | Main 4+ targets /39 | XTRA 4+ targets /39 |
|---|---:|---:|---:|---:|
| SHELL mean | 49 | 58 | 1 | 0 |
| SHELL four-plus | 44 | 51 | 0 | 2 |
| SHELL all-five | 45 | 57 | 0 | 3 |
| SHELL avoid catastrophe | 49 | 50 | 0 | 0 |
| SHELL_TRANS mean | 52 | 54 | 0 | 1 |
| SHELL_TRANS four-plus | 43 | 56 | 1 | 0 |
| SHELL_TRANS all-five | 47 | 51 | 0 | 2 |
| SHELL_TRANS avoid catastrophe | 48 | 53 | 0 | 1 |

No allocation arm contained all five winners on any target. The exact random-K13 expectation is 50.7 total hits and about 0.511 four-plus targets per 39. Several XTRA tail counts look interesting, but they come from eight related allocation arms plus multiple fields/windows, not one untouched test. Those counts do not repair the models' worse full-line probabilities.

Changing objectives shifts risk: optimizing all-five or four-plus can sacrifice average capture. The Main four-plus allocation arms actually captured fewer total winning coordinates than their mean-hit counterparts. An optimizer cannot create information absent from its input field.

## XTRA: a limited lead, not an improvement claim

| Field | Mean log-loss delta, all39 | Mean delta, last6 |
|---|---:|---:|
| GROUP | +0.02563 | +0.06841 |
| SHELL | +0.23401 | -0.15815 |
| SHELL_TRANS | +0.46221 | +0.24604 |
| VVD_RESIDUAL | +0.13061 | +0.10262 |
| SIGNED_RESIDUAL | +0.23203 | +0.53210 |
| SAFE_MIX | +0.03632 | -0.02045 |
| Incumbent comparator | +0.00221 | +0.00263 |

The SHELL mean-allocation basket captured **58 versus 50.7 expected** over 39 targets and had 18 zero/one-hit catastrophes. SHELL's coordinate Brier delta was slightly favorable (-0.000025), suggesting a possible coarse marginal signal, but its joint log score was materially worse (+0.23401). It modestly improved on the last six targets only; that subwindow is already known and cannot rescue a full-window promotion.

If further research is desired, the specific unresolved question is whether a **lower-dimensional decade-rate model** can preserve that weak marginal effect without estimating 126 sparse shell probabilities. That model was not tested here, and is not a recommendation to alter K13. It would need a new fixed protocol and fresh targets, not tuning to this report. XTRA evidence cannot be transferred to Main.

## Additional mathematical repair

E0037's F020 note proposed centering a transition basis by subtracting its exact structural expectation given the previous draw. For a normalized exponential model, subtracting a quantity depending only on history cannot change predictions:

`exp(theta*(f(x,p)-c(p))) / sum_y exp(theta*(f(y,p)-c(p)))`

is exactly

`exp(theta*f(x,p)) / sum_y exp(theta*f(y,p))`.

The common factor cancels. Thus that centering alone cannot fix a coordinate-height/tail-band collapse. This does not invalidate F020's observed failure; it corrects the proposed sufficient repair. The identity was verified numerically. A genuine successor must change the estimator, outcome-dependent feature space or regularization, then pass proper scores. E0039's observed-versus-expected residual estimator is such a distinct attempt; it also failed to establish predictive lift.

## Decision and useful improvements

- **Do not promote these methods for Main.** None beats uniform on primary joint proper score in the full or latest-six window.
- **Retain exact decade-null and K13-allocation infrastructure.** It exposes grouping base rates and makes K13 tradeoffs measurable without heuristic optimization errors.
- **Retain slot provenance and target-excluded scoring.** Never revive independent HLR×VVD products or call a common grouping pattern a predictive expert.
- **Correct the centering-repair interpretation.** It is a mathematical no-op in this normalized model and should not be offered as a solution.
- **Treat the XTRA marginal finding as a question for fresh research only.** Do not select it because it is the most attractive result among many searched comparisons.

No model was retuned, no ledger or old experiment was overwritten, and no production/expert authority changed. Current E0037 monitoring remains untouched. A future confirmatory experiment requires a frozen selection rule, multiplicity-aware sequential gate, adequate power and independent review.

## Reproduction and limitations

Run `python experiments/E0039/research.py` and `python experiments/E0039/test_research.py`.

Seven focused verification tests passed. They include exhaustive enumeration of all **2,118,760 legal lines** for both non-flat movement fields' normalizers and slot marginals; small-universe brute-force validation of allocation hit distributions; exact uniform recovery; GROUP symmetry; target/future mutation isolation; and all 78 forecast hashes and K13 sizes. Existing shared model code was not modified. Data validation and manifest checks passed; unchanged E0038 stationarity and 100,000-trial null controls remain applicable to the same ledger hashes.

`results.json` reports every model, allocation arm and declared window, including losses and descriptive SE. `forecasts.jsonl` contains all pre-score parameters and baskets, explicitly labelled replay. `protocol.md` records the finite search exposure. `test_log.txt` records verification.

E0039 uses seeded ties and 12-decimal tie grouping; E0038 used ascending numeric ties. Candidate counts can therefore differ for tied fields between reports (notably XTRA incumbent 3 versus 4 in the last six). Probability scores are unchanged. No historical basket or official prediction record is rewritten.

All results remain post-hoc and exposed to the extensive HEPS search history. The 39-target comparison does not establish a reliable future edge, and negative findings do not prove exact absence of a small effect. There is currently no evidence-backed replacement selector to install.
