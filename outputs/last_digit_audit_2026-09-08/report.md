# Main last-digit audit — 8 September 2026

Evidence classification: **INSUFFICIENT_EVIDENCE**. Architecture status: experimental. No predictive authority or pipeline changes.

There is an interesting chronological concentration in absolute Main digit-sum changes of 11–13, already tracked in HEPS E0028. This audit supports continued prospective testing, not an established prediction improvement.

## Workbook integrity

The original workbook contains 24 draws, uniquely matched by five sorted-slot terminal digits plus PB terminal digit to canonical Main dates 16 June–4 September 2026, newest first. It is not the complete active ledger: 2, 5, 9 and 12 June are absent. All 24 G formulas included F, the PB digit. The source was preserved during analysis; following the user's subsequent instruction, G2:G25 was changed to SUM(Arow:Erow). All formulas and cached totals were verified, as were unchanged other cell contents and styles. All other ZIP members were byte-identical. Native renderer failed at Vulkan initialization; no visual/native Excel runtime verification was available.

The original checksum and row mapping are retained in results.json; rerunning analyze.py after the authorized correction will naturally describe the corrected file. The existing results.json intentionally records the original audit.

## Findings

- Workbook Main digits: counts for 0–9 are 16, 9, 12, 10, 17, 9, 11, 15, 7, 14 (120 digits). Under uniform legal 5/50 geometry each digit has expected total 12 here, but sorted-slot digit probabilities are unequal. Digit 4's observed lead does not establish a predictive edge.
- Corrected sum average is 22.042 and standard deviation 6.125, versus exact random expectations 22.5 and 6.155. Central concentration is ordinary lottery geometry and provides no evidence to favor individual central-sum lines.
- Lag-one sum correlation is -0.436 in the workbook and -0.388 across the full ledger. Searching lags 1–5 gives permutation-adjusted p approximately 0.190 and 0.109 respectively. No convincing periodicity was detected by this bounded test.
- Absolute changes 11–13 occur 11/23 workbook transitions (47.8%) and 12/27 canonical transitions (44.4%). Exact independent-draw unconditional probability is 10.94%. Conditional on each observed previous sum, expected counts are 2.611 and 2.985 respectively.
- A 20,000-permutation chronology test, conditioning on the observed sum histogram and correcting for all 44 contiguous three-wide delta bands, gives approximate p=0.00145 for the workbook and 0.00280 for the ledger. This is a notable discovery anomaly. It does not correct for every historical HEPS feature/window/threshold search or demonstrate future persistence. The datasets overlap and are not independent replications.
- E0028 already selected 11–13 retrospectively through 1 September. The 4 September change from 15 to 26 adds one previously frozen success. It is the same observation, not a new independent confirmation. Hard filtering on this band would have discarded 15 of the 27 historical winning lines.

## Sequential probability replay

First eight prior draws initialize each model. Each target is excluded from fitting; all choices remain discovery-only because outcomes and prior research existed when the audit was designed. Exact null enumerates all 2,118,760 legal Main lines. Sum probabilities are converted to a coherent full-support line field by allocating each sum's probability uniformly among its legal lines. Positive gain means lower log loss than uniform legal lines, in nats per draw.

| Model | Workbook: 16 targets | Full ledger: 20 targets |
|---|---:|---:|
| Shrunk historical sum frequency | +0.0850 | -0.0479 |
| Shrunk latest-eight sum frequency | +0.1564 | +0.0578 |
| Previous-sum category model | +0.1276 | +0.0433 |
| Adaptive absolute-change residual | +0.1405 | +0.1233 |

The adaptive model leads on the full ledger, but only 12/20 targets improve over null. Its paired gain standard deviation is 0.573 nats; a rough independent-normal 95% interval for average gain is -0.128 to +0.374, before multiplicity/dependence correction. No statistically reliable improvement is established. This approximate interval is diagnostic, not confirmatory inference.

Slot digit-frequency fitting worsens average marginal log loss on both samples. Previous-same-slot-digit conditioning worsens the workbook result and improves the full ledger by only 0.00163 nats per digit. Marginal scores are not multiplied into joint evidence.

Search exposure: two overlapping samples; four sum models; two slot models; five autocorrelation lags; 44 three-wide LDSAD bands; fixed shrinkage 20, warm-up eight, recent window eight, sum categories <=17/18–27/>=28, and declared seeds. No variants were retuned after their results. Historical E0028/E0029 search adds unquantified exposure.

## HEPS implication

Continue the existing E0028 frozen band diagnostic and consider independently reviewing this smooth adaptive sum-change model. A hard band is unsuitable: even this unusually favorable historical sample loses more than half the actual winning lines. Any practical ranking use belongs after K13 freeze unless upstream authority is earned separately. A sum feature cannot identify which of five same-terminal-digit coordinates is the winner, and it is not independent evidence from other transforms of the same numbers.

Before operational use: freeze a specific model, score fresh targets against exact null and simple/incumbent controls, retain full support, measure incremental value, and seek independent reproduction. No matched-K acquisition or downstream incumbent comparison was performed here, so no K13, E0029, or portfolio improvement is claimed.

At a minimum effect of 0.02 nats/draw and observed paired SD 0.573, an independent-normal approximation suggests roughly 6,400 fresh targets for 80% power at two-sided 5%, before multiplicity/dependence adjustments. This rough planning number illustrates why 20 replay targets cannot reliably resolve a small edge; it is not a validated sample-size prescription.

Ledger and manifest checks passed (28 draws); stationarity audit reports 15 mechanical-labelled and 13 unknown-method rows with mixed machine identities. No physical mechanism is inferred. The repository random-null validation ran 100,000 trials with its mandated seed. Exact slot/sum controls were independently constructed by enumeration in analyze.py.

Sources: user workbook; data/draw_history.jsonl; data/draw_manifest.json; governance/current_method_doctrine.md; governance/nomenclature.md; experiments/E0028/protocol.yaml and decision.md; experiments/E0029/decision.md; core/heps_architecture.md. Results and reproducible code are adjacent to this report.
