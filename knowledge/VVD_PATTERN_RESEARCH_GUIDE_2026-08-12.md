# HEPS VVD Pattern Research Guide — 2026-08-12

## Status

- evidence: `INSUFFICIENT_EVIDENCE`
- architecture authority: none
- research mode: prospective challenger
- active-era data only
- pre-June legacy PRNG data: prohibited for parameter setting
- first frozen target: 2026-08-14

This guide preserves the VVD pattern hypotheses identified on 2026-08-12 so future sessions can test them prospectively without reconstructing or reinterpreting the pattern after outcomes are known.

## Definition

For sorted slot `j`, Vertical Variance Delta is:

`D_j(t) = |S_j(t) - S_j(t-1)|`.

These hypotheses concern temporal structure in the VVD magnitudes. They do not claim that a mathematical pattern is automatically predictive. Each hypothesis must beat appropriate blind/null controls before gaining any HEPS authority.

## Data provenance

The pattern search uses the active-era main-draw sequence beginning 2026-06-02. The 2026-08-11 result used to derive the first prospective target was reported as `3,14,26,40,48`; external web indexes available on 2026-08-12 were stale, so canonical result ingestion should remain subject to the normal source-verification rule.

The full recent VVD tails relevant to these hypotheses are preserved below.

### Slot 1 VVD tail

- 2026-07-31: 7
- 2026-08-04: 6
- 2026-08-07: 8
- 2026-08-11: 5

### Slot 3 historical repeat motifs

- 2026-06-16 / 2026-06-19: `7,7`
- 2026-06-23 / 2026-06-26: `5,5`
- 2026-07-10 / 2026-07-14: `8,8`
- 2026-07-17 / 2026-07-21: `10,10`
- 2026-08-11: current VVD = 5

### Slot 4 complete recent VVD tail

`3,9,16,1,10,25,14,9,11,5,1`

corresponding to 2026-07-07 through 2026-08-11. The 2026-07-24 VVD 25 and 2026-07-31 VVD 9 must not be omitted when evaluating Slot 4 patterns.

### Slot 5 Tuesday-to-Friday pairs

- Tue 2026-07-28 -> Fri 2026-07-31: `9,1`
- Tue 2026-08-04 -> Fri 2026-08-07: `8,2`
- Tue 2026-08-11 -> Fri 2026-08-14: `8,?`

## H1 — Slot 1 dual-phase ladder / conserved pair sum

Observed tail:

`7,6,8,5`

Split by weekday phase:

- Friday: `7,8,...`
- Tuesday: `6,5,...`

Prospective recurrence:

- Friday phase increments by `+1`: `7 -> 8 -> 9`
- Tuesday phase decrements by `-1`: `6 -> 5 -> 4`
- Friday/Tuesday pair sum remains `13`: `7+6=13`, `8+5=13`, proposed `9+4=13`

### Frozen predictions

For Friday 2026-08-14:

`D_1 = 9`.

Given reported Tuesday Slot1 = 3, the only legal coordinate is:

`S1 = 12`.

If the Friday phase forecast survives, the continuation already frozen for Tuesday 2026-08-18 is:

`D_1 = 4`.

Do not redefine the phase rule after the Friday result.

## H2 — Slot 3 VVD echo / adjacent doublet

Slot 3 has produced four prior adjacent equal-VVD doublets:

`7,7`; `5,5`; `8,8`; `10,10`.

The reported 2026-08-11 Slot3 move gives current `D_3 = 5`.

### Frozen prediction

For Friday 2026-08-14:

`D_3 = 5`.

Given reported Tuesday Slot3 = 26, legal coordinate branches are:

`S3 = 21` or `S3 = 31`, subject to legal sorted-slot feasibility and any separately frozen HLR direction.

This is an echo hypothesis, not evidence that repeats are intrinsically more probable.

## H3 — Slot 5 Tuesday-to-Friday complement

Two completed recent Tuesday-to-Friday VVD pairs satisfy a conserved sum of 10:

`9+1=10`

`8+2=10`.

Reported Tuesday 2026-08-11 Slot5 VVD is 8.

### Frozen prediction

For Friday 2026-08-14:

`D_5 = 2`.

Given reported Tuesday Slot5 = 48, legal coordinate branches are:

`S5 = 46` or `S5 = 50`.

The rule is specifically Tuesday-to-Friday and must not be generalized to arbitrary adjacent draws without separate evidence.

## H4 — Slot 4 algebraic closure

Slot 4 exhibits visually interesting arithmetic relationships among observed VVD magnitudes, including:

- `9 - 3 = 6`
- `9 + 5 = 14`
- `6 + 5 = 11`
- `14 - 3 = 11`
- `11 + 5 = 16`

The two routes to 11 are algebraically dependent rather than independent votes:

`(9-3)+5 = (9+5)-3 = 11`.

Therefore the current status is descriptive only.

### Frozen allowed grammar for future testing

To prevent unconstrained arithmetic overfit, the first allowed closure grammar is restricted to:

- `a+b`
- `|a-b|`
- no multiplication
- no division
- no arbitrary coefficients
- no use of the future target value in constructing features
- preregistered lookback window before scoring

No Slot4 Friday VVD value is frozen from this hypothesis yet.

## Slot 2 negative finding

Slot2 showed a historical mirror-like subsequence `1,4,31,32,4,1`, but the subsequent `13,2,8` tail does not currently support a constrained continuation. HEPS should record `NO_FORECAST` rather than manufacture an algebraic rule.

## Evidence firewall

These observations were discovered retrospectively. Therefore all begin as `INSUFFICIENT_EVIDENCE` regardless of visual neatness.

They may enter a Friday K=13 only through explicitly labelled rescue/shadow lanes until prospectively validated. They must not receive hard-pruning authority.

## Required validation

1. Freeze the formulas and first target before 2026-08-14.
2. Score exact VVD magnitude, legal coordinate survival, and slot-coordinate outcome.
3. Continue the S1 Tuesday-2026-08-18 forecast only under the already frozen rule; do not conditionally invent a replacement after Friday.
4. Backtest each frozen grammar with strict walk-forward generation, comparing against exact structural VVD null, empirical slot VVD frequency, recency, and matched simple rules.
5. Record multiple-pattern search exposure. S1/S3/S5 were selected after exploratory inspection, so retrospective fit cannot be used as evidence of significance.
6. Promote only if future blind performance adds information beyond `MAIN_VVD_DELTA` / `NULL_VVD_STRUCTURAL` under E0001-style proper controls.

## Research interpretation

The hypotheses are deliberately heterogeneous:

- S1: phase/weekday recurrence;
- S3: local echo/doublet recurrence;
- S4: algebraic closure graph;
- S5: Tuesday-to-Friday complement;
- S2: no defensible current rule.

HEPS should not force one common mechanism across slots merely because all are expressed in VVD space.
