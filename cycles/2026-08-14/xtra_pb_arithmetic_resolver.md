# PowerBall XTRA — Arithmetic PB Resolver Hypothesis

**Target:** Friday 2026-08-14  
**Status:** `INSUFFICIENT_EVIDENCE` / prospective exact-ball challenger  
**Mode:** `paper_trading_only`

## Hypothesis proposed pre-draw

For a local XTRA PB motif of the form:

`anchor -> low_a -> low_b -> next`

propose the exact resolver:

`next = low_a + low_b + 3`

provided the result lies in the legal PowerBall range 1-16.

## Observed examples in the June-August 2026 XTRA ledger

Successful examples identified by the project director:

- `15 -> 4 -> 8 -> 15`, because `4 + 8 + 3 = 15`.
- `10 -> 5 -> 5 -> 13`, because `5 + 5 + 3 = 13`.

Current unresolved sequence:

- `13 -> 6 -> 2 -> ?`, therefore `6 + 2 + 3 = 11`.

**Frozen exact-ball prediction for 2026-08-14: PB11.**

This is also consistent with the separately frozen broad tier hypothesis `PB > 10`, because 11 is in the 11-16 tier.

## Red-team counterexample

The full June-August ledger contains an earlier comparable window:

- `11 -> 1 -> 1 -> 15`.

The arithmetic rule would have predicted `1 + 1 + 3 = 5`, so it fails on that earlier case.

Therefore this is not a global law over the complete 21-draw sample. If the anchor criterion is taken as `>=10` followed by two values `<10`, the historical record before tonight is 2 exact matches in 3 comparable completed windows.

The apparent historical fit was discovered retrospectively and must not be assigned a valid significance level without correcting for hypothesis search / multiple testing. Tonight's PB11 call is the first genuinely prospective test of this exact arithmetic resolver.

## Prospective interpretation

- If PB11 occurs: record one prospective exact hit and elevate the resolver for replication, not directly to production.
- If PB11 does not occur: record a prospective miss; do not redefine the constant `+3`, the anchor boundary, or the window after seeing the outcome.
- The broader `PB >10` tier hypothesis must be scored separately from the exact PB11 hypothesis.
