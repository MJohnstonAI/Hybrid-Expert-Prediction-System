# E0037 Decision — Bucket-Depletion / Cold-Number Residual Championship

## Decision

**Main:** `REJECT current cold-bucket formulation`.

**XTRA:** `PROVISIONAL_SIGNAL — DISCOVERY ONLY / ZERO-WEIGHT PROSPECTIVE SHADOW`.

Overall evidence classification: `INSUFFICIENT_EVIDENCE`.

## Main

The director's "numbers left in the bucket" intuition does not improve Main under the current experiment.

Across 39 target-excluded targets:
- AGE_COLD K13 averaged **1.2821** winners versus random-K13 expectation **1.30**;
- catastrophic `H<=1` occurred **69.23%** versus random **61.10%**;
- all tested cold probability fields had mean log loss worse than uniform;
- a single remarkable 5/5 cold-K13 event occurred on 2026-10-06, but the full denominator is negative.

Do not promote the isolated 5/5.

## XTRA

XTRA shows a different pattern.

For the 8-draw unseen set:
- average unseen coordinates before each target: **20.44 of 50**;
- expected winners from that set under IID: **79.7 of 195** target coordinates;
- observed: **97 of 195**;
- observed winner share **49.74%** versus **40.87%** expected;
- relative enrichment about **1.217x**;
- raw standardized excess `z=2.637`;
- 50,000 IID sequence simulations: one-sided p about **0.00438** for W8;
- after searching the frozen four windows {3,5,8,12}, max-window simulation p about **0.0141**.

The effect is not confined to one half:
- first 19 targets: 46 observed vs 39.3 expected, z=1.460;
- last 20 targets: 51 observed vs 40.4 expected, z=2.262.

However, predictive evidence is weaker:
- target-excluded UNSEEN_W8 proper-score mean delta = **-0.0442 nats/target** (better than uniform), SE **0.0563**, t=-0.785;
- AGE_COLD K13 averaged **1.4103** winners vs random 1.30, but exact null tail for >=55 total hits is about **0.257**.

Therefore this is not a production edge.

## Interpretation

The physical "balls have been removed from the bucket" story is not accepted. Draws reset between games, and current public draw information describes RNG selection with traditional machines only as fallback. E0037 instead tests a statistical **negative-recurrence / recent-absence residual**.

The only worthwhile lead is XTRA-specific:
> coordinates absent from the previous 8 XTRA draws have appeared in the next XTRA draw more often than their set size predicts.

Main does not reproduce this, so no cross-lane transfer is allowed.

## Forward rule

1. Freeze XTRA UNSEEN_W8 as a zero-weight shadow beginning 2026-11-27.
2. Do not alter the official XTRA K13 or slate from E0037 yet.
3. Score every fresh XTRA target:
   - unseen set size;
   - winners from unseen set;
   - conditional null expectation;
   - proper-score delta;
   - cold-K13 hits.
4. No window retuning. W=8 is frozen.
5. Main remains rejected for this formulation unless materially new evidence/operator is proposed.
6. Reassess after multiple prospective XTRA targets; no single draw may promote it.
