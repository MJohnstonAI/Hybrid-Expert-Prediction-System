# E0038 — Missing-draw update and target-excluded architecture audit

Declared 2026-11-05 before executing the evaluation. Role: quantitative tester and failure analyst.
Evidence classification: INSUFFICIENT_EVIDENCE. Architecture status: experimental. Paper trading only.

## Scope and evidence boundary

Append the six missing Tuesday/Friday results from 2026-10-16 through 2026-11-03 to Main and XTRA independently. Preserve every existing ledger byte. Main IDs remain local sequential IDs; XTRA IDs retain the public draw sequence. Public archives corroborate numbers; unknown machine/method remain unknown. XTRA retains the manifest's provenance-qualified exception and pending official verification because the configured official endpoint returned 403.

The analyst has seen the result sources. This newly written harness is therefore **post_hoc_replay**, not a genuinely blind prospective slate. Every forecast receives only the expanding prefix strictly before its target; write the complete forecast and hash before scoring. No fitting, threshold selection, or tuning may inspect that target or later rows. Historical pre-draw artifacts remain untouched.

Separately continue E0037's specification-determined monitor: code commit 9560d781d9e8a5d28f4b84e603120a97b4b619f1 dated 2026-10-14 predates all six targets. Keep its frozen parameters, weights, start date, four-lane threshold E>=80 and practical threshold 0.009388 nats/draw. This is delayed execution of a previously frozen algorithm, not evidence that per-draw forecasts were physically saved before the results. E0037 remains scoring-only with zero slate authority.

## Hypothesis, controls and evaluation

Hypothesis: existing HEPS probability models and fixed-K compression can outperform uniform/simple controls on the newly appended block; acquisition may remain the binding failure.

Training: active-era rows from 2026-06-02 through t-1, expanding independently by lane (39..44 rows). Six evaluation targets per lane, no untouched validation set for newly designed comparisons.

Probability models: unchanged E0037 nine forecasters, uniform, and its E0030 incumbent/cumulative/recent5 comparators. Primary metric: mean joint log-loss minus uniform (negative is better); coordinate Brier secondary. PB: unchanged four Dirichlet strengths and uniform. Report all models, not only a winner. E-process threshold is the existing frozen E0037 family rule, not an E0038 promotion route.

Acquisition/portfolio audit: E0030 mixture top marginal K13; same-field four-plus swap objective from E0030 (five passes); simple cumulative and recent5 K13 controls. Ascending coordinate ties fixed before evaluation. K20 is a separately labelled diagnostic, never pooled with K13. No claim to reproduce a historical hand-crafted slate. No unrestricted marginal basket is labelled E0026 slot-routed acquisition.

For each frozen K13 enumerate all 1,287 lines. Use the accepted E0022 four-plus-first Johnson 20-line geometry; compare with 20 uniformly sampled distinct lines from the same K13 and 20 from the full field (seed 20261105 plus fixed lane and chronological index offsets). No pattern hard-pruning or oracle winner injection. Rank membership is geometry only; no new coalition-lift claim. Reproduce the applicable E0022 geometry result and run repository tests.

Metrics: K13 hits, <=1 catastrophes, >=3/4/5 survival, exact hypergeometric rates, full-line model mass in basket; K20 separately; same-line best matches, counts >=3/4/5 out of 20 lines; separate PB proper scores/top1 with deterministic ties. Do not conflate candidate hits with ticket hits or Main success with PB.

Search exposure: 9 frozen E0037 forecasters + 3 comparators + uniform; 4 PB strengths + uniform; 4 acquisition arms; 2 K sizes; 3 portfolio comparisons; 2 independently fitted games. One run, no tuning or seed search. Six targets cannot establish a reliable edge. Existing repository-wide search is extensive and unquantified. Draw-level SE is descriptive only; no normal-CI confirmation from six draws.

Falsification: no predictive promotion if proper scores lose to uniform, evidence gate does not pass, temporal tests fail, or matched-exposure acquisition does not improve. Retain negative findings. Any future architectural change requires successor protocol and independent review; this audit changes no production authority.

## Reproduction

Run `python experiments/E0038/update_ledgers.py`, then `python experiments/E0038/replay.py`. Ledger updater is idempotent and refuses conflicting existing outcomes. Replay outputs are isolated in E0038 and each new cycle's post_draw directory; it does not rewrite earlier experiments or pre_draw files.
