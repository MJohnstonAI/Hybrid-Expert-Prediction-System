# E0028 — Last-Digit Sum Absolute-Delta Constraint Championship

## Status

`PROPOSED PROSPECTIVE SHADOW / DISCOVERY BAND FROZEN`

Evidence classification: `INSUFFICIENT_EVIDENCE`.

Paper trading only.

## Canonical terminology

The director's working phrase `Last Digit Absolute Variance` is retained as an alias for communication, but the statistic tested here is not statistical variance.

Canonical HEPS name:

`LAST_DIGIT_SUM_ABS_DELTA` (`LDSAD`).

For Main draw `t` with sorted main numbers `x_1..x_5`:

`SLD_t = sum_j (x_j mod 10)`

and for consecutive draws:

`LDSAD_t = abs(SLD_t - SLD_{t-1})`.

## Discovery observation — Main Mechanical Era

Using the 27 canonical Main draws from 2026-06-02 through 2026-09-01 gives 26 consecutive transitions.

Observed LDSAD frequencies include:

- `12`: 5 occurrences;
- `11`: 4 occurrences;
- `13`: 2 occurrences.

Therefore the discovery band `11..13` occurred:

`11/26 = 42.3077%`.

Under the exact IID uniform 5-of-50 structural null, where the SLD distribution is enumerated across all `C(50,5)=2,118,760` legal lines and two consecutive draws are independent:

`P(LDSAD in 11..13) = 0.1093753578` (~10.94%).

Observed/null lift is therefore approximately:

`0.423077 / 0.109375 = 3.87x`.

Related discovery bands:

- `10..13`: observed 13/26 = 50.00%; exact-null 15.7532%;
- `9..13`: observed 15/26 = 57.69%; exact-null 21.1859%.

## Critical multiplicity warning

The `11..13` band was noticed after inspecting the transition distribution. It was not preregistered before these outcomes existed.

Therefore:

- nominal fixed-band surprise must not be treated as confirmation;
- neighboring-band search exposure and other pattern-search exposure must be recorded;
- no predictive `BREAKTHROUGH` credit is allowed from the historical concentration;
- the discovery band is frozen now for genuinely prospective scoring only.

## Core hypothesis

A pre-frozen LDSAD band can act as a useful **combination-space constraint** after stronger state constraints such as HLR / scenario-constrained slot routing, eliminating a materially larger fraction of legal lines than the fraction of future winning lines it loses.

The primary research question is not whether LDSAD ranks individual numbers. It is whether it provides incremental legal-space compression **conditional on existing HEPS constraints** while preserving the realized winning line.

## Current Main target mapping

The 2026-09-01 Main draw `14,16,31,34,40` has:

`SLD = 4+6+1+4+0 = 15`.

For the frozen discovery band `LDSAD in 11..13`, the corresponding next-draw SLD-sum targets are:

- lower branch: `2,3,4`;
- upper branch: `26,27,28`.

These values are **shadow constraints only**. They may not alter an already frozen slate unless a separately governed pre-draw challenger was frozen before outcome knowledge.

## Main versus XTRA boundary

Main and XTRA must be independent.

Do not transfer the Main-fitted 11..13 band to XTRA as predictive authority.

XTRA may reuse only the method:

1. compute its own draw-level SLD sequence;
2. compute its own consecutive LDSAD sequence;
3. compare observed band concentration with the same exact 5/50 structural null;
4. freeze any XTRA discovery band prospectively before using it in XTRA filtering;
5. account for search exposure separately.

## Desired role in HEPS

LDSAD belongs to `pattern_constraint_elimination / morphology` and has:

- zero candidate-discovery authority;
- zero slot-forecast authority;
- zero hard-pruning authority initially;
- shadow line-retention/compression scoring only.

Promotion to hard elimination requires repeated prospective winner retention with strong incremental compression beyond HLR/E0026 and matched controls.