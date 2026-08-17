# PowerBall XTRA — Cross-Lane VVD Motif Challenger Freeze

**Target:** Tuesday 2026-08-18  
**Mode:** `paper_trading_only`  
**Authority:** experimental challenger only  
**Evidence:** `INSUFFICIENT_EVIDENCE` unless explicitly rejected below  
**Data:** XTRA canonical ledger only through 2026-08-14  
**Main leakage:** none. Main values/motifs were not used to discover or parameterize this freeze.

This file does **not** replace or edit `powerball_xtra_pre_draw.md`. It is an independently frozen VVD-motif challenger to be scored separately after the draw.

## 1. Current state

Latest XTRA result: `7,27,28,46,48 | PB2`.

Current VVD state from 2026-08-11 -> 2026-08-14:

`S1=8 | S2=6 | S3=3 | S4=4 | S5=2 | PB=0`

Existing XTRA-only HLR/BARP challenger was independently frozen as:

`S1 H | S2 L | S3 L | S4 L | S5 H`

For PB, structural direction from PB2 strongly favours HIGH (14/16 values) but repeat remains possible.

Exact structural modal directions from current main coordinates are `L,L,L,L,L`; the learned HLR challenger therefore disagrees on S1 and S5. Both coordinate branches must remain visible.

## 2. Prospective direct-transition residual formulation

Historical diagnostic suggests pooled XTRA cross-lane VVD transitions may improve mode selection but damage full-distribution calibration at full strength. Therefore the prospectively frozen challenger is a **tempered residual**:

`P_challenger(VVD=d) ∝ P_structural(VVD=d | slot,current_coordinate) × LR_transition(d)^0.20`

where `LR_transition(d)` is the five-observation-shrunk pooled XTRA estimate of `P(next=d | current VVD) / P(next=d)` using only earlier XTRA VVD values.

`beta=0.20` was selected after retrospective diagnostics and receives zero historical predictive credit. Tuesday 2026-08-18 is its first prospective test.

## 3. Lane forecasts

### S1

CURRENT: coordinate7; VVD tail `5,5,8`.

XTRA-native support:
- direct `8→3` occurred 2/9 pooled transitions and is structurally plausible;
- algebraic VVD3 has 3 source lanes / 4 formula families;
- structural VVD mode is6;
- `8→21` has large empirical lift but structural `P(VVD21|S1=7)≈0.35%`, so it is rejected as primary.

FORECAST:
- primary motif VVD **3**;
- secondary **6**;
- matrix-convergence hedge **10**.

HLR:
- learned challenger HIGH -> VVD3 gives **S1=10**;
- exact structural direction is nearly balanced and slightly LOW -> VVD3 gives **S1=4**.

Evidence: `INSUFFICIENT_EVIDENCE`.

### S2

CURRENT: coordinate27; VVD tail `9,10,6`.

XTRA-native support:
- direct **6→8** occurred 3/8 pooled transitions; raw lift4.5, shrunk lift≈3.15;
- direct 6→7 occurred2/8;
- algebraic matrix-wide VVD10 is a separate hedge.

FORECAST:
- primary VVD **8**;
- secondary **7**;
- algebraic hedge **10**.

HLR LOW -> coordinates:
- VVD8 -> **19**;
- VVD7 -> **20**;
- VVD10 -> **17**.

Evidence: `INSUFFICIENT_EVIDENCE`, but S2 direct transfer is one of the cleaner current XTRA-native motifs.

### S3

CURRENT: coordinate28; VVD tail `0,10,3`.

XTRA-native support:
- direct **3→3** occurred4/14 pooled transitions;
- direct 3→11 occurred2/14;
- algebraic VVD3 has 3 source lanes /4 families;
- reflection: historical XTRA PB triples `1,3,10` and `7,3,10` make current S3 suffix `10,3` a reverse partial, generating reflected candidates VVD1 and VVD7.

FORECAST:
- primary VVD **3**;
- secondary direct VVD **11**;
- reflected challengers **1 / 7**;
- algebraic hedge **10**.

HLR LOW -> coordinates:
- d3 -> **25**;
- d11 -> **17**;
- d1 -> **27**;
- d7 -> **21**;
- d10 -> **18**.

Reflection itself is `REJECT` as an active predictive expert after blind controls; 1/7 are logged only as experimental candidates. Overall lane evidence: `INSUFFICIENT_EVIDENCE`.

### S4

CURRENT: coordinate46; VVD tail `10,4,4`.

XTRA-native support:
- direct **4→7** occurred2/9 pooled transitions;
- algebraic matrix-wide VVD10 is strongly generated in the current field;
- exact structural VVD mode is1.

