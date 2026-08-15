# 2026-08-14 Physics of Failure

## Result and provenance

Director-reported result pending external verification:

`14, 15, 19, 39, 44 | PB 3`

Previous draw:

`3, 14, 26, 40, 48 | PB 10`

Actual main-field HLR: `HHLLL`  
Actual VVD: `[11,1,7,1,4]`

This audit does not reconstruct or rewrite any pre-draw artifact after the result.

## First failure stage

**Candidate acquisition.**

The frozen E0004 candidate union retained only winner `44`, giving `1/5` winner-coordinate survival. Its 20 frozen lines produced sixteen `0/5` overlaps and four `1/5` overlaps; maximum main overlap was `1/5`. Johnson or any later assembler could not rescue a basket that had already lost four winners.

## Structural baseline

For previous sorted state `[3,14,26,40,48]`, the exact per-slot structural modal directions were:

`HIGH, HIGH, LOW, LOW, LOW`

The actual draw was exactly `HHLLL`.

The exact joint `HHLLL` vector had probability `207592 / 2118760 = 0.097978...` and rank 3 among the 243 legal HLR vectors. This is a successful structural baseline prediction of direction, **not** evidence of lottery predictability. It demonstrates how much apparent HLR structure can be explained by sorted order-statistic geometry.

## E0003 first prospective target

The frozen point hypotheses failed:

- Slot1: VVD9 -> coordinate12; actual VVD11 -> coordinate14.
- Slot3: VVD5 -> coordinates21/31; actual VVD7 -> coordinate19.
- Slot5: VVD2 -> coordinates46/50; actual VVD4 -> coordinate44.
- Slot4 was diagnostic only in E0003.
- Slot2 had no E0003 forecast.

Post-draw, the three point errors on Slots1/3/5 are all `+2` in actual VVD relative to forecast. This is a new observation only. It receives zero retrospective credit and must be frozen prospectively before any predictive claim.

## E0004 challenger

- Slot2 frozen coordinate13 missed actual15.
- Slot4 closure set `{4,6,10,14,16}` missed actual VVD1.
- Frozen candidate union captured only44.
- The closure route that contained44 was not an exact-slot success: actual44 occupied Slot5, not Slot4.

## Coulomb / candidate-preservation lesson

Several actual winners had simple candidate-level support from the previous draw:

- `14`: exact repeat of prior coordinate14, but migrated from Slot2 to Slot1.
- `15`: `+1` shadow of prior14.
- `39`: `-1` shadow of prior40.

The concentrated slot lattice did not preserve all of these coordinates. This is an architecture failure mode: a globally supported coordinate can be suppressed because a slot-specific expert assigns it to the wrong positional lane or because consensus becomes too concentrated.

## Winner44

Winner44 had at least two plausible pre-draw routes:

- starvation/void support under `MAIN_VOID_BRIDGE`;
- coordinate44 appeared in the E0004 Slot4 algebraic-closure branch.

It should receive candidate-coordinate credit only. The actual Slot5 assignment means the E0004 Slot4 VVD hypothesis did not succeed.

## Winner19

No strong frozen E0003/E0004 route has been identified for19. This is a useful negative case for future candidate-discovery research.

## PowerBall

Conversation-stage research before the result favoured LOW from prior PB10 and exact candidates `{5,8,9}`. Actual PB3 was LOW, so direction succeeded while the exact shortlist failed. Because this PB synthesis was not durably frozen in the repository, record it as research context rather than canonical slate evidence.

## Overall diagnosis

1. The main bottleneck remains candidate acquisition, not Johnson assembly.
2. Exact structural HLR should remain mandatory as a null/rescue reference.
3. VVD should not be abandoned, but exact point-pattern forecasting was brittle on its first prospective target.
4. Global coordinate support must be separated from exact-slot assignment.
5. Coulomb-supported dissent requires protected exposure so consensus cannot erase it silently.
6. New state-duration, distributional VVD, coordinate-mobility and joint-state residual models require prospective experiments rather than post-hoc retuning.

## Evidence classification

`INSUFFICIENT_EVIDENCE`

No Friday result justifies promotion of a predictive expert. The draw mainly supplies a falsification event and architecture-learning evidence.
