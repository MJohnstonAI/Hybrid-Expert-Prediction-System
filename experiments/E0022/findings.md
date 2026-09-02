# E0022 Findings — Oracle-K13 Assembly Evolution and Tie-Safe Ranking Audit

Evidence classification: `INSUFFICIENT_EVIDENCE`.

Paper trading only.

## Executive finding

E0022 did **not** discover a new predictive `BREAKTHROUGH` assembler.

The experiment did produce three durable outcomes:

1. **A deterministic portfolio improvement:** a `four_plus_first` Johnson objective covers more possible 4+/5 winning states than the historical `three_plus_first` objective at identical K13 and identical line budget.
2. **A Main robustness challenger:** `MAIN_ASSEMBLY_DISSENT_OR` materially reduces catastrophic winner burial in the retrospective oracle-K13 replay, especially on 2026-09-01, but does not beat E0013 on overall mean rank and is not statistically significant. It therefore enters prospective shadow only.
3. **A methodological correction:** the previously strong-looking XTRA raw-pair oracle result was materially inflated by optimistic treatment of ties. Average midrank removes the apparent lift. XTRA raw-pair assembly is not a predictive breakthrough in its current form.

## Main — what survived

### E0013 remains the strongest historical mean assembler, but recent evidence weakens confidence

Across 19 post-June Main oracle-K13 targets, E0013 spectral achieved mean winner percentile about `0.5904`.

However, on the two newest targets available to E0022:

- 2026-08-28: mean oracle winner percentile about `0.2453`;
- 2026-09-01: mean oracle winner percentile about `0.3265`;
- two-target mean about `0.2859`;
- Top-20 rate: `0`;
- Top-100 rate: `0`.

This does not erase the older discovery signal, but it is negative later-target evidence and must lower confidence.

### MAIN_ASSEMBLY_DISSENT_OR

Frozen E0022 challenger:

`max(midrank_percentile(frequency), midrank_percentile(recency), midrank_percentile(E0013_spectral))`

This is a bounded **OR robustness operator**, not a claim of three independent votes.

Across all 19 Main targets:

- mean winner percentile: about `0.5453`;
- minimum target mean percentile: about `0.2457`;
- Top-20 rate: about `0.0193`;
- Top-100 rate: about `0.1140`;
- targets above random median: `10/19`;
- one-sided sign p-value: `0.5`;
- one-sided t-test p-value: about `0.194`.

It therefore does **not** establish average predictive lift.

Its value is anti-burial robustness. On the two newest targets:

- 2026-08-28: about `0.2457`;
- 2026-09-01: about `0.8693`;
- two-target mean: about `0.5575`.

The 2026-09-01 rescue came largely from singleton frequency/recency information that E0013 spectral did not preserve. This motivates prospective shadow testing, not production authority.

## Main — what failed

Several intuitively attractive higher-order coalition strategies looked promising in earlier targets and then collapsed on the newest two:

- four-node nucleus: newest-two mean percentile about `0.1187`;
- conditional completion: newest-two mean percentile about `0.1449`;
- simple PMI: newest-two mean percentile about `0.1300`.

These current formulations are rejected for forward authority. Their failure is important: higher-order language does not create information when the active-era sample is too small.

## XTRA — tie-safe audit overturns the apparent raw-pair signal

E0014's historical oracle ranking used a strict-greater rank:

`rank = 1 + count(score > winner_score)`

For a discrete score, that gives every line tied with the winner the **best rank in the tie block**. This is optimistic.

On the original 16-target E0014 XTRA window, E0022 reproduced the effect:

- raw pair, optimistic best-tie percentile: about `0.6284`;
- raw pair, average-midrank corrected percentile: about `0.4591`.

Frequency was also inflated:

- optimistic: about `0.5537`;
- midrank corrected: about `0.4743`.

PMI changed less:

- optimistic: about `0.5268`;
- midrank corrected: about `0.5128`.

The continuous spectral score barely changed:

- optimistic: about `0.4768`;
- midrank corrected: about `0.4762`.

On the expanded 19-target XTRA replay, no tested assembler established lift:

- raw pair: about `0.4619`;
- PMI: about `0.5061`;
- spectral: about `0.4690`;
- frequency: about `0.4727`;
- recency: about `0.4933`.

Therefore no XTRA predictive coalition model is promoted from E0022.

## Johnson evolution — deterministic high-order coverage gain

For K13 there are exactly:

`C(13,5) = 1,287`

possible winning five-number states.

Each submitted five-number line covers 41 states at the 4+/5 threshold: itself plus the 40 lines that differ by one coordinate.

The historical Johnson implementation prioritizes new 3+ coverage before 4+. E0022 adds an optional `four_plus_first` objective because 3+ coverage saturates quickly and the director's objective is to maximize high-order same-line matches.

At identical K13 and line budget:

- budget 10: legacy 4+ coverage `30.61%`; four-plus-first `31.86%`;
- budget 20: legacy `58.82%`; four-plus-first `61.23%`;
- budget 30: legacy `79.18%`; four-plus-first `80.73%`.

Against random distinct lines, four-plus-first 4+/5 coverage is approximately:

- 10 lines: `31.86%` vs random expectation `27.74%`;
- 20 lines: `61.23%` vs `47.92%`;
- 30 lines: `80.73%` vs `62.56%`;
- 50 lines: `97.20%` vs `80.81%`.

This is a **provable combinatorial coverage improvement**, not a predictive probability improvement.

Exact 5/5 coverage remains `M/1287` for any `M` distinct submitted lines unless a valid predictive ranker supplies non-uniform winning-state probabilities.

## Research interpretation

The strongest near-term assembly architecture is therefore not a single magical coalition score.

For Main:

`frozen K13 -> enumerate all 1,287 lines -> E0013 + Dissent-OR shadow diagnostics -> fixed line budget -> optional four-plus-first Johnson coverage`

For XTRA:

`frozen K13 -> enumerate all 1,287 lines -> no promoted predictive coalition ranker -> four-plus-first Johnson geometry may still be used as non-predictive portfolio optimization`

The next prospective question is whether the Main Dissent-OR reduces catastrophic burial on actual frozen K13s without degrading average exact-winner rank. Until that happens repeatedly, its status remains shadow only.
