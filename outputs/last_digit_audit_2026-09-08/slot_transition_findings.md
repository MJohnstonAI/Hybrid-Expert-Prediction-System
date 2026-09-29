# Does digit x follow digit y in slot z?

**No reliably predictive same-slot digit transition was established.** There are candidate patterns, especially S1 9 -> 6, but the available observations are too sparse to treat historical percentages as forecast probabilities. Evidence classification: INSUFFICIENT_EVIDENCE. Architecture status: experimental.

We tested all 500 possible one-step transitions (10 previous digits x 10 next digits x five sorted slots). Workbook data: 24 draws, 23 transitions per slot, 16 sequential evaluation targets after eight initialization draws. Canonical data: 28 draws, 27 transitions per slot, 20 evaluation targets. The samples overlap and do not supply independent confirmation.

## Most interesting repeated examples

| Rule | Full-ledger occurrences | Observed rate | Exact random next-digit baseline in that slot |
|---|---:|---:|---:|
| S1: 6 after 9 | 3/4 | 75% | 9.14% |
| S4: 0 after 9 | 3/4 | 75% | 9.29% |

These baselines are exact uniform legal 5/50 sorted-slot probabilities, not an assumption that each slot has ten equiprobable digits. S1 denotes the smallest winning Main number; S5 denotes the largest, not physical extraction order. Counts in the baseline column describe random geometry, not empirical transition forecasts.

Across 20,000 permutations of complete draw rows, the maximum standardized transition excess among all 500 cells had adjusted p approximately 0.464 for the workbook and 0.253 for the full ledger. Neither shows a compelling global departure from random chronology. For S1 9 -> 6 specifically, the full-ledger nominal permutation p is 0.0053, but its 500-transition maximum-statistic-adjusted p is 0.779. This illustrates the cost of looking for the strongest among many sparse patterns. The most extreme standardized cells overall had fewer than three antecedent occurrences; the displayed repeated examples require at least three. No broader historical-search correction is claimed.

## Prediction check

At each evaluation draw, predict next digit from earlier same-slot transitions only, shrinking counts with 20 observations' worth of exact slot-null prior. Compare with exact slot null and similarly shrunk unconditional digit frequency. All slots retain full digit support. No parameter tuning after results.

The conditional model's average gain over exact slot null is -0.00473 nats/digit in the workbook replay (slightly worse) and +0.00163 in the full-ledger replay (essentially unchanged). Full-ledger gains by slot: S1 +0.0554, S2 +0.0118, S3 -0.0071, S4 +0.0093, S5 -0.0612. The combined per-draw average gain SD is 0.0743 across 20 targets, giving a rough unadjusted independent-normal interval -0.031 to +0.034 nats/digit. This is discovery-only descriptive uncertainty, not prospective inference.

Conditional fitting beats the unconditional fitted-frequency comparator in four slots, but the latter is worse than exact null in all five. Beating a poor fitted comparator does not establish predictive value. Scores here are marginal digit scores, not joint line likelihoods.

## HEPS decision

S1 9 -> 6 is a reasonable explicitly named hypothesis to monitor on future occurrences, with all outcomes retained. The historical 75% must not be used as the next-draw probability. There is no supported reason yet to alter K13 membership, hard-exclude other digits, or promote a digit-transition expert. This conclusion concerns the tested one-step same-slot family; it does not prove that every conceivable digit-based model is impossible.

Reproduction: slot_transitions.py, slot_transition_protocol.md, and slot_transition_results.json in this directory. Source: original workbook row reconciliation in results.json and canonical data/draw_history.jsonl. Exact baseline: exhaustive enumeration from analyze.py. No source workbook, ledger, or pipeline changes were made during this follow-up.
