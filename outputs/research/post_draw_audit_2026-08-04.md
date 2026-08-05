# HEPS Post-Draw Audit — 2026-08-04

Status: retrospective scoring of frozen pre-draw artifacts; paper-trading research only.

## Actual main PowerBall result

- Main: `16, 24, 29, 34, 38`
- PowerBall: `15`
- Macro-sum: `141`

User-reported/cross-checked PowerBall XTRA result:

- Main: `5, 20, 21, 36, 44`
- PowerBall: `13`

## Frozen HEPS v33.3 artifact scored

Artifact: `outputs/predictions/prediction_slate_2026-08-04_v33_3_20line.json`

### Candidate discovery

Frozen 22-number hierarchy:

`2,9,37,44,16,26,40,43,33,10,45,12,47,21,27,32,48,35,19,39,11,46`

Actual winners present: `16` only.

Candidate recall: **1/5**.

Frozen 13-number covering pool also contained only `16`, so the conditional 3+ covering guarantee was never activated.

### Final 20-line portfolio

- Champion 10: best main overlap = **1/5**.
- Challenger 10: best main overlap = **1/5**.
- Full 20: zero lines with 2+ mains.
- Exact PB15 appeared on frozen lines 7 and 12, but those lines had zero main-number matches.

Failure classification: **candidate-discovery failure**. Coalition assembly cannot recover winners that never enter the candidate pool.

This contrasts with 2026-07-31, where candidate discovery captured all five mains and final routing/assembly was the principal failure.

## HLR directional challenger

Pre-draw HLR hypothesis relative to 2026-07-31:

`L — H — L — L — H | H`

Actual directional transition on 2026-08-04:

`H — H — L — L — L | H`

Matched states: S2, S3, S4 and PB = **4/6**. The explicit pre-draw PowerBall direction call `H (>11)` succeeded because PB15 was drawn.

The later VVD/HLR exact challenger `PB13 or PB16`, primary `13`, did not hit the main PowerBall. PB13 did occur in XTRA, but this was not a pre-draw XTRA-targeted forecast and must be recorded only as a cross-game observation.

## XTRA cross-score boundary

Against the frozen 20-line main-PowerBall slate, the XTRA result produced best main overlap **1/5**. Three frozen lines happened to carry PB13; the best of those had 1 main + PB.

The later 10-line HLR/PB13 challenger produced best XTRA overlap **2 mains + PB13**, not 3 mains + PB13. Any separate 3+PB line must be identified from a different frozen artifact before HEPS receives credit for it.

## HLR legacy diagnostic

The user-provided `Train on Main.xlsx` contains 811 legacy main-PowerBall draws from 2018-01-09 through 2025-10-17. It was used as a diagnostic prior only and is not an active mechanical-era dependency.

A fixed H/L/R motif classifier was trained on the first 600 chronological legacy draws and evaluated on the next 211. It underperformed the exact fair-draw modal direction implied by the current sorted-slot value in every slot:

| Slot | HLR motif accuracy | fair modal geometry |
|---|---:|---:|
| S1 | 65.9% | 74.4% |
| S2 | 67.8% | 71.6% |
| S3 | 65.4% | 77.3% |
| S4 | 62.1% | 73.9% |
| S5 | 62.6% | 74.9% |
| PB | 63.5% | 76.3% |

Therefore visual motif repetition is largely explained by ordinary order-statistic/boundary geometry and should not be promoted as a universal predictor.

However, when the frozen legacy motif rule is applied to the 14 mechanical-era targets for which sufficient HLR history exists, PB-direction accuracy is 9/14 versus 7/14 for the simple fair-modal direction. The motif rule provided two PB-direction corrections and no paired losses in this tiny sample. This is insufficient for significance or core promotion, but sufficient to retain a **PB directional challenger**.

## Candidate feature recall audit

Mechanical-era walk-forward, min_train=3, 16 evaluated targets. Mean winning-main recall for a 22-number candidate pool:

- hot: 2.000
- cold_void: 2.250
- stiction_shadow: 1.938
- pair_bridge: 2.000
- midfield: 2.125
- high_register: 2.250
- uniform random expectation: 2.200

No expert demonstrates a meaningful candidate-recall edge at this sample size. Do not retune weights aggressively from the 2026-08-04 miss.

## Architecture recommendation

1. Keep Pair-of-Pairs + Anchor unchanged as the Stage-C synthesizer.
2. Add a Stage-A **dual-pool recall guard**: a compact model core plus a broader specialist/rescue pool, scored separately.
3. Add Stage-B **scenario routing** rather than hard HLR filtering:
   - null-geometry H/L/R scenario;
   - HLR motif challenger scenario;
   - optional human/director motif scenario when frozen pre-draw.
4. For PowerBall, separate direction classification from exact-ball ranking and benchmark direction against the exact 1–16 combinatorial null conditional on the current PB value.
5. Keep entropy, sum, parity, adjacency and register rules soft; no hard vetoes.
6. Track machine identity when authoritative metadata are available; do not infer a PowerBall/XTRA machine swap from outcome similarity alone.

## Next-draw directional scenarios from 2026-08-04

Current sorted main line: `16,24,29,34,38`; PB15.

- Exact fair-modal slot geometry: **L — L — L — H — H | L**.
- Frozen legacy HLR motif challenger: **L — L — H — H — H | L**.

Only S3 differs between the two main-field scenarios. Both call PB lower than 15. For PB15, a lower next PB already has fair probability 14/16 = 87.5%, so a future `L` directional hit is not evidence of HLR edge by itself.
