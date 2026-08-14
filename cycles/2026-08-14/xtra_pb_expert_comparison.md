# PowerBall XTRA — PB Expert Comparison

**Target:** Friday 2026-08-14  
**Mode:** `paper_trading_only`  
**Dataset boundary:** XTRA only, 2026-06-02 through 2026-08-11  
**Purpose:** compare independent PB experts prospectively; no single pattern has veto authority.

## Frozen expert outputs

| Expert / lane | Frozen output | Interpretation |
|---|---|---|
| Human HLR | **HIGH from PB2** | PB in 3-16; broad directional call |
| Tier oscillator | **PB > 10** | PB in 11-16 |
| Piecewise arithmetic resolver | **PB11** | exact challenger: current block `13 -> 6 -> 2`, primary rule `6+2+3=11` |
| PB2 successor-resonance | **PB12 / PB16** | the two prior PB2 observations in the active XTRA sample were followed by 12 and 16 |
| XTRA frequency/recency support | **PB15** | 15 is the most frequent teen PB in the 21-draw XTRA sample and is retained as a hedge, not a probability claim |
| First-order VVD transition analog | **PB9** | current VVD magnitude is `abs(6-2)=4`; the only prior completed case with VVD=4 was followed by VVD=7, so with HLR HIGH from PB2 the analog gives `2+7=9` |
| VVD central-magnitude baseline | **PB8-9** | historical XTRA PB absolute movement median is 6.5; with HLR HIGH from PB2 this maps approximately to 8-9 |

## Agreement map

### Strong agreement on direction/tier

- Human HLR says HIGH from 2.
- Tier oscillator narrows this to 11-16.
- PB2 successor-resonance points to 12/16.
- Arithmetic resolver gives 11.
- Frequency/recency hedge gives 15.

These lanes concentrate on **11, 12, 15, 16**.

### Deliberate disagreement

The magnitude-only VVD lanes currently favor a smaller upward move, approximately **PB8-9**, and therefore disagree with the >10 tier hypothesis and the arithmetic PB11 call.

This disagreement must be preserved. Do not alter VVD after the draw to force convergence.

## Pre-draw confidence interpretation

The expert ensemble does **not** justify calling PB11 high-confidence in an absolute statistical sense. It does justify treating PB11 as the primary exact arithmetic challenger because it lies inside the independently predicted >10 tier.

Protected exact PB set for comparative scoring:

`{11, 12, 15, 16}`

Dissent/control set:

`{8, 9}`

## Post-draw scoring rule

After the result:

1. score each expert independently against its frozen output;
2. distinguish directional/tier hit from exact-ball hit;
3. update an expert ledger with prospective hits/misses and denominators;
4. do not reward an expert merely because another expert overlapped its candidate set;
5. compare calibration and exact-ball accuracy over repeated future draws before changing authority.

The purpose of consensus is ranking confidence; the purpose of disagreement is model selection evidence.