# PowerBall XTRA — Post-Draw Physics-of-Failure Audit

**Draw:** Tuesday 2026-08-18  
**Mode:** `paper_trading_only`  
**Result source state:** project-director supplied; pending external verification  
**Actual:** `7,11,18,26,31 | PB12`

## 1. State transition

Previous XTRA state (2026-08-14):

`7,27,28,46,48 | PB2`

Actual HLR transition:

`R,L,L,L,L | PB H`

Actual VVD vector:

`S1=0 | S2=16 | S3=10 | S4=20 | S5=17 | PB=10`

The draw therefore produced a broad downward compression of S2-S5, with S1 repeating exactly at7 and PB rising by10.

## 2. HLR expert audit

### Learned HLR/BARP challenger

Frozen: `H,L,L,L,H`

Actual main: `R,L,L,L,L`

Raw score: 3/5 (S2,S3,S4).

Using the exact sorted-order structural directional probabilities at the 2026-08-14 state, the summed event surplus of the five frozen directional calls is approximately **-0.00184**, effectively neutral. The raw 3/5 therefore does not demonstrate residual directional information beyond structural geometry.

### Director HLR flow

Frozen: `H,L,H,H,H,H`

Actual: `R,L,L,L,L,H`

Main raw score: 1/5 (S2 only); PB direction hit.

Combined null-adjusted surplus is approximately **-0.7995**. The aggressive upper-tail S3-S5 branch failed.

The prior debate over S1=10 versus13 never reached the VVD-magnitude stage: the H premise itself failed because S1 repeated at7.

### Exact structural modal control

Frozen modal main direction: `L,L,L,L,L`.

Actual: `R,L,L,L,L`.

Raw score: 4/5. Its summed event-surplus score is approximately **+0.4329**. The exact actual main directional configuration `R,L,L,L,L` occupies about **3.00%** of legal 5/50 combinations at the prior coordinate thresholds, so it is uncommon but not anomalous.

## 3. Candidate acquisition

### Incumbent K13

Frozen:

`{5,8,10,16,20,21,26,27,32,44,46,47,50}`

Actual intersection:

`{26}`

Recall = **1/5**, versus unstructured K13 expectation 1.3/5. This is another catastrophic acquisition miss under the HEPS league definition (<3/5).

### Cross-lane VVD FCPC derived Top13

Frozen:

`{1,3,4,17,19,22,25,31,39,43,46,48,50}`

Actual intersection:

`{31}`

Recall = **1/5**. Again, hard compression looks poor.

However, the full 50-coordinate FCPC vector scores slightly **better than flat** on this first prospective target:

- Bernoulli mean log loss: 0.322772 vs flat 0.325083; delta **-0.002311**;
- Brier: 0.089546 vs flat 0.090000; delta **-0.000454**.

Negative deltas are better. One target has no inferential weight, but this is exactly why Gate1 proper-score information detection must be kept separate from Gate2 K13 compression.

## 4. Coulomb / shadow

Frozen Coulomb density line:

`8,26,27,44,50`

Actual intersection:

`{26}`

Raw line recall = 1/5 versus random K5 expectation 0.5/5, giving +0.5 raw recall surplus for this single target. This is insufficient evidence and does not rescue the broader candidate-acquisition failure.

## 5. Cross-lane VVD motif audit

Frozen primary magnitudes:

`3,8,3,7,2,10`

Actual magnitudes:

`0,16,10,20,17,10`

Only the **PB primary VVD10** hit exactly: 1/6 primary lane hits.

S3 did not hit its primary VVD3, but its pre-frozen **algebraic hedge VVD10** hit exactly. Thus the pre-frozen matrix-wide candidate VVD10 occurred in two lanes:

- S3: `28 -> 18`, VVD10;
- PB: `2 -> 12`, VVD10.

For a pre-specified VVD10 applied across all six lanes at the prior state, exact structural 5/50 order-statistic geometry plus independent uniform PB gives approximately **2.52%** probability of at least two lane hits. This is before adjustment for the many other prospectively frozen motif candidates and model families, so it is an interesting first prospective event, not a discovery claim.

## 6. PowerBall attribution

The incumbent PB hierarchy ranked PB10 first and PB12 only as a later hedge, so the incumbent exact-primary PB forecast missed.

The separately frozen XTRA cross-lane VVD motif challenger made:

`PB current2 + primary VVD10 + HIGH = PB12`

Actual PB was **12**.

This earns clean prospective exact-ball credit for the cross-lane motif challenger. It must not be transferred retrospectively to the incumbent PB10 expert.

The older repeat-break set `{10,13,15}` and zero-VVD same-PB set `{8,10,16}` both missed. Therefore the PB12 success came from the **cross-lane 0->10 / matrix-wide VVD10 route**, not from the same-lane repeat-state experts.

## 7. Coordinate mobility

The Director-HLR motif line was:

`10,19,31,47,50 | PB12`

It contains main coordinate31 and PB12. Actual main31 occurred at **S5**, whereas the rationale generated31 as an S3 coordinate (`28 + VVD3`). Therefore:

- portfolio coordinate credit for31: yes;
- exact-slot S3 credit: no;
- PB12 exact credit: yes.

This is a concrete example of HEPS coordinate mobility: a coordinate can survive globally while the slot assignment is wrong.

## 8. Architecture verdict

1. Main candidate acquisition failed again; incumbent K13 and VVD-FCPC Top13 both retained only 1/5.
2. Structural HLR control outperformed both learned and Director HLR on this target.
3. The learned HLR raw 3/5 reduces to essentially zero residual surplus after structural adjustment.
4. Cross-lane VVD primaries failed on 5/6 lanes, so the family did not succeed broadly.
5. **PB12 is a valid prospective success** for the cross-lane VVD10 challenger.
6. **Matrix-wide VVD10 landing in S3 and PB is the strongest experimental observation from this draw**, but requires multiplicity control and future replication.
7. The first prospective FCPC full-field score is slightly better than flat despite a poor Top13, supporting the architecture distinction between information detection and compression.
8. Coordinate mobility remains a live research problem:31 was globally useful but assigned to the wrong slot.
9. No breakthrough is declared.

## 9. New current state

For the next XTRA target, the state is now:

- coordinates: `7,11,18,26,31 | PB12`;
- latest HLR: `R,L,L,L,L | H`;
- latest VVD: `0,16,10,20,17 | 10`.

Any next-cycle motif discovery must use this new XTRA-only state prospectively and must not repair the 2026-08-18 rules after seeing the outcome.
