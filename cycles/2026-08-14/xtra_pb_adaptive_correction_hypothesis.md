# PowerBall XTRA — Adaptive PB Correction Hypothesis

**Target:** Friday 2026-08-14  
**Status:** `INSUFFICIENT_EVIDENCE` / competing prospective resolver  
**Mode:** `paper_trading_only`

## Context

The previously frozen exact resolver was:

`next = low_a + low_b + 3`

which correctly reconstructs:

- `15 -> 4 -> 8 -> 15` because `4 + 8 + 3 = 15`
- `10 -> 5 -> 5 -> 13` because `5 + 5 + 3 = 13`

and predicts the current unresolved sequence:

- `13 -> 6 -> 2 -> 11` because `6 + 2 + 3 = 11`

## June exception proposed by project director

Earlier sequence:

`11 -> 1 -> 1 -> 15`

The fixed `low_a + low_b + 3` rule would yield 5, which conflicts with the separate tier motif that the fourth ball should return to the `>10` tier.

The project director proposed an alternate correction:

- block sum: `11 + 1 + 1 = 13`
- correction delta: `1 + 1 = 2`
- resolved output: `13 + 2 = 15`

Equivalent algebraically:

`next = anchor + 2 * (low_a + low_b)`

For terminology, HEPS records the quantity 2 as a **correction delta**, not statistical variance.

## Red-team consequence

This adaptive correction is not the same formula as the fixed `+3` resolver. If applied mechanically to the current block `13 -> 6 -> 2`, it gives:

`13 + 2*(6+2) = 29`

which is outside the legal PB range 1-16. A wraparound convention would be an additional post-hoc rule and is therefore not authorized.

Accordingly HEPS must not use the June rescue as retrospective validation of the `+3` law unless a pre-specified trigger explains when the adaptive correction is active.

## Frozen prospective hierarchy for 2026-08-14

1. **Primary exact resolver:** `low_a + low_b + 3` -> **PB11**.
2. **Tier hypothesis:** next PB in **11-16**.
3. **Adaptive-correction hypothesis:** retained as a separate challenger requiring a deterministic trigger rule before it may generate a future exact prediction.

## Falsification rule

After the 2026-08-14 draw, do not alter the constant `+3`, invent a wraparound rule, or retrospectively choose between formulas based on the observed result. Any adaptive trigger must be specified and frozen before a later draw.
