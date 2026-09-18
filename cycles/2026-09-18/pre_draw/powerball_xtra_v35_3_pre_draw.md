# HEPS XTRA Pre-Draw — 2026-09-18

**Architecture:** HEPS v35.3 methodology transfer with XTRA-fitted state only  
**Mode:** paper trading / research  
**Data boundary:** XTRA Mechanical Era only, 2026-06-02 through 2026-09-15  
**Rows:** 31  
**Previous XTRA draw:** 5,16,24,36,49 | PB16  
**Provenance:** operational ledger complete through 2026-09-15; recent rows independently corroborated and retained with `pending_official_source_verification`.

## 1. Transition state

Current realized HLR entering this target: `LLLLH`.

Per-slot E0018-style successor HLR posterior:

| Slot | Previous | Conditioning | LOW | REPEAT | HIGH |
|---|---:|:---:|---:|---:|---:|
| S1 | 5 | L | 22.88% | 7.90% | 69.22% |
| S2 | 16 | L | 32.54% | 6.97% | 60.50% |
| S3 | 24 | L | 47.66% | 1.16% | 51.17% |
| S4 | 36 | L | 40.72% | 1.30% | 57.99% |
| S5 | 49 | H | 62.95% | 7.05% | 30.00% |

Top joint HLR mixture states after exact legal-line coupling:

1. HHHHL — 15.783%
2. LLLLL — 11.404%
3. HLLLL — 7.689%
4. HHHLL — 7.370%
5. HHHHH — 5.513%
6. HHHHR — 3.662%
7. HHLLL — 3.469%
8. LHHHL — 2.944%

No HLR vector is a hard gate.

## 2. Frozen XTRA K13

Scenario-preserving slot-routed challenger:

`{1,7,13,16,18,26,27,37,38,39,40,48,50}`

It preserves at least one legal line for each of the four highest-mass HLR scenarios while remaining K=13.

Complete-line mass under the XTRA full-mixture field:

- challenger K13: 0.00071214
- uniform K13 line-space mass: 0.00060743
- internal model/null mass ratio: 1.1724x

This ratio is an internal model-allocation diagnostic, not evidence of a real lottery edge.

Slot provenance:

| Number | Primary slot | Secondary slot |
|---:|:---:|:---:|
| 1 | S1 | — |
| 7 | S1 | S2 |
| 13 | S2 | S1 |
| 16 | S2 | S3 |
| 18 | S2 | S3 |
| 26 | S3 | S2 |
| 27 | S3 | S4 |
| 37 | S4 | S3 |
| 38 | S4 | S5 |
| 39 | S4 | S5 |
| 40 | S4 | S5 |
| 48 | S5 | S4 |
| 50 | S5 | — |

Bounded reserves, kept outside K13: `3@S1, 19@S2, 28@S3, 35@S4, 47@S5`.

Evidence: **INSUFFICIENT_EVIDENCE / prospective shadow**.

## 3. Candidate-frozen Pattern-OR

All `C(13,5)=1,287` lines were enumerated.

XTRA-fitted adaptive lanes:
- HLR residual;
- LDSAD residual;
- SUMAD residual;
- SPANAD residual.

No Main fixed LDSAD/SUMAD/SPANAD band was imported.

Using the v35.3 conservative 80%-style Pattern-OR shadow:
- retained: **1,037 / 1,287**
- shadow-eliminated: **250**
- retained fraction: **80.57%**
- retained E0018 line-mass fraction: **82.85%**

This remains shadow triage only; no production hard-pruning authority.

No XTRA fixed pattern band is promoted. Any attractive fixed band identified from the existing XTRA outcomes now is **POST-HOC DISCOVERY / INSUFFICIENT_EVIDENCE**.

## 4. Top 20 XTRA combinations

Because XTRA spectral transfer was rejected and raw-pair assembly has no promoted authority, lines are ordered by the coherent XTRA E0018 legal-line residual weight after the Pattern-OR shadow gate. Tie handling is deterministic.

| Rank | Main numbers | HLR | Pattern-OR pct |
|---:|---|:---:|---:|
| 1 | 7,16,18,37,50 | HRLHH | 0.9965 |
| 2 | 7,16,18,38,50 | HRLHH | 0.9965 |
| 3 | 7,16,18,39,50 | HRLHH | 0.9965 |
| 4 | 7,16,18,40,50 | HRLHH | 0.9965 |
| 5 | 7,16,18,48,50 | HRLHH | 0.9965 |
| 6 | 13,16,18,37,50 | HRLHH | 0.9965 |
| 7 | 13,16,18,38,50 | HRLHH | 0.9965 |
| 8 | 13,16,18,39,50 | HRLHH | 0.9965 |
| 9 | 13,16,18,40,50 | HRLHH | 0.9965 |
| 10 | 13,16,18,48,50 | HRLHH | 0.9965 |
| 11 | 7,16,40,48,50 | HRHHH | 0.9844 |
| 12 | 13,16,38,40,50 | HRHHH | 0.9662 |
| 13 | 13,16,40,48,50 | HRHHH | 0.9662 |
| 14 | 7,16,26,37,50 | HRHHH | 0.9114 |
| 15 | 7,16,26,38,50 | HRHHH | 0.9114 |
| 16 | 7,16,26,39,50 | HRHHH | 0.9114 |
| 17 | 7,16,26,40,50 | HRHHH | 0.9114 |
| 18 | 7,16,26,48,50 | HRHHH | 0.9114 |
| 19 | 7,16,27,37,50 | HRHHH | 0.9114 |
| 20 | 7,16,27,38,50 | HRHHH | 0.9114 |

**XTRA coalition authority remains: INSUFFICIENT_EVIDENCE / no promoted predictive XTRA assembler.**

## 5. Final 10-line portfolio

E0022 `four_plus_first` Johnson geometry is applied only after K13 freeze. Model/pattern support is used only as a tie-break. The ten-line portfolio covers 410/1287 = **31.86%** of possible K13 winner states at 4+/5; this is deterministic geometry, not prediction.

1. **7,16,18,37,50 | PB10**
2. **13,16,38,40,50 | PB10**
3. **7,27,38,39,50 | PB2**
4. **18,26,27,40,50 | PB6**
5. **26,37,39,48,50 | PB2**
6. **1,16,27,48,50 | PB15**
7. **13,16,18,39,48 | PB8**
8. **7,16,26,39,40 | PB12**
9. **7,37,38,40,48 | PB16**
10. **13,18,26,37,38 | PB11**

### Flagship

**7,16,18,37,50 | PB10**

## 6. XTRA PowerBall

E0015 tau=4 conditional-convergence shadow, fitted only on XTRA through 2026-09-15.

Current state:
- PB = 16
- current VVD = 0
- current HLR = REPEAT

Ranking:

1. PB10 — 21.85%
2. PB2 — 17.02%
3. PB6 — 9.74%
4. PB15 — 8.95%
5. PB8 — 8.04%
6. PB12 — 5.49%
7. PB16 — 5.07%
8. PB11 — 4.59%
9. PB13 — 3.88%
10. PB5 — 3.68%

Primary: **PB10**.

Evidence: **PROVISIONAL_SIGNAL / shadow**. Prior prospective observations include negative proper-score targets, so this is not promoted authority.

## 7. Supersession

The latest prior frozen XTRA slate is the 2026-09-01 slate. It is **superseded for the 2026-09-18 target** because four newer XTRA draws have changed the transition state and fitted XTRA history. This is not a claim that v35.3 has established predictive superiority.

All Main fitted state remains excluded.
