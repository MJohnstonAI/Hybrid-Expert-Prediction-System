# HEPS Slot Constraint Funnel & Winner-Float Reconstruction Research

**Date:** 2026-08-05  
**Status:** EXPERIMENTAL — REVIEW REQUESTED  
**Production weight:** ZERO  
**Scope:** Main field only (sorted Slot1–Slot5, 1–50)  
**Purpose:** Reconstruct and rigorously test an older HEPS architecture in which slot-level directional constraints reduce the candidate field before combination assembly, followed by morphology filtering and adaptive winner-float ranking.

---

## 1. Executive finding

The key architectural reconstruction is:

1. **HLR must always forecast one flow direction for each sorted slot:** Low, Repeat, or High.
2. **VVD then estimates plausible movement magnitude conditional on that HLR direction.**
3. Other slot experts score/rank the surviving coordinates.
4. The five slot baskets are cross-combined into legal ascending lines.
5. Combination-level experts (e.g. SLDV, sum/spread, gap morphology, parity/register structure, pair/anchor relationships) score the assembled lines.
6. A post-draw **Physics of Failure** traces exactly where the actual winning line was suppressed.

The old implementation appears to have been brittle because HLR/VVD were often used as veto-like constraints. The reconstructed hypothesis is that HLR and VVD may still contain useful information if retained as **mandatory forecasters but softened as scoring/coverage constraints rather than fatal eliminators**.

Preliminary replay of the three most recent known targets suggests the **candidate-survival funnel can be repaired**, but the principal bottleneck becomes **winner-float ranking**: the exact winning combinations can survive into the generated universe yet remain ranked far below the desired Top-20.

This is not a production result. Independent reproduction is required.

---

## 2. Historical architecture being reconstructed

The reconstructed old-HEPS logic is a slot-first constraint cascade:

```text
Previous sorted slot value
        ↓
HLR forecast: L / R / H
        ↓
VVD movement magnitude
        ↓
Other slot expert scores
        ↓
Ranked slot basket
        ↓
Cross-slot legal assembly
        ↓
Combination morphology / coalition scoring
        ↓
Ranked prediction universe
        ↓
Top-N portfolio
        ↓
Post-draw Physics of Failure
```

This differs from a simple global Top-K number-ranking engine.

---

## 3. Mandatory HLR rule

For every target draw and every sorted slot `j ∈ {1,2,3,4,5}`, HLR must publish exactly one forecast state before candidate generation:

```text
L = next sorted slot value lower than previous
R = next sorted slot value repeats previous
H = next sorted slot value higher than previous
```

Formally, for sorted slot value `x[t,j]`:

```text
HLR[t,j] = L if x[t,j] < x[t-1,j]
           R if x[t,j] = x[t-1,j]
           H if x[t,j] > x[t-1,j]
```

The forecast vector is therefore always a five-state sequence such as:

```text
L — H — L — L — H
```

**Important:** a hedge coordinate outside the forecast direction does not change the HLR call. HLR must remain auditable as a single committed directional forecast per slot.

---

## 4. VVD rule

For each sorted slot:

```text
VVD[t,j] = abs(x[t,j] - x[t-1,j])
```

Primitive HEPS sometimes used sparse transition rules of the form:

```text
previous VVD = 5 → next VVD likely 2 or 5
```

The reconstructed research hypothesis is more conservative:

- VVD is a **movement-magnitude expert**;
- VVD should be evaluated conditional on slot and HLR direction;
- exact sparse VVD-to-VVD lookup tables should not receive veto authority unless strong walk-forward evidence supports them;
- a shrunk movement-band model may be more robust than exact transition lookup.

If HLR predicts Low:

```text
candidate = previous_slot_value - predicted_VVD
```

If HLR predicts High:

```text
candidate = previous_slot_value + predicted_VVD
```

If HLR predicts Repeat:

```text
candidate = previous_slot_value
```

---

## 5. Reconstructed Slot Constraint Funnel (SCF)

The current experimental funnel per slot contains distinct lanes:

### 5.1 HLR core lane
Coordinates consistent with the mandatory HLR direction receive primary exposure.

### 5.2 VVD movement lane
Coordinates whose displacement is compatible with the slot-specific VVD model receive additional support.

### 5.3 HLR escape lane
Because HLR is not perfectly accurate, one or more high-scoring coordinates that violate the HLR forecast may be retained as explicit hedges.

These are labelled **HLR escapes**, not alternative HLR forecasts.

### 5.4 Sorted-slot density hedge
Coordinates in historically dense regions for the relevant order statistic may be retained to protect against overconfident directional constraints.

