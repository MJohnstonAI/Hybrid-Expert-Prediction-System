# HEPS — Last-Digit Sum Absolute-Delta Handoff

## Purpose

Communicate E0028 to all PowerBall Main and XTRA research/prediction sessions.

## Canonical name

`LAST_DIGIT_SUM_ABS_DELTA` (`LDSAD`).

The director may refer to this as `Last Digit Absolute Variance`, but the statistic is an absolute draw-to-draw change, not variance.

For each draw:

`SLD_t = sum(last digit of each of the five main numbers)`

Then:

`LDSAD_t = abs(SLD_t - SLD_(t-1))`.

## Main discovery

Using the 27 canonical Main Mechanical-Era draws from 2026-06-02 through 2026-09-01 gives 26 transitions.

Primary frozen discovery band:

`LDSAD in {11,12,13}`

Observed:

`11/26 = 42.31%`

Exact IID 5/50 structural-null expectation:

`10.94%`

Observed/null lift:

`~3.87x`

Secondary frozen challengers:

- `10..13`: 13/26 = 50.00%, null ~15.75%;
- `9..13`: 15/26 = 57.69%, null ~21.19%.

## Critical evidence warning

These bands were discovered after examining historical transitions. They are not confirmed predictive rules.

E0028 status:

`INSUFFICIENT_EVIDENCE / PROSPECTIVE SHADOW ONLY`.

No hard pruning is allowed yet.

## Main next-state reference

The 2026-09-01 Main winning line was:

`14,16,31,34,40`

Its SLD is:

`4+6+1+4+0 = 15`.

Under the primary 11..13 shadow band, the next-draw SLD-sum targets are:

`2,3,4,26,27,28`.

This is shadow information only and must not retroactively rewrite a frozen prediction artifact.

## Intended HEPS role

LDSAD is a **combination-space constraint**, not a number-selection expert.

Correct order of use:

1. exact legal-line geometry;
2. HLR / signed-transition scenario constraints;
3. E0026 slot routing;
4. LDSAD shadow constraint;
5. downstream ranking/assembly.

For every target, report:

- legal lines before LDSAD;
- legal lines after LDSAD;
- incremental compression after HLR/E0026;
- whether the actual winning line survives;
- candidate-coordinate survival;
- catastrophic winner loss;
- exact-null expected retention;
- matched random-band control.

## XTRA rule

Do NOT copy Main's 11..13 band into XTRA as predictive authority.

XTRA may transfer the method only:

1. use the canonical XTRA Mechanical-Era ledger beginning 2026-06-02;
2. compute XTRA SLD for each draw;
3. compute consecutive XTRA LDSAD values;
4. build the XTRA frequency pivot;
5. compare each proposed band with the exact 5/50 structural null;
6. record neighboring-band/multiple-testing exposure;
7. freeze an XTRA-specific band prospectively;
8. test it as a shadow combination-space constraint before any pruning authority.

Main and XTRA findings remain independent.

## Repository paths

Read:

1. `experiments/E0028/hypothesis.md`
2. `experiments/E0028/protocol.yaml`
3. `experiments/E0028/results.json`
4. `experiments/E0028/decision.md`
5. `experiments/E0026/`
6. `governance/current_method_doctrine.md`

## Promotion criterion

Only consider hard-elimination authority after multiple genuinely prospective targets demonstrate very high winning-line retention (preferably >=90–95%) together with material incremental legal-space compression beyond HLR/E0026 and multiplicity-aware evidence.