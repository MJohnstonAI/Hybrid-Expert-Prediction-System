# PowerBall XTRA — Physics of Failure

**Draw:** Tuesday 2026-08-25  
**Verified public result:** `4,7,15,18,29 | PB16`  
**Draw number:** 1749  
**Mode:** `paper_trading_only`

## 1. Result and transition

Previous XTRA state:

`17,23,37,39,48 | PB2`

Actual HLR:

`L,L,L,L,L | H`

Actual VVD:

`[13,16,22,21,19] | PB14`

The frozen flagship was:

`7,21,24,36,46 | PB12`

with primary VVD magnitudes approximately:

`[10,2,13,3,2] | PB10`.

Direction was correct; magnitude was systematically too small.

## 2. HLR layer — correct but low information

The frozen structural vector was exactly:

`L,L,L,L,L | H`.

It matched all six lanes.

However, exact 5/50 structural counting from the previous state gives about **45.42%** probability that all five sorted slots are lower. PB>2 has structural probability **87.5%**. The combined structural frequency of `LLLLL|H` is therefore about **39.75%**.

Verdict: **directional hit, but not rare enough to establish predictive information.** The important failure happened downstream in magnitude selection.

## 3. Magnitude failure

Actual versus flagship VVD:

| Lane | Frozen primary VVD | Actual VVD | Error |
|---|---:|---:|---:|
| S1 | 10 | 13 | +3 |
| S2 | 2 | 16 | +14 |
| S3 | 13 | 22 | +9 |
| S4 | 3 | 21 | +18 |
| S5 | 2 | 19 | +17 |
| PB | 10 | 14 | +4 |

The main-slot actual mean VVD was **18.2**, versus **6.0** for the flagship.

This was not random lane-by-lane noise. HEPS selected an all-LOW direction and then repeatedly chose small-to-moderate displacements, especially in S2/S4/S5. The draw instead produced a coordinated large-displacement collapse.

Pooled direct-transition history also had little ability to foresee these exact magnitudes:

- current S1 VVD10 -> actual13: unseen in prior pooled VVD10 successors;
- S2 VVD12 -> actual16: no completed pooled predecessor sample;
- S3 VVD19 -> actual22: no completed pooled predecessor sample;
- S4 VVD13 -> actual21: unseen after prior VVD13 states;
- S5 VVD17 -> actual19: unseen after prior VVD17 states;
- PB VVD10 -> actual14: previously observed once and was a secondary path.

Verdict: **short-state direct-transition tables were sparse and over-confident at the point-estimate layer.**

## 4. Joint structural conditioning was underused

Once `LLLLL` was frozen, the correct structural control was not five independent LOW translations. Exact enumeration conditional on all five current coordinates moving LOW gives approximate conditional means:

- S1: **5.84**
- S2: **12.18**
- S3: **20.03**
- S4: **27.92**
- S5: **37.96**

The flagship `7,21,24,36,46` remained materially too high in S2, S4 and S5 relative even to this joint all-LOW control.

Actual coordinates `4,7,15,18,29` were deeper still. Their slotwise conditional CDF positions under the all-LOW structural control were approximately:

- S1=4: 46th percentile or lower;
- S2=7: 22nd percentile;
- S3=15: 27th percentile;
- S4=18: 10th percentile;
- S5=29: 12th percentile.

The architecture therefore needs a **joint HLR-conditioned magnitude field** before residual experts are applied.

## 5. Morphology / sum-regime failure

Actual main-number sum:

`4+7+15+18+29 = 73`.

Before this draw, the active June-2026+ XTRA series had:

- mean sum about **138.1**;
- median **137**;
- previous minimum **93**.

So 73 set a new active-series low by **20 points** and was about **2.44 historical-sample standard deviations** below the previous mean.

Under the exact exchangeable 5/50 null, `P(sum <= 73)` is about **4.03%**. Conditional on the already-correct all-LOW event, `P(sum <= 73 | all five LOW)` rises to about **8.80%**.

This is a key Physics-of-Failure result: a deep-compression outcome was a tail scenario, but not so rare that HEPS should have had zero dedicated exposure to it.

The pre-draw morphology panel explicitly preferred ordinary 134–142 sum families. Although morphology had no hard veto, the slate population was effectively centered around ordinary sums. A **deep-compression chaos lane** was missing.

## 6. Candidate acquisition and E0010

Frozen Core FCPC K13:

`{3,7,8,10,11,13,31,32,36,41,42,44,47}`

Actual intersection:

`{7}` = **1/5**.

Frozen Specialist Reserve:

`{7,9,13,21,24,25,30,31,36,42,44,46}`

Actual intersection:

`{7}` = **1/5**.

Core+Reserve union had 19 distinct coordinates and still captured only **7**. A fixed random K19 has about 36.2% probability of capturing at most one of five winners, so this single result is not statistically shocking, but operationally it demonstrates that E0010's preservation/fusion architecture could not help because four winners were never acquired upstream.

Verdict: **candidate acquisition failure, not assembly failure.**