### 5.5 Void / structural hedge
A small number of independently motivated coordinates may be admitted from non-HLR experts such as void/canyon or other candidate engines.

The purpose of these hedges is not to inflate coverage indefinitely. Their value must be assessed by candidate survival per unit of basket expansion.

---

## 6. Preliminary three-target replay

Targets:

| Target date | Actual sorted main numbers |
|---|---|
| 2026-07-28 | 3, 12, 27, 36, 47 |
| 2026-07-31 | 10, 11, 37, 45, 46 |
| 2026-08-04 | 16, 24, 29, 34, 38 |

### 6.1 HLR directional replay

A first-order slot-specific HLR model was directionally correct on approximately:

```text
28 Jul: 4/5 slots
31 Jul: 3/5 slots
04 Aug: 3/5 slots
Total: 10/15 = 66.7%
```

This is encouraging enough to retain HLR as an expert, but far too weak to justify using the forecast direction as an unconditional hard veto.

### 6.2 Robust funnel survival

A multi-lane SCF variant retained all five actual winning coordinates on all three replay targets.

Approximate legal combination universes after slot-basket cross-combination were:

| Target | Approx. generated legal combinations | Exact winner survived? |
|---|---:|---|
| 2026-07-28 | ~396,145 | Yes |
| 2026-07-31 | ~460,747 | Yes |
| 2026-08-04 | ~366,306 | Yes |

### 6.3 Winner-float ranking bottleneck

Using the preliminary reconstructed HLR/VVD-oriented score, the exact jackpot lines were still ranked poorly:

| Target | Exact winner rank | Approx. top percentile |
|---|---:|---:|
| 2026-07-28 | ~46,848 | 11.8% |
| 2026-07-31 | ~281,625 | 61.1% |
| 2026-08-04 | ~333,645 | 91.1% |

This is the most important current finding:

> The reconstructed funnel can preserve the winner while the ranking layer can still bury it.

Therefore the immediate research bottleneck is not necessarily candidate discovery. It is **relative combination scoring / winner floating**.

---

## 7. Red-team warning: these are not confirmatory results

The three replay outcomes were already known while architecture variants were being explored. Therefore:

- the 3/3 exact-winner survival result is **not** prospective evidence;
- architecture choices may contain post-hoc selection bias;
- all figures must be independently reproduced from code/data;
- no production weight should be assigned on the basis of these three replay targets;
- Friday 2026-08-07 should be treated as a genuine frozen prospective test if this architecture is used.

Classification:

```text
SCF candidate-survival concept: PROVISIONAL / NEEDS REPLICATION
HLR hard veto: REJECT
HLR mandatory directional forecast: KEEP FOR TESTING
VVD exact sparse transition veto: REJECT / DOWNGRADE
VVD soft movement expert: KEEP FOR TESTING
Winner-float ranking layer: PRIMARY OPEN PROBLEM
```

---

## 8. Combination-level scoring candidates to test

Once legal slot combinations are generated, the following experts should be tested as soft scores unless hard-filter value is empirically demonstrated:

### Morphology
- SLDV — Sum of Last-Digit Variance / absolute delta
- macro-sum and macro-sum delta
- span/range
- odd/even composition
- low/high composition
- register/decade occupancy
- gap vector / gap dispersion
- consecutive-number count
- terminal-digit diversity / repetition
- sorted-slot likelihood

### Candidate / coalition
- slot candidate strength
- pair strength
- pair-of-pairs + anchor
- Coulomb / void / shadow support where independently justified
- current experimental candidate engine scores

### Control
- random-from-same-funnel baseline
- morphology-only baseline
- candidate-only baseline

Every expert must be judged on whether it improves the **rank of future winning combinations**, not whether it creates aesthetically normal-looking lines.

---

## 9. Winner-Float objective

For surviving winning combination `W[t]`, record:

```text
rank(W[t])
rank_percentile(W[t])
```

Track survival/rank thresholds:

```text
Top 300K
Top 100K
Top 50K
Top 10K
Top 1K
Top 500
Top 100
Top 20
```

A Top-21 miss and a bottom-decile miss must not be treated as equivalent.

---

## 10. Physics of Failure protocol

After each draw, trace the actual winner through every stage.

### Layer 1 — HLR forecast
For each slot, was the predicted L/R/H direction correct?

### Layer 2 — VVD
Was the actual movement magnitude supported or penalised?

### Layer 3 — slot basket
Did the exact winning coordinate survive the slot funnel? What was its slot rank?

