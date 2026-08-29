# 2026-08-28 Main — Post-Draw Audit / Physics of Failure

Verified result: `19,22,24,25,47 | PB11`.

Verification source: `https://www.powerball.net/southafrica/results/2026-08-28`.

Frozen previous state: `5,34,39,43,45 | PB1`.

## Realized state

- Main HLR: `HLLLH`
- Main VVD: `[14,12,15,18,2]`
- PowerBall direction: `HIGH`
- PowerBall VVD: `10`
- Main sum: `137`
- Main spread: `28`

## Frozen forecast comparison

Frozen primary HLR was `HLLLL`, but `HLLLH` was explicitly the third-ranked exact structural joint scenario with probability `0.1446577243` and was preserved as the S5-HIGH hedge branch.

The frozen K13 was:

`{2,6,8,15,19,24,29,33,34,40,43,44,46}`

Winner-coordinate survival:

- 19: survived
- 22: excluded
- 24: survived
- 25: excluded
- 47: excluded

K13 recall: `2/5`.

For a flat K13 under exchangeability, exact-null probabilities are approximately:

- P(exactly 2/5) = 0.2860
- P(2+/5) = 0.3890
- P(3+/5) = 0.1030

Therefore 2/5 survival is not evidence of acquisition lift.

## Frozen portfolio score

Maximum same-line main overlap among the 20 submitted lines: `2/5`.

Lines 1, 3, 5 and 7 each contained `{19,24}`. No frozen line contained 3 or more winning mains.

Frozen PowerBall ranking was `[6,15,3,5]`, primary `6`. Actual PB11 was not in the declared PB exposure.

PB direction `HIGH` was correct, but the exact displacement/state-transition layer failed: actual move was `1 -> 11`, VVD10.

## First failure stage

`candidate_acquisition`.

Coalition assembly, morphology, winner-float and portfolio compression cannot be blamed for the exact-line miss because 3 of 5 winning coordinates never entered K13.

## Failure decomposition

### S1 — 19

`5 -> 19`, HIGH, VVD14. Direction was consistent with the HLLLH branch and the coordinate survived K13.

### S2 — 22

`34 -> 22`, LOW, VVD12. The LOW direction was strongly supported pre-draw, but the magnitude/coordinate field failed to retain 22.

### S3 — 24

`39 -> 24`, LOW, VVD15. The coordinate survived K13 despite the large displacement.

### S4 — 25

`43 -> 25`, LOW, VVD18. The LOW direction was supported, but the large displacement was not preserved through K compression.

### S5 — 47

`45 -> 47`, HIGH, VVD2. This is the most actionable miss. `MAIN_STICTION_SHADOW` explicitly tracks +/-1 or +/-2 shadows, so 47 was inside an existing expert's support neighborhood but lost during K13 compression. This is a clean candidate-preservation/rescue failure, not an unknown tail event.

No retrospective credit is awarded to 47; the lesson is to test whether fixed-K expert-preservation rescue can protect such coordinates prospectively.

### PowerBall — 11

`1 -> 11`, HIGH, VVD10. Direction was correct; frozen exact-ball convergence was wrong. The target reinforces the need to score full PB displacement distributions and shrinkage-weighted conditional transitions rather than rely on a narrow exact-state successor shortlist.

## Architectural interpretation

This target is an important separation case:

1. **Directional scenario coverage was reasonably good.** The exact realized HLR vector `HLLLH` was explicitly retained before the draw.
2. **Magnitude-to-coordinate acquisition failed.** S2/S4 large LOW displacements and the simple S5 +2 shadow were not all preserved.
3. **Distribution-first architecture did not yet solve K13 acquisition.** Preserving HLR branches is insufficient if the coordinate field still compresses away supported residual experts.
4. **Fixed-K rescue deserves higher research priority, not production promotion.** In particular, the S5=47 miss is a prospective motivation for E0007/E0009/E0011 `Core13` vs `Core12+Rescue1` vs `Core11+Rescue2` tests.
5. **Do not increase K simply because this draw missed.** All comparisons remain matched-exposure.

## E0013 jurisdiction

E0013 Positive-PMI Spectral Coalition Ranking requires 5/5 candidate survival for its primary exact-winner rank metric. Because K13 retained only 2/5, the exact winner was not in its 1,287-line universe.

Therefore this target is `NOT_SCORABLE_FOR_PRIMARY_E0013_WINNER_RANK` and provides neither positive nor negative evidence on the primary E0013 coalition hypothesis.

## Evidence classification

- Current Main predictive architecture on this target: miss; first failure `candidate_acquisition`.
- HLR exact-vector branch coverage: prospective scenario-support success, not proof of HLR edge.
- Fixed-K expert-preservation rescue: `INSUFFICIENT_EVIDENCE`, priority increased by a clean +2-shadow exclusion example.
- E0013: no primary score because acquisition prerequisite failed.

Do not regenerate or modify any 2026-08-28 pre-draw artifact.