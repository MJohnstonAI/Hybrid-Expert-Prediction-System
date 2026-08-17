# HEPS Prediction Delivery — Friday 7 August 2026

**Status:** PRE-DRAW FROZEN / PAPER TRADING ONLY  
**Training cut-off:** 4 August 2026  
**Active rows:** 19  
**Architecture:** HEPS v34 + Candidate Lattice v0.1 shadow overlay

## Frozen directional state

Previous main draw: `16, 24, 29, 34, 38`.

Mandatory independent HLR forecast:

`H-L-H-H-L`

The joint flow-feasibility layer does not overwrite this forecast. It supplies rescue scenarios because the independent vector is highly constrained by the ascending-slot rule.

Top joint rescue vectors:

`LLHHH, LLLHH, LHHHH, HLHHH, LLLLH, HHHHH, LLLLL, HLLHH`.

PowerBall previous value: `15`.

PowerBall shadow model favours **LOW**, with strongest candidates `11, 12, 10, 9, 13`. Across the 20-line portfolio all 16 PowerBall values are covered at least once; `11, 12, 10, 13` receive duplicate exposure.

## 20-line frozen slate

| Rank | Main numbers | PB | Flow | Lane |
|---:|---|---:|---|---|
| 1 | **21 22 35 36 37** | **11** | HLHHL | committed HLR |
| 2 | **22 23 35 36 37** | **12** | HLHHL | committed HLR |
| 3 | **20 21 34 36 37** | **10** | HLHHL | committed HLR |
| 4 | **19 23 34 35 37** | **13** | HLHHL | committed HLR |
| 5 | **4 12 34 43 47** | **9** | LLHHH | joint rescue |
| 6 | **6 18 36 44 48** | **8** | LLHHH | joint rescue |
| 7 | **8 20 38 45 49** | **14** | LLHHH | joint rescue |
| 8 | **10 22 40 46 50** | **16** | LLHHH | joint rescue |
| 9 | **3 11 21 43 47** | **15** | LLLHH | joint rescue |
| 10 | **5 13 23 44 48** | **7** | LLLHH | joint rescue |
| 11 | **7 17 22 45 49** | **6** | LLLHH | joint rescue |
| 12 | **4 26 35 43 47** | **5** | LHHHH | joint rescue |
| 13 | **9 27 37 45 50** | **4** | LHHHH | joint rescue |
| 14 | **19 21 34 43 47** | **3** | HLHHH | joint rescue |
| 15 | **20 23 38 45 49** | **2** | HLHHH | joint rescue |
| 16 | **4 12 21 30 47** | **1** | LLLLH | joint rescue |
| 17 | **17 25 34 43 47** | **11** | HHHHH | joint rescue |
| 18 | **4 12 21 30 36** | **12** | LLLLL | joint rescue |
| 19 | **18 20 23 43 47** | **10** | HLLHH | joint rescue |
| 20 | **5 18 31 33 47** | **13** | LLHLH | diversity rescue |

## Candidate exposure

The 20 lines expose 38 distinct main numbers. That is intentionally wider than the earlier goal of a 20-30-number flat base because current active-era evidence does not justify aggressive exclusion at that level. Compression comes primarily from slot direction, VVD feasibility and ascending-path constraints rather than from pretending 12-20 numbers can already be safely vetoed.

## Research warning

Candidate Lattice v0.1 is **not validated as an edge**. In a quick non-confirmatory replay on 28 July, 31 July and 4 August, the actual full HLR flow vector ranked 3rd, 8th and 8th among 243 scenarios, but the first direct 20-line ranker still failed to produce a 3+ line on those targets. The Friday slate is therefore a clean prospective shadow test whose post-draw value is primarily diagnostic.

Do not alter this report after the target result is known.