### Layer 4 — exact assembly
If all five coordinates survived, was the exact line generated legally?

### Layer 5 — morphology / coalition scoring
Which combination experts raised or lowered the winning line?

### Layer 6 — final rank
Where did the line rank before portfolio selection?

### Layer 7 — leave-one-expert-out counterfactuals
For each expert `E_j`, compute a counterfactual rank:

```text
rank_without_Ej(W[t])
```

A destructive expert is one that repeatedly pushes future winners downward relative to appropriate controls.

Do not reduce or increase expert weight because of one target alone.

---

## 11. Learning-to-rank interpretation

The winner-float problem should be treated as relative ranking, not score fitting.

Given actual winner `W` and losing survivor `L`, the desired condition is:

```text
Score(W) > Score(L)
```

A transparent regularized pairwise ranking model should be preferred initially over opaque high-capacity models.

Training after draw `t` may use outcomes through `t`, but the updated weights must be frozen before ranking draw `t+1`.

Retrospectively adjusting weights until an already-known winner enters the Top-20 is explicitly prohibited as evidence.

---

## 12. Required independent review questions

Reviewers should attempt to falsify the following claims.

### A. HLR
1. Reproduce slot-specific HLR directional accuracy historically and in the mechanical era.
2. Compare first-order, second-order, unconditional, and simple continuation/reversal models.
3. Test whether HLR adds information beyond sorted-slot marginal distributions.

### B. VVD
1. Reproduce slot-specific VVD autocorrelation / transition structure.
2. Compare exact transition lookup with shrunk movement bands.
3. Test conditional VVD given HLR direction.
4. Determine whether VVD contributes out-of-sample rank lift.

### C. Funnel efficiency
1. Measure exact 5/5 candidate survival against basket size.
2. Compare SCF with a same-size sorted-slot-density control.
3. Compare with random same-size slot baskets where valid.
4. Quantify whether added escape lanes improve winner survival more than they expand combination count.

### D. Winner floating
1. Reproduce the three stated winner ranks.
2. Add combination morphology experts one at a time.
3. Run leave-one-expert-out attribution.
4. Test learning-to-rank only under strict walk-forward.
5. Compare against random-from-same-funnel and morphology-only controls.

### E. Multiple testing
Maintain an experiment registry and correct for the number of architectures / parameterizations inspected.

---

## 13. Prospective integration gate

No part of this reconstruction should enter production HEPS until it satisfies a prospective or properly untouched validation gate.

Minimum evidence should include:

1. all parameters frozen before target reveal;
2. exact denominators retained;
3. comparison with same-size control funnels;
4. reproducible winner-rank improvement, not merely candidate survival;
5. no dependence on post-target tuning;
6. explicit failure cases preserved in the ledger.

The first genuine prospective opportunity after this memo is the South African PowerBall draw scheduled for **Friday, 2026-08-07**.

---

## 14. Relationship to current HEPS repository architecture

This research does **not** replace the active production architecture.

Relevant repository history already documents:

- dynamic expert weighting / consensus scoring;
- sorted-position momentum;
- void / starvation concepts;
- stiction / shadow concepts;
- macro-sum/spread controls;
- self-improvement / post-game recalibration.

This memo proposes a reconstructed middle layer that may have been lost or weakened during HEPS evolution:

```text
mandatory slot-direction forecast
        +
movement constraint
        +
slot baskets
        +
legal combination assembly
        +
combination morphology scoring
        +
winner-float ranking
```

Production files must remain untouched until review and validation are complete.

---

## 15. Requested reviewer verdict

Please classify the reconstruction as one of:

```text
BREAKTHROUGH
PROVISIONAL SIGNAL
INSUFFICIENT EVIDENCE
REJECT
```

and specifically state:

- what is reproducible;
- what is post-hoc;
- which expert(s) deserve further testing;
- which expert(s) should be killed;
- whether the SCF adds information beyond same-size control baskets;
- whether any combination score can materially float future winners without overfitting.

---

## 16. Current lab verdict

**SCF / HLR+VVD reconstruction: PROVISIONAL ARCHITECTURAL LEAD, NOT PREDICTIVE PROOF.**

The most defensible current claim is structural:

> HLR/VVD may be more useful as auditable slot-level constraints and scores than as hard eliminators; preliminary replay suggests the exact winner can survive the funnel, but the ranking layer remains the dominant unresolved failure.

The next research priority is therefore **Winner-Float scoring with strict walk-forward controls**, followed by a genuinely frozen prospective test.
