# 2026-08-07 Physics of Failure

## Actual result

Main: `8,22,31,39,40`  
PowerBall: `5`

Verified against the director-approved result sources `powerball.net/southafrica/results` and `lottery.co.za/powerball/results`.

Relative to the previous main `16,24,29,34,38`, the realized sorted-slot HLR vector was:

`LLHHH`

with slot deltas:

`[-8,-2,+2,+5,+2]`.

The PowerBall moved `15 -> 5`, direction LOW, delta `-10`.

## Frozen-slate score

The frozen pre-draw slate in `cycles/2026-08-07/pre_draw/prediction_slate.json` achieved a best same-line main overlap of `2/5`.

The best frozen line for mains was:

`10,22,40,46,50` -> hits `22,40`.

PowerBall `5` appeared on frozen line 12, but that line contained zero winning main numbers.

## Stage attribution

### Slot forecast

Frozen committed HLR: `HLHHL`  
Actual HLR: `LLHHH`

The frozen primary HLR was correct on Slots 2, 3 and 4 and wrong on Slots 1 and 5 (`3/5`).

The pre-draw joint-flow rescue lane ranked `LLHHH` first. The director's independent pre-draw analysis also selected LOW for Slot1 and Slot2, uncertain HIGH for Slots3/4, and HIGH for Slot5; the realized main vector therefore validated the retained `LLHHH` scenario direction prospectively but does not establish durable HLR skill from one target.

### Candidate funnel

The frozen 38-number exposure union contained `8,22,31,40` but excluded `39`.

Candidate survival: `4/5`.

First irreversible pipeline failure: **candidate exclusion of 39**.

This is a Safe Exclusion failure. No downstream assembler could construct the exact winning main line after 39 was removed.

### Coalition / portfolio assembly

Even among the four surviving winning coordinates, the published 20-line slate assembled at most two on one line. Therefore there was a secondary assembly failure after the candidate-funnel failure.

### Important VVD correction

Do not record a false `29 -> 39` Slot3 VVD hit. The actual sorted slots were:

- Slot3: `29 -> 31` (`+2`)
- Slot4: `34 -> 39` (`+5`)

The legitimate exact pre-draw coordinate success was Slot1 `8`, which matched the director's VVD/HLR challenger bias. `39` was the actual Slot4 value and had been excluded from the frozen candidate union.

## Evidence classification

- `LLHHH` rescue direction: `PROVISIONAL_SIGNAL` for this target only; requires prospective replication.
- Slot1=8 director/VVD challenger: exact target hit, still `INSUFFICIENT_EVIDENCE` as a general rule.
- Candidate Lattice K=38 exclusion safety: failed this target by excluding 39.
- Frozen 20-line assembly: failed to exceed 2/5.
- PowerBall coverage: exact PB existed somewhere in slate but had no useful same-line main synergy.

## Architectural implication

Prioritize candidate survival / Safe Exclusion research. Johnson/extremal-combinatoric assembly can improve portfolio geometry only after winning coordinates survive the candidate stage.
