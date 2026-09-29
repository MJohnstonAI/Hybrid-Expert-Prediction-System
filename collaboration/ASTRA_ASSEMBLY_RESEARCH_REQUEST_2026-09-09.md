# Astra Research Request — Exact 5-of-13 Assembly / Winner-Float Challenge

**Date:** 2026-09-09  
**Lane:** South African PowerBall Main only  
**Stage:** Coalition Assembly -> Winner-Float Ranking -> Fixed-Budget Portfolio  
**Evidence status entering task:** `INSUFFICIENT_EVIDENCE`  
**Paper trading only:** yes

## Research objective

HEPS has now isolated a downstream problem that remains unsolved even under an oracle acquisition assumption:

> **Conditional on a fixed K13 that contains all five actual winning Main numbers, can a target-excluded assembly model surface the exact winning 5-number combination into a Top-10 prediction slate, or at minimum materially improve exact-winner rank / Top-20 survival over matched controls?**

This is a stage-isolation problem only. Oracle injection of winners gives **zero candidate-acquisition credit**.

The desired output is not merely 3+/5 or 4+/5 overlap. The primary target is **exact 5/5 winner ranking** inside the `C(13,5)=1,287` legal K13 lines.

## Mandatory reading order

1. `AGENTS.md`
2. `governance/current_method_doctrine.md`
3. `governance/methodology_deprecations.md`
4. `governance/external_contribution_protocol.md`
5. `knowledge/ASSEMBLY_EVOLUTION_HANDOFF_2026-09-02.md`
6. `experiments/E0013/hypothesis.md`
7. `experiments/E0013/decision.md`
8. `experiments/E0022/hypothesis.md`
9. `experiments/E0022/findings.md`
10. `experiments/E0022/decision.md`
11. `experiments/E0029/protocol.yaml`
12. `experiments/E0033/hypothesis.md`
13. `experiments/E0033/results.md`
14. `experiments/E0033/decision.md`
15. `data/draw_history.jsonl`

Use only the Main active era beginning `2026-06-02`. Do not import XTRA fitted state. Do not use pre-June workbook history.

## Current empirical finding that motivates this request

E0033 performed a last-three-draw oracle-replacement assembly stress test. For each target, HEPS started from the actual frozen pre-draw K13, retained any winners already present, injected the missing actual winners, and then kept K fixed at 13 by testing **every valid way to retain eight of the original K13 non-winners**. This avoided cherry-picking which predicted numbers to remove.

Total oracle-adjusted K13 universes scored: **1,155**.

### 2026-09-01

Actual: `[14,16,31,34,40]`  
Frozen K13: `[20,22,23,26,30,31,32,34,35,39,41,43,49]`  
Winners already in K13: `31,34`  
Missing winners injected: `14,16,40`  
Exhaustive adjusted universes: `165`

### 2026-09-04

Actual: `[4,7,27,38,50]`  
Frozen official K13: `[3,8,18,19,20,23,32,34,35,39,40,48,50]`  
Winner already in K13: `50`  
Missing winners injected: `4,7,27,38`  
Exhaustive adjusted universes: `495`

### 2026-09-08

Actual: `[4,8,13,37,49]`  
Frozen E0032 shadow K13: `[2,4,5,14,16,19,22,24,27,31,34,39,40]`  
Winner already in K13: `4`  
Missing winners injected: `8,13,37,49`  
Exhaustive adjusted universes: `495`

## Existing assembly results

### Direct E0013 spectral exact-line ranking is weak

Median exact-winner rank among 1,287 lines:

- 2026-09-01: **1,062**
- 2026-09-04: **1,108**
- 2026-09-08: **735**

No E0013 exact winner reached Top-20 in any replacement variant across these targets.

### Nucleus-completion idea is attractive but current rankers are unstable

A four-number nucleus has nine possible fifth-number completions inside K13. Therefore if the correct 4/5 nucleus is identified, exhaustive completion can guarantee the exact winner inside nine lines.

However the current tested nucleus rankers are unstable:

- frequency nucleus worked strongly on 2026-09-01 and failed on 2026-09-04 / 2026-09-08;
- positive-PMI nucleus worked strongly on 2026-09-08 and weakly on the previous two;
- E0013 spectral nucleus was not stable.

This means the **completion mechanism is sound**, but reliable nucleus identification remains unsolved.

### Johnson geometry is robust for 4+/5, not exact 5/5

E0022 four-plus-first Johnson geometry on the adjusted oracle K13 universes:

Top-20 contains at least one 4+/5 line:

- 2026-09-01: **92.12%**
- 2026-09-04: **88.89%**
- 2026-09-08: **76.36%**

Reordering the fixed Johnson-20 set by simple positive-PMI pair score floated a 4+/5 line into Top-10 in:

- 2026-09-01: **58.79%**
- 2026-09-04: **44.65%**
- 2026-09-08: **55.76%**

Median first 4+/5 rank: `8, 10, 7` respectively.

This suggests a potentially useful architecture:

`correct K13 -> geometry-first protected Top20 -> predictive reordering of those fixed lines`

But **exact 5/5 remains unsolved**.

