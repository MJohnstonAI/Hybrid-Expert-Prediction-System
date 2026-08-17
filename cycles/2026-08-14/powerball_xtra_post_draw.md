# PowerBall XTRA — Post-Draw Audit

**Draw:** Friday 2026-08-14  
**Mode:** `paper_trading_only`  
**Result source state:** project-director supplied, pending external verification  
**Actual:** `7, 27, 28, 46, 48 | PB2`

## 1. Frozen HLR versus actual

Previous XTRA state was `15,21,31,42,50 | PB2`.

Frozen main HLR: `L,L,L,?,L` with S4 non-repeat and PB HIGH.

Actual transition:

- S1: 15 -> 7 = **L** hit
- S2: 21 -> 27 = **H** miss
- S3: 31 -> 28 = **L** hit
- S4: 42 -> 46 = **H** accepted by unresolved non-repeat branch
- S5: 50 -> 48 = **L** hit
- PB: 2 -> 2 = **R**; PB-H miss

Raw main HLR score is 4/5, but this is misleading without structural-null correction. Exact null probabilities at the frozen thresholds were approximately:

- S1 L 0.82207
- S2 L 0.67405
- S3 L 0.69003
- S4 non-repeat 0.95975
- S5 L 0.90000

The summed main-slot null-adjusted surplus is about **-0.0459**, essentially no residual advantage. PB-H from PB2 had null coverage 14/16 = 0.875 and missed, scoring -0.875.

## 2. Candidate funnel

Frozen XTRA K13:

`{3,5,10,14,16,20,21,23,29,36,44,46,47}`

Actual winner intersection:

`{46}`

Recall = **1/5**. For an unstructured K13, random expected recall is 1.3/5, so recall surplus is -0.3. This is a catastrophic omission under the expert-league rule (<3/5 winner survival).

Candidate acquisition therefore failed before assembly.

## 3. Coulomb attribution

Frozen Coulomb core/rescue basket:

`{13,14,19,20,29,30,40,41,43,44,48,49}`

Actual intersection:

`{48}`

The important attribution is that **48 was explicitly identified pre-draw as the clearest Coulomb rescue candidate missing from K13**. It then landed exactly as S5=48.

Coulomb corridor scoring:

- S1 13/14 -> actual 7: miss
- S2 19/20 -> actual 27: miss
- S3 29/30 -> actual 28: exact-slot miss, 29 was adjacent
- S4 40/41 or 43/44 -> actual 46: miss
- S5 48/49 -> actual 48: **exact hit**

This is one useful prospective rescue event, not evidence of a durable edge.

## 4. PB expert failure cluster

Actual PB repeated at 2.

All frozen PB lanes missed:

- Human HLR HIGH (>2): miss
- Tier oscillator 11-16: miss
- Arithmetic resolver PB11: miss
- PB2 successor resonance 12/16: miss
- Frequency/recency PB15: miss
- VVD PB9 / band8-9: miss

The failure is correlated: most lanes encoded variants of the same assumption that PB2 should break upward. Future PB ensembles must measure dependency between experts and preserve a repeat/anti-consensus lane.

## 5. Cross-game orthogonal-rescue observation

Director-reported Main result for the same date:

`14,15,19,39,44 | PB3`

The independently frozen XTRA K13 contained Main winners `{14,44}` = 2/5.

The independently frozen XTRA Coulomb basket contained Main winners `{14,19,44}` = **3/5**.

For a fixed random 12-number basket against a five-number Main winning set, P(3 or more hits) is about **8.22%**. This is interesting but not rare enough to infer a cross-game predictive link, especially after considering multiple experts and repeated opportunities.

Therefore this is recorded only as an **orthogonal rescue observation**. Main and XTRA state remain isolated. Future draws may score whether independently generated opposite-game baskets rescue omitted winner coordinates at matched exposure.

## 6. Architecture lessons

1. Candidate acquisition remains the bottleneck.
2. Coulomb rescue deserves continued protected exposure, not increased veto authority.
3. HLR raw-hit counts must remain null-adjusted.
4. PB expert dependency must be tracked; consensus is not independent evidence.
5. Exact-repeat PB states require their own transition expert.
6. Cross-game overlap is a diversification experiment only, not a merged model.