This is the opposite of 2026-08-21, where the protected reserve held 4/5 winners and assembly/compression was the dominant problem.

## 7. Coordinate mobility

Coordinate7 was strongly predicted, principally as S1. It appeared in the draw as **S2=7**.

Thus:

- anywhere-coordinate credit for7: **hit**;
- exact-slot S1=7: **miss**.

This is another prospective example supporting the distinction between coordinate existence and slot provenance, but one migrated coordinate is not validation of a mobility kernel.

## 8. Multi-expert panel

Frozen expert-preservation slates:

1. VVD/E0010: `7,21,24,36,46`
2. terminal/exact-state: `7,21,31,33,46`
3. density: `7,21,32,35,47`
4. Coulomb/stiction: `16,21,36,38,47`
5. bridge hedge: `7,21,31,36,46`

Actual: `4,7,15,18,29`.

Only coordinate7 survived anywhere in the first, second, third and fifth lines. Coulomb captured no winner. Therefore expert diversification did not solve this target; most experts were sharing the same central-magnitude bias.

This reveals **expert dependency at the regime level**: nominally different experts converged on mid/upper coordinates because they all implicitly assumed ordinary displacement/sum behavior.

## 9. FCPC proper-score audit

The frozen 50-coordinate FCPC vector was slightly worse than flat0.1 on this target:

- composite Bernoulli log-loss delta vs flat: **+0.000526**;
- Brier delta vs flat: **+0.000090**.

Positive is worse.

Derived Top13 recall was 1/5. The full-field result therefore gives no hidden probability-calibration success that would rescue the failed compression.

## 10. PowerBall

Frozen PB ranking:

`12 > 16 > 2 > ...`

Actual PB: **16**.

So:

- exact primary PB12: **miss**;
- second-ranked PB16: **hit**;
- HIGH direction from PB2: **hit**;
- primary VVD10 continuation: **miss**;
- actual VVD14 was a previously observed secondary successor of PB VVD10.

PB2 exact-successor history before the draw was `12,16,2,12`; after the draw it is `12,16,2,12,16`. Thus PB12 is no longer uniquely modal: PB12 and PB16 now have two occurrences each.

Verdict: the PB exact-state family retained the winner in its top2, but the exact primary recurrence was over-confident.

## 11. Root-cause classification

### What worked

- HLR vector `LLLLL|H`: 6/6 directions.
- coordinate7 existed in the prediction field, though wrong slot.
- PB16 was second-ranked and direction HIGH was correct.

### What failed

1. **Magnitude regime:** all main VVDs were much larger than the flagship assumed.
2. **Joint conditioning:** all-LOW was treated too independently instead of re-basing the whole sorted vector jointly.
3. **Morphology/regime coverage:** no explicit deep-sum compression lane.
4. **Candidate acquisition:** 4/5 winners absent from both Core and Reserve.
5. **Expert diversity:** Coulomb, density, terminal-digit and VVD experts shared a hidden centrality bias.
6. **PB point ranking:** PB12 over PB16 was too sharp for a tiny exact-state sample.

## 12. Required architecture changes for next target

### A. HLR-conditioned joint structural baseline

After freezing an HLR vector, enumerate/sample the exact legal combination field satisfying that vector and derive:

- joint slot marginals;
- expected/quantile coordinates;
- conditional sum/spread distribution;
- conditional VVD distributions.

Residual experts should modify this **joint conditional baseline**, not five independent slot baselines.

### B. Magnitude-regime classifier

Before selecting point VVDs, classify at least three exposure regimes:

- **stiction/small:** low displacements;
- **central:** ordinary structural displacement;
- **expansion/compression:** coordinated large displacement.

Freeze weights prospectively. Do not infer the regime from the target after the draw.

### C. Deep-compression chaos lane

When the HLR vector permits a broad directional collapse, reserve a small fixed portfolio allocation to the lower conditional sum tail, e.g. conditional 5–15th percentile. This is exposure insurance, not a claim that low sums are predictive.

### D. Magnitude distribution, not point magnitude

Each lane should retain a calibrated VVD PMF or at least low/central/high magnitude bands. Exact-point motifs such as 10->10 may rank within a band but must not collapse all exposure around one magnitude.

### E. Regime-level expert dependency penalty

Experts that output different numbers but occupy the same sum/magnitude regime should not be counted as independent votes. Diversity must be measured in outcome-space as well as expert-name space.

### F. PB top-k calibration

For tiny exact-state samples, preserve a compact PB top2/top3 and score exact rank, rather than allowing a 2-vs-2 empirical difference to create false precision.

## 13. Evidence verdict

- HLR `LLLLL|H`: **correct but structurally high-base-rate**.
- Tuesday VVD point model: **FAIL**.
- FCPC field: **FAIL/slightly worse than flat on target**.
- E0010 Core/Reserve preservation: **FAIL on acquisition**.
- Coulomb/terminal/density panel: **FAIL on regime coverage**.
- PB exact-state family: **top2 success; exact primary miss**.
- Proposed joint-HLR regime architecture: **new hypothesis, zero retrospective credit**.

No breakthrough is claimed.