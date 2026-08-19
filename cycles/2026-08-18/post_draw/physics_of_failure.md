# 2026-08-18 — Physics of Failure

Evidence classification: `INSUFFICIENT_EVIDENCE`.

Reported result pending approved-source verification: `3,7,20,31,39 | PB13`.

## First failure stage

The canonical frozen E0008 target failed at **slot movement / candidate information**, before any assembly question.

- S1 reflection forecast: VVD9, LOW, coordinate5. Actual: VVD11, LOW, coordinate3. Direction survived; magnitude and coordinate failed.
- S4 cross-lane `1->4` forecast: VVD4, HIGH, coordinate43. Actual: VVD8, LOW, coordinate31. Magnitude, direction and coordinate failed.
- Matrix-wide VVD6 convergence: 0/6 exact magnitude hits across S1-S5 and PB.

## Structural comparator

The actual Main HLR vector was `LLHLL`. Exact enumeration of all 2,118,760 legal next lines relative to `[14,15,19,39,44]` gives `LLHLL` probability 0.0783401612 and rank 4/243. The realized direction pattern was therefore already highly plausible under exact order-statistic geometry.

## Lessons

1. Algebraic elegance did not survive the first prospective target. E0008 must remain a residual/diagnostic feature and may not override structural or VVD-R probability mass.
2. A pre-draw probability field is preferable to a brittle point motif. The S1 motif chose 5 while the actual 3 remained structurally plausible.
3. Slot assignment can hide useful global coordinate evidence: 39 repeated globally while migrating from prior S4 to actual S5.
4. Simple local coordinate evidence also survived: actual20 was +1 from prior19. This does not prove shadow edge, but it reinforces preserving soft repeat/shadow mass rather than eliminating it.
5. Conversation-only forecasts that were not durably frozen are excluded from canonical prospective scoring.

No expert weight or architecture authority is changed from one draw.
