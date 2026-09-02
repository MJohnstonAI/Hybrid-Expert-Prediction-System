# HEPS Assembly Evolution Handoff — 2026-09-02

## Purpose

This file is a compact handoff for ChatGPT, Codex, Claude, Gemini, Cline and other HEPS agents working on coalition assembly, winner-float ranking or portfolio optimization.

Read this before reusing old E0013/E0014 assembly conclusions.

## Mandatory context

Read:

1. `AGENTS.md`
2. `governance/current_method_doctrine.md`
3. `governance/methodology_deprecations.md`
4. `experiments/E0002/decision.md`
5. `experiments/E0013/`
6. `experiments/E0014/` when working on XTRA provenance
7. `experiments/E0022/`
8. `scripts/oracle_k13_assembly_evolution.py`
9. `scripts/johnson_portfolio_optimizer.py`

## Active-era boundary

For E0022 and its derivatives:

- Main uses 2026-06-02 onward only.
- XTRA uses its own 2026-06-02 onward state only.
- No pre-June workbook state, pair count, frequency, recency, gap model or fitted parameter may enter.
- Main and XTRA fitted coalition state never transfer.

## If K13 contains all five winners

Enumerate **all**:

`C(13,5) = 1,287`

five-number lines before ranking.

Do not lose the winner through heuristic generation or hard morphology filters.

Conditional on correct K13, 3+ overlap is a weak headline metric. Prioritize:

- exact winner rank/percentile;
- Top-20/Top-100 survival;
- 4+/5 portfolio coverage;
- catastrophic burial;
- fixed-budget comparison.

## Main — E0013 remains useful but unstable

E0013 spectral remains the strongest historical Main coalition discovery signal by mean oracle-K13 rank, but the newest E0022 replay targets were poor.

Do not promote E0013 further on the basis of old discovery averages.

## Main — new E0022 shadow

`MAIN_ASSEMBLY_DISSENT_OR`

Frozen formula:

`max(midrank_percentile(additive_frequency), midrank_percentile(additive_recency), midrank_percentile(E0013_spectral))`

Interpretation:

- one robustness/meta-assembly operator;
- not three independent votes;
- zero candidate authority;
- zero production authority;
- intended to reduce catastrophic burial when E0013 fails;
- first eligible prospective target after freeze: 2026-09-04.

Retrospective evidence is insufficient for predictive promotion.

## Current rejected Main assembly variants

Do not silently promote or rebrand the current E0022 forms of:

- four-node nucleus;
- conditional completion;
- simple PMI breakthrough claims;
- searched retrospective fusion variants.

They may be revisited only through materially different preregistered hypotheses.

## XTRA correction — old raw-pair result is not a breakthrough

E0014's oracle ranking used a best-in-tie convention for discrete scores. E0022 showed this materially inflated raw pair/frequency percentiles.

Original E0014-window raw-pair replay:

- optimistic best-in-tie mean percentile: about `0.628`;
- average-midrank corrected: about `0.459`.

Therefore:

- do not cite the old XTRA raw-pair ~0.645 oracle result as predictive lift without the E0022 warning;
- use average midrank for tied coalition scores;
- no XTRA predictive coalition assembler is currently promoted.

## Johnson portfolio evolution

The historical `three_plus_first` objective remains available for audit reproduction.

E0022 adds optional:

`four_plus_first`

Use when the fixed-budget objective is maximizing 4+/5 winner-state coverage inside an already frozen candidate set.

For K13:

- 10 lines: 4+-first covers 410/1287 = about 31.86% of possible winner states at >=4/5;
- 20 lines: 788/1287 = about 61.23%;
- 30 lines: 1039/1287 = about 80.73%;
- 50 lines: 1251/1287 = about 97.20%.

At budget 20 the historical 3+-first objective covers 757/1287 = about 58.82%, so 4+-first gives a deterministic same-budget improvement.

This is **portfolio geometry, not prediction**.

For any M distinct selected lines, exact 5/5 coverage remains M/1287 unless a separately validated predictive posterior makes some winner states non-uniform.

## Mandatory tie rule

For an oracle winner score tied with other lines, use average midrank (or another explicitly justified tie-aware rule).

Never use:

`1 + count(score > winner_score)`

and interpret that as if the winner were first within every tie block.

## Recommended forward architecture

### Main

`frozen K13 -> enumerate all 1287 -> E0013 incumbent shadow + Dissent-OR challenger -> fixed budget -> optional 4+-first Johnson`

### XTRA

`frozen XTRA K13 -> enumerate all 1287 -> no promoted predictive coalition ranker -> optional 4+-first Johnson`

XTRA Richardson remains an upstream candidate-field shadow under E0016/E0018 doctrine; do not double-count its information by inventing a second pair vote at assembly without a new residualized experiment.

## Evidence language

- Johnson 4+-first: accepted deterministic assembly geometry.
- Main Dissent-OR: `INSUFFICIENT_EVIDENCE`, prospective shadow.
- E0013: remains `PROVISIONAL_SIGNAL`, coalition shadow.
- XTRA raw pair: prior apparent oracle strength downgraded by tie correction; no predictive authority.
- E0022 overall: `INSUFFICIENT_EVIDENCE` for prediction.

No agent may call E0022 a predictive `BREAKTHROUGH` until prospective evidence satisfies HEPS promotion policy.
