# HEPS Main — Pattern-Constraint K13 Assembly Handoff

## Purpose

Communicate the E0029 blind-replay result and evolved Main assembly architecture to all HEPS research/prediction sessions.

## Read first

1. `experiments/E0029/hypothesis.md`
2. `experiments/E0029/protocol.yaml`
3. `experiments/E0029/results.json`
4. `experiments/E0029/decision.md`
5. `experiments/E0028/`
6. `experiments/E0022/`
7. `experiments/E0013/`
8. `experiments/E0005/`
9. `governance/current_method_doctrine.md`
10. `governance/methodology_deprecations.md`

## Core architectural conclusion

Pattern recognition should operate **after the K13 candidate basket is frozen**, not by trying to eliminate lines from the whole 2,118,760 state space and not by changing K13 membership.

For K13 there are exactly:

`C(13,5)=1,287`

five-number lines.

E0029 isolates this stage with oracle K13 replay: five true winners + eight random decoys, all 1,287 lines enumerated, average-midrank scoring, minimum eight prior Main draws, and target-excluded feature estimation.

## Adaptive pattern family

For each target, fit only from earlier draws:

- BARP HLR residual versus exact structural HLR null;
- adaptive LDSAD residual;
- adaptive total-sum absolute-delta residual (`SUMAD`);
- adaptive span absolute-delta residual (`SPANAD`).

Use `kappa=20` shrinkage for the three whole-line delta residual fields.

Convert each pattern lane to an average-midrank percentile across the 1,287 lines.

## Pattern-OR

Canonical formula:

`MAIN_PATTERN_OR = max(HLR_pct, LDSAD_pct, SUMAD_pct, SPANAD_pct)`.

Interpret this as one anti-burial robustness operator, not four independent probability votes.

## Preferred E0029 shadow cascade

`MAIN_PATTERN80_SPECTRAL5_RESCUE`

1. Freeze Main K13.
2. Enumerate all 1,287 combinations.
3. Compute target-excluded Pattern-OR for every line.
4. Retain the top 80% Pattern-OR lines.
5. Rescue any E0013 spectral line in the top 5%, even when Pattern-OR would exclude it.
6. Rank retained lines by E0013 spectral score.
7. Keep excluded lines in the artifact below retained lines for audit; do not erase them from scientific memory.
8. Apply fixed-budget portfolio geometry only after ranking.

## Blind replay result

Across 19 eligible target-excluded Main replay targets, 30 oracle-decoy replicates per target, and two independent random seeds:

- mean winner percentile: ~`0.63675`;
- median winner percentile: ~`0.70811`;
- Top-100 rate: ~`16.32%`;
- winner above median: ~`69.0%`;
- fraction of lines retained: ~`80.27%`;
- fraction eliminated: ~`19.73%`;
- winning-line gate survival: ~`92.81%`.

For comparison, the two-seed E0013 spectral-only mean winner percentile was ~`0.58189`, while E0022 Dissent-OR was ~`0.50076` in the same discovery programme.

## Why not use the 50% gate?

The 50% gate looked stronger on mean rank but sacrificed too many winners. HEPS prioritizes catastrophic-loss control, so 80% is the preferred prospective shadow threshold.

## Why spectral rescue exists

The pattern family can reject a line that E0013 considers elite. A top-5% spectral rescue adds very little line exposure but protects those cases.

No K expansion occurs. The rescue operates only inside the already frozen 1,287-line K13 universe.

## E0028 fixed-band warning

The following discovery bands remain shadow only:

- LDSAD `11..13`;
- SUMAD `8..9`;
- SPANAD `5..6`.

They produced stronger retrospective tiering but were chosen after historical outcomes were visible. Do not use them as production hard filters or cite them as confirmed predictive rules.

## Evidence boundary

E0029 is:

`INSUFFICIENT_EVIDENCE / PROSPECTIVE SHADOW ARCHITECTURE`.

The replay is strict target-excluded, but the strategy family was designed after those historical outcomes existed. Therefore it is discovery evidence, not prospective confirmation.

## First fresh target

`2026-09-04 Main`

Freeze the E0029 ranking as a shadow against the already frozen K13. Do not rewrite the existing official slate solely from E0029 discovery evidence.

## XTRA boundary

Do not transfer fitted Main residual distributions, Pattern-OR performance claims, or the 80/5 thresholds automatically into XTRA.

XTRA may transfer the **methodology only** through a separately registered, XTRA-specific target-excluded experiment using its own post-2026-06-02 ledger.
