# PowerBall XTRA — Frozen Pre-Draw Cycle

**Target:** Friday 2026-08-14  
**Mode:** `paper_trading_only`  
**XTRA dataset:** 21 canonical draws, 2026-06-02 through 2026-08-11  
**Canonical ledger:** `data/powerball_xtra_history.jsonl`  
**Architecture:** `core/powerball_xtra_architecture.md`

## Pre-draw correction log

At **2026-08-14 08:56 SAST**, before the target draw, the project director corrected a transcription error in the human PowerBall forecast. The intended forecast is **PB HIGH (>2)**, not PB LOW. The earlier PB-L wording is retained in Git history for auditability; this file records the corrected prospective hypothesis before the draw.

## Isolation declaration

This forecast uses South African PowerBall XTRA rows from 2026-06-02 onward only. No pre-June PowerBall Plus/XTRA history and no Main PowerBall learned state or fitted parameter is used.

## Frozen human HLR forecast — corrected pre-draw

Project-director forecast supplied before the draw:

`S1 L | S2 L | S3 L | S4 H/L unresolved | S5 L | PB H`

Relative to the 2026-08-11 XTRA result:

`15, 21, 31, 42, 50 | PB 2`

this means:

- S1 < 15
- S2 < 21
- S3 < 31
- S4 < 42 or > 42; repeat 42 is not the forecast
- S5 < 50
- PB > 2, therefore the human directional PB candidate range is **3-16**

## Red-team calibration

Under the exact 5-of-50 order-statistic structural null at the current thresholds:

- P(S1 < 15) = 82.21%
- P(S2 < 21) = 67.41%
- P(S3 < 31) = 69.00%
- P(S4 < 42) = 78.39%
- P(S4 > 42) = 17.59%
- P(S5 < 50) = 90.00%

The joint all-main-low geometry `S1<15, S2<21, S3<31, S4<42, S5<50` occupies about 47.19% of the legal 5/50 combination space. Therefore the main-field L calls are not, by themselves, evidence of predictive edge.

PB-H from PB2 is broad: under a uniform 1-16 null, 14 of 16 values are higher than 2, so `P(PB > 2) = 87.5%`. Direction alone is therefore weak evidence; exact-ball ranking remains the harder problem.

### Descriptive XTRA HLR evidence

- S1 and S5 have matched H/L direction on the last eight observed transitions; across all 20 XTRA transitions they match 13/20 (65%). Treat as a prospective hypothesis, not proof.
- S1: after an `HH` suffix, historical next directions are L=3, H=1; the current `HHH` suffix has not previously occurred.
- S2: after H, next directions are L=6, H=4.
- S3: after H, next directions are L=5, H=3, R=1.
- S4: after L, next directions are H=5, L=4. Sequence evidence is effectively ambiguous; structural-null geometry favors L.
- S5: after H, next directions are L=6, H=3, R=1; current `HHH` suffix has not previously occurred.
- PB: the two previous observed occurrences of PB2 were followed by **PB12** and **PB16**, both HIGH. This agrees with the corrected human PB-H call but is only two observations and is not sufficient evidence of a transition law.

## Primary directional resolution

HEPS retains the human HLR forecast as a frozen expert output but resolves the S4 portfolio weight toward **LOW**, because the current order-statistic geometry heavily favors S4<42 and the short transition history does not provide sufficient evidence to override that base rate.

Portfolio allocation: 17 S4-L lines / 3 S4-H challenger lines.

## XTRA K=13 candidate basket

`{3, 5, 10, 14, 16, 20, 21, 23, 29, 36, 44, 46, 47}`

Rationale is a soft ensemble of XTRA-only slot density, recency, +/-1/2 shadow support, repeated-pair support, HLR feasibility, and morphology. No candidate is claimed to have a mathematically elevated lottery probability.

Repeated-pair support inside this basket includes `5-20`, `5-21`, `21-46`, `21-47`, `46-47`, `14-16`, `16-47`, and `23-44`, each observed twice in the 21-draw XTRA sample.

## Corrected frozen 20-line paper-trading slate

Main-number combinations are unchanged from the earlier pre-draw freeze. Only PB allocation is corrected to respect the intended **PB > 2** hypothesis.

| # | S1 | S2 | S3 | S4 | S5 | PB | S4 branch |
|---:|---:|---:|---:|---:|---:|---:|:---:|
| 1 | 5 | 16 | 21 | 36 | 47 | **12** | L |
| 2 | 5 | 20 | 21 | 36 | 46 | **16** | L |
| 3 | 14 | 16 | 21 | 23 | 47 | **15** | L |
| 4 | 5 | 20 | 21 | 23 | 44 | **12** | L |
| 5 | 10 | 20 | 21 | 29 | 47 | **16** | L |
| 6 | 5 | 10 | 21 | 23 | 47 | **15** | L |
| 7 | 3 | 16 | 29 | 36 | 47 | **12** | L |
| 8 | 10 | 14 | 21 | 36 | 46 | **16** | L |
| 9 | 3 | 16 | 21 | 23 | 46 | **15** | L |
| 10 | 5 | 16 | 21 | 29 | 44 | **5** | L |
| 11 | 10 | 16 | 23 | 36 | 44 | **13** | L |
| 12 | 3 | 20 | 23 | 36 | 47 | **4** | L |
| 13 | 3 | 10 | 21 | 36 | 44 | **6** | L |
| 14 | 5 | 14 | 16 | 20 | 47 | **10** | L |
| 15 | 14 | 20 | 29 | 36 | 44 | **14** | L |
| 16 | 3 | 14 | 21 | 29 | 46 | **8** | L |
| 17 | 10 | 16 | 20 | 29 | 46 | **11** | L |
| 18 | 5 | 16 | 21 | 46 | 47 | **12** | H |
| 19 | 10 | 20 | 21 | 46 | 47 | **16** | H |
| 20 | 14 | 16 | 21 | 44 | 47 | **15** | H |

## Flagship nucleus — corrected PB allocation

Primary XTRA line:

`5 / 16 / 21 / 36 / 47 | PB 12`

Secondary:

`5 / 20 / 21 / 36 / 46 | PB 16`

Third:

`14 / 16 / 21 / 23 / 47 | PB 15`

## PB interpretation

The explicit human hypothesis is **PB HIGH (>2)**. This is directionally consistent with the only two previous PB2 transitions in the June-August XTRA ledger, which moved to PB12 and PB16. Because two observations are far too few to establish a transition rule, HEPS treats **12 and 16 as protected successor-resonance lanes**, not as validated predictions. PB15 receives additional exposure from recent-frequency support, while the remaining HIGH values provide diversification across the slate.

This is a frozen prospective experiment, not evidence of a durable predictive edge.
