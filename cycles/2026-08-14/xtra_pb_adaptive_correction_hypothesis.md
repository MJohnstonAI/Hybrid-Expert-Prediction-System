# PowerBall XTRA — Tier-Constrained Adaptive PB Resolver

**Target:** Friday 2026-08-14  
**Status:** `INSUFFICIENT_EVIDENCE` / prospective exact-ball challenger  
**Mode:** `paper_trading_only`

## Motif

The working XTRA PB block is:

`anchor -> low_a -> low_b -> next`

with a separate tier hypothesis that the fourth PB should return to the **>10** tier after two values below 10.

## Primary arithmetic candidate

First compute:

`candidate_1 = low_a + low_b + 3`

Historical completed blocks:

- `15 -> 4 -> 8 -> 15`: `4 + 8 + 3 = 15` — exact hit.
- `10 -> 5 -> 5 -> 13`: `5 + 5 + 3 = 13` — exact hit.

Current unresolved block:

- `13 -> 6 -> 2 -> ?`: `6 + 2 + 3 = 11`.

Therefore the frozen primary prediction for 2026-08-14 remains **PB11**.

## Tier-constrained fallback

Earlier June block:

`11 -> 1 -> 1 -> 15`

The primary formula gives `1 + 1 + 3 = 5`, which violates the separate fourth-position tier expectation `>10`.

The project director proposed a correction using the three-ball block:

- block sum: `11 + 1 + 1 = 13`
- correction delta: `1 + 1 = 2`
- corrected output: `13 + 2 = 15`

Equivalent fallback formula:

`candidate_2 = anchor + 2 * (low_a + low_b)`

HEPS records the quantity 2 as a **correction delta**, not statistical variance.

## Frozen piecewise resolver

Before the 2026-08-14 draw, the hypothesis is now specified as:

1. Compute `candidate_1 = low_a + low_b + 3`.
2. If `candidate_1` is legal and in the expected **>10** tier, use `candidate_1`.
3. If `candidate_1 <= 10`, treat it as tier-inconsistent and evaluate the fallback `candidate_2 = anchor + 2*(low_a + low_b)`.
4. The fallback is valid only if it is itself a legal PB value 1-16. No wraparound/modulo operation is authorized.

Applied retrospectively to the three completed qualifying blocks:

- `11,1,1`: primary gives 5 -> tier fail -> fallback gives 15 -> actual 15.
- `15,4,8`: primary gives 15 -> accepted -> actual 15.
- `10,5,5`: primary gives 13 -> accepted -> actual 13.

Applied prospectively tonight:

- `13,6,2`: primary gives **11**, which is legal and >10, so the fallback is not invoked.

**Frozen exact prediction: PB11.**

## Red-team qualification

The piecewise trigger was discovered using the completed June exception, so the three historical fits are retrospective and cannot be treated as independent validation. The 2026-08-14 PB11 call is the first prospective test of the fully specified tier-constrained resolver.

After the draw, do not alter the `+3` constant, the `>10` trigger, the fallback equation, or introduce wraparound based on the observed result.