FORECAST:
- primary motif VVD **7**;
- secondary algebraic VVD **10**;
- structural control VVD **1**.

HLR LOW -> coordinates:
- d7 -> **39**;
- d10 -> **36**;
- d1 -> **45**.

Evidence: `INSUFFICIENT_EVIDENCE`.

### S5

CURRENT: coordinate48; VVD tail `3,3,2`.

XTRA-native support:
- direct `2→2` occurred2/9;
- direct `2→5` occurred2/9 and has larger residual lift but conflicts with the learned HIGH branch because 48+5 is illegal;
- reflection of historical S5 `2,2,3` from current suffix `3,2` generates VVD2;
- algebraic support also generates VVD2;
- exact structural `P(VVD2|S5=48)≈17.0%`, making2 a high-base-rate value.

FORECAST:
- primary VVD **2**;
- secondary structural VVD **1**;
- LOW-only direct challenger VVD **5**.

Coordinates:
- learned HLR HIGH: d2 -> **50**, d1 -> **49**;
- exact structural HLR LOW: d2 -> **46**, d1 -> **47**, d5 -> **43**.

Because much of the d2 agreement is explained by structural base rate, evidence remains `INSUFFICIENT_EVIDENCE`.

### PB

CURRENT: PB2; VVD tail `7,4,0`.

XTRA-native support:
- pooled cross-lane direct **0→10** occurred2/6 times; raw lift4.0, shrunk lift≈2.64;
- current algebraic VVD10 is the matrix's strongest closure: 4 source lanes, 5 non-equivalent formula families, 6 paths;
- same-PB historical VVD0 successors were14,6,8, so the PB lane itself does not replicate 0→10;
- structural PB VVD mode from PB2 is1.

FORECAST:
- primary **motif challenger VVD10**;
- structural control **VVD1**;
- same-PB zero-state hedges **VVD8 / VVD6 / VVD14**.

With HIGH direction from PB2:
- d10 -> **PB12**;
- d1 -> **PB3**;
- d8 -> **PB10**;
- d6 -> **PB8**;
- d14 -> **PB16**.

VVD10 is `INSUFFICIENT_EVIDENCE`: the current convergence is unusual, but an equally strong some-value convergence occurs in ~6.1% of histogram-preserving randomized matrices and generic algebraic prediction failed the historical proper-score test.

## 4. Current multipath hierarchy

| VVD | Algebraic source lanes | Algebraic families | Additional current structures | Interpretation |
|---:|---:|---:|---|---|
| **10** | **4** | **5** | direct support in PB and S3 | strongest current matrix-wide challenger |
| **3** | 3 | 4 | direct support in S1/S3 | practical S1/S3 challenger |
| **6** | 3 | 3 | PB direct support | mostly structural/common-value support |
| **2** | 2 | 2 | S5 direct + S5 reflection | strongest S5 confluence, but high structural base rate |
| **7** | 2 | 2 | S2/S4 direct + S3 reflection | secondary cross-lane challenger |
| **11** | 2 | 3 | S3 direct | secondary S3/PB-area magnitude |

Multipath counts are not interpreted as independent votes.

## 5. FCPC full-field challenger

The direct-transition residual is mapped from slot VVD distributions to 1-50 marginal coordinate probabilities by modifying each exact structural slot-coordinate distribution with `LR^0.20`, normalizing each slot to mass1, then summing across S1-S5. The resulting vector sums exactly to5 and is frozen separately in:

`cycles/2026-08-18/xtra_vvd_cross_lane_fcpc_vector.json`

Derived Top13, used only as Gate-2 compression:

`{1,3,4,17,19,22,25,31,39,43,46,48,50}`

Probability ranking:

`31 > 39 > 50 > 46 > 43 > 19 > 1 > 22 > 4 > 25 > 3 > 17 > 48`

This Top13 does not replace the incumbent XTRA K13 and must be scored as a separate challenger.

## 6. Prospective scoring

After the 2026-08-18 draw, score independently:

1. VVD magnitude per lane;
2. HLR direction per lane;
3. exact coordinate conditional on pre-frozen direction;
4. direct-transition full VVD log/Brier score versus exact structural VVD;
5. FCPC 1-50 marginal log/Brier score versus flat0.1;
6. derived Top13 winner recall;
7. reflected candidates separately with no authority;
8. algebraic VVD10 convergence separately;
9. incumbent Tuesday XTRA forecast separately.

No post-draw modification of beta, grammar, transition shrinkage, reflection rule, or selected VVD candidates is permitted.
