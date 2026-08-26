# PowerBall XTRA — Frozen Pre-Draw Forecast

**Target:** Friday 2026-08-28  
**Mode:** `paper_trading_only`  
**Working latest result:** `4,7,15,18,29 | PB16` from Tuesday 2026-08-25, draw 1749. Publicly corroborated; official single-source repository verification remains pending.  
**Latest VVD:** `13,16,22,21,19 | PB14`  
**Architecture:** E0010 acquisition-preservation + E0011 joint HLR-conditioned magnitude regimes

## 1. Direction freeze

Exact structural direction probabilities from the current sorted state:

- S1 from4: L 27.60%, R 7.70%, H **64.70%**
- S2 from7: L 10.30%, R 3.49%, H **86.20%**
- S3 from15: L 12.62%, R 2.56%, H **84.83%**
- S4 from18: L 4.00%, R 1.03%, H **94.97%**
- S5 from29: L 4.64%, R 0.97%, H **94.40%**
- PB from16: L **93.75%**, R 6.25%, H 0%

Primary vector: **H,H,H,H,H | L**.

The exact structural probability of all five main slots moving HIGH is about **56.90%**. Including PB LOW gives roughly **53.34%**. This is therefore a high-base-rate direction event, not a rare predictive claim.

Shadow diagnostics also lean HIGH after the current main-slot `...HL` endings: pooled two-step `HL` continuations are H 24, L 14, R 1. S1 current three-step `RHL` resolved H 4/6 in pooled history; S2-S5 current `LHL` resolved H 9/13. PB current `HLH` is mixed, but H is impossible from PB16; among feasible L/R continuations, LOW dominates.

## 2. Joint HHHHH conditional structural field

Exact enumeration of all legal 5/50 combinations satisfying the frozen HHHHH event yields about 1,205,484 combinations.

Conditional slot means:

- S1 12.46
- S2 20.93
- S3 29.14
- S4 36.64
- S5 44.08

Conditional medians:

`11,20,29,37,45`

Modal/high-density neighborhoods:

- S1: 5/6/7, then8/9/10/11
- S2: 17/16/18/19/15/20
- S3: 28/27/29/26/30/31
- S4: 39/40/38/41/37/42
- S5: 50/49/48/47/46

Conditional sum quantiles:

- 50th: 142
- 75th: 160
- 85th: 170
- 90th: 176
- 95th: 186

E0011 therefore reserves explicit HIGH-expansion exposure in the 85th–95th percentile sum regime rather than centering every line near the ordinary mean.

## 3. VVD / algebraic residuals

Current VVD state: `13,16,22,21,19 | PB14`.

### S1
Same-lane d13 historical successors: d8 and d7 -> under HIGH from4 gives **12/11**.

Latest VVD triple `(0,10,13)` algebraically produces d10 (two families) ->14, d3->7, and deeper d23/d26 ->27/30. Joint structure, density and Coulomb also favor5/6/7.

Primary hierarchy: **7 > 11/12 > 5/6 >14**.

### S2
Same-lane d16 successor: d12 -> **19**.

Latest triple `(16,12,16)` also generates d12 twice ->19, d16->23, d20->27 and d4->11. Terminal-digit history from ending7 gives20/11. Joint structural mode is17.

Primary hierarchy: **19 > 20/17/16 >23 >11/27**.

### S3
Same-lane d22 successor: d24 ->39. Pooled d22 successors include d14->29, d18->33, d4->19 and d24->39.

Latest triple `(10,19,22)` generates d13->**28**, d9->24, d7->22, d1->16, plus deeper46/44/49 branches. Joint structural mode is28 and density supports27/31/32.

Primary hierarchy: **28/27 >29/31/32 >39 >24**.

### S4
Same-lane d21 successor: d1 ->19; pooled d21 also gives d15->33.

Latest triple `(20,13,21)` generates d22->40, d27->45, d28->46, d14->32, d12->30, d7->25. Terminal-digit history from ending8 gives45/39/35. Joint mode is39.

Primary hierarchy: **39 >40/35 >45/46 >33 >19**.

### S5
No completed same-lane d19 successor. Latest triple `(17,17,19)` gives d19 twice ->**48**, d17->46, d15->44, d21->50. Density is strongest at47/48; joint structural mode is50.

Primary hierarchy: **48 >46/50/47 >44**.

## 4. PowerBall

Current PB=16, current PB VVD14, direction LOW.

Completed exact PB16 successors are `16,10`; conditioning on LOW leaves **PB10** as the exact-state successor.

Same-PB d14 historical successors include d11 and d0; under LOW the d11 path gives **PB5**.

Latest PB VVD triple `(10,10,14)` algebraically generates d6->PB10, d10->PB6, d14->PB2, plus repeat d0.

Thus PB10 has two distinct prospective routes: exact-state PB16->10 and algebraic d6. Ranking:

**PB10 > PB5 > PB6 > PB2 > PB16 repeat**.

## 5. Initial acquisition objective

The broad acquisition field is deliberately larger than final compression because the research objective is to acquire all five winning main coordinates before assembly.

### Broad Acquisition K25

`{5,6,7,11,12,16,17,18,19,20,21,23,27,28,29,31,32,35,39,40,43,45,46,48,50}`

This basket preserves joint structural modes/medians, direct-VVD candidates, algebraic rescues, terminal/density support, and expansion-regime coordinates. K25 is an acquisition experiment, not a final betting pool. A fixed random K25 contains all five winners only about 2.51% of the time.

## 6. E0011 expansion-regime lines

The frozen HHHHH 85th–95th percentile sum band is approximately 170–186. Splitting this prospectively into three fixed sub-bands gives deterministic median representatives:

1. sum170–174: `17,29,37,43,48`
2. sum175–179: `19,30,38,43,48`
3. sum180–186: `21,32,39,44,48`

These are regime-insurance lines only and receive no special authority.

## 7. Frozen prediction slates

### Flagship residual-convergence
**7,19,28,39,48 | PB10**

### Joint-structural central
**11,20,29,37,45 | PB10**

### Direct-VVD / bridge
**12,19,28,39,48 | PB5**

### Density / terminal hedge
**7,20,32,39,47 | PB10**

### Algebraic hedge
**14,19,28,40,48 | PB6**

### Stiction/Coulomb
**5,8,16,19,30 | PB10**

### Expansion 85–88%
**17,29,37,43,48 | PB10**

### Expansion 88–92%
**19,30,38,43,48 | PB5**

### Expansion 92–95%
**21,32,39,44,48 | PB6**

## 8. Primary exact calls

- S1 **7**
- S2 **19**
- S3 **28**
- S4 **39**
- S5 **48**
- PB **10**

# Flagship: **7,19,28,39,48 | PB10**

## 9. Evidence status

All main-number mechanisms remain `INSUFFICIENT_EVIDENCE` / `PROVISIONAL_SIGNAL`. E0011 is a new prospective architecture and has zero retrospective validation credit from the 2026-08-25 motivating failure. The acquisition K25 is evaluated first on 5/5,4/5,3/5 winner recall against matched random exposure; assembly is evaluated only after acquisition. PB10 is a primary research call, not a guaranteed outcome.