## Hard research question for Astra

Design and rigorously test the strongest mathematically defensible assembly / winner-float method you can derive under the following condition:

> The fixed K13 is guaranteed to contain all five winners, but the model does not know which five they are.

The method should aim to surface the exact winner into **Top-10**, with Top-20 as secondary objective, while preserving or explicitly trading off the strong 4+/5 coverage already available from Johnson geometry.

Do not assume that E0013, PPMI, nucleus completion, or Johnson is correct. They are baselines / components to challenge.

## Important directions worth considering, not requirements

You may investigate any mathematically justified approach, including but not limited to:

- uncertainty-aware four-node nucleus ensembles rather than a single top nucleus;
- exhaustive fifth-number completion when nucleus posterior concentration is high;
- Bayesian or hierarchical pair/hypergraph models with strong shrinkage;
- marginal-conditioned residual pair association rather than raw/smoothed PMI;
- higher-order interactions only when sample-size control is explicit;
- posterior probability over the 1,287 K13 lines rather than ad-hoc rank fusion;
- diversity-aware or risk-sensitive Top10 selection;
- two-stage `coverage -> ranking` systems;
- mixture-of-assemblers where weights are learned strictly target-excluded;
- rank aggregation with explicit dependence control;
- minimum-regret / minimax methods over model uncertainty;
- conformal or Bayesian uncertainty sets over candidate nuclei/completions;
- exact combinatorial optimization of Top10 / Top20 under a learned posterior.

Avoid inventing complexity merely to fit the three known targets.

## Baselines and nulls

At minimum compare against:

1. random ordering of the same 1,287 lines;
2. additive frequency;
3. additive recency;
4. simple positive-PMI / raw pair where tie-safe;
5. E0013 spectral;
6. E0022 Dissent-OR;
7. Johnson 4+-first Top10 and Top20 geometry;
8. Johnson-20 followed by the current post-hoc PPMI reorder;
9. nucleus-completion baselines already described in E0033.

For exact winner under a uniformly random ranking of 1,287 states:

- Top-10 probability = `10/1287 ≈ 0.777%`;
- Top-20 probability = `20/1287 ≈ 1.554%`.

Do not claim lift merely from 4+/5 coverage geometry.

## Evaluation design

### Phase A — reproduce E0033

First independently reproduce the E0033 last-three oracle-replacement results. If you cannot reproduce them, report the discrepancy before proposing a successor.

### Phase B — discovery on broader active-era oracle replay

Use target-excluded expanding-window state. Oracle K13 may be constructed as five actual winners plus eight decoys, or by the E0033 replacement protocol when historical frozen K13 artifacts exist. Keep the two designs labelled separately.

Because the strategy is being designed after these historical outcomes are known, all such results are **discovery/post-hoc evidence only**.

### Phase C — freeze a derivative prospective challenger

If a method survives, specify one exact frozen algorithm for the next eligible Main target. No target-aware tuning after freeze.

## Primary metrics

Report at minimum:

- exact winner rank / percentile among 1,287;
- Top-10 exact 5/5 rate;
- Top-20 exact 5/5 rate;
- median exact-winner rank;
- catastrophic burial rate, e.g. rank > 1,000;
- Top-10 and Top-20 4+/5 rate;
- median first 4+/5 rank;
- line-budget fixed at 10 and 20;
- results by target, not only pooled mean;
- replacement-universe sensitivity;
- decoy-seed sensitivity where random decoys are used;
- search / hyperparameter exposure.

If producing probabilities, include proper scoring against an appropriate within-K13 baseline.

## Falsification standard

A successor should be rejected or remain `INSUFFICIENT_EVIDENCE` if:

- it relies on target-known feature selection or tuning;
- exact 5/5 improvement is driven by one target only;
- performance collapses under alternative valid decoy/replacement universes;
- it improves only 4+/5 geometry while exact winner remains random;
- it depends on tie handling artefacts;
- gains disappear against matched line budgets;
- model complexity is unsupported by the tiny active-era sample;
- its posterior / score is not full-support where a probability claim is made.

## Required deliverables

Please place your contribution under a new folder such as:

`collaboration/contributions/Astra_codex_2026-09-09/`

Include, where practical:

1. `ASSEMBLY_EXACT5_RESEARCH_2026-09-09.md` — derivation, critique, experiment design, results and recommendation;
2. runnable code or pseudocode sufficient for independent reproduction;
3. machine-readable results JSON/CSV;
4. explicit search-exposure disclosure;
5. proposed derivative protocol if anything survives;
6. exact evidence classification using one of: `BREAKTHROUGH`, `PROVISIONAL_SIGNAL`, `INSUFFICIENT_EVIDENCE`, `REJECT`.

Do **not** modify frozen historical prediction artifacts or silently promote a method into production authority.

## Desired role

Act as an adversarial senior research scientist / combinatorial statistician. The goal is not to validate the current HEPS architecture. Try to falsify it, replace it, or derive a simpler and stronger assembler if possible.

A negative result is valuable if it demonstrates that exact Top-10 assembly is statistically unidentifiable with the current active-era data.
