# E0001 — Findings

**Evidence classification:** `INSUFFICIENT_EVIDENCE`  
**Architecture status:** `experimental`

## 1. Source separation

This package combines three contributions but keeps their roles distinct:

- **Claude Sonnet red-team:** identified the exact order-statistic HLR/VVD null as the required comparator and recommended prospective proper-score testing.
- **Gemini:** proposed slot-gap Dirichlet modelling as a cleaner state representation.
- **ChatGPT reproduction/synthesis:** corrected the gap definition, verified Claude's per-slot null calculations, enumerated the full 2,118,760-combination joint HLR null, and integrated the findings into a falsifiable experiment.

The source reviews remain preserved separately. This findings document is the HEPS synthesis, not a replacement for those sources.

## 2. Claude's corrected red-team conclusion is accepted

The previous repository-provenance objection was resolved: Claude's first review inspected the `main`-branch state. The corrected re-review accepted the 19-row research-branch snapshot and concluded that HLR/VVD have `INSUFFICIENT_EVIDENCE` beyond exact order-statistic geometry.

That scientific conclusion is retained.

## 3. Friday HLR is a strong anti-null hypothesis

For previous draw `16,24,29,34,38`, exact slot geometry strongly prefers:

- Slot1 LOW: `0.846782`;
- Slot2 LOW: `0.771385`;
- Slot3 LOW: `0.616156`;
- Slot4 HIGH: `0.518458`;
- Slot5 HIGH: `0.763096`.

The frozen learned model instead committed `HLHHL`, with especially large positive probability deviations from the null on the chosen HIGH/LOW state at Slots 1, 3, and 5.

This is not evidence of predictive skill. It makes the 2026-08-07 target a useful prospective stress test because the learned model is explicitly overriding a strong free structural baseline.

## 4. Full joint-null enumeration weakens the prior 3/8/8 narrative

The exact 243-vector null was computed by enumerating all `C(50,5)=2,118,760` legal next draws for each fixed previous state.

For the Friday previous state, the top structural vectors include:

`LLLLH, LLLLL, LLLHH, LLHHH, LHHHH, HHHHH`.

Several Candidate Lattice rescue vectors are therefore already high-probability under IID geometry.

The Friday committed vector `HLHHL` has only `336` legal next draws, probability `0.01585833%`, structural-null rank `109/243`.

Retrospective comparison:

| Target | Actual vector | Candidate Lattice rank | Exact null rank | Interpretation |
|---|---|---:|---:|---|
| 2026-07-28 | LHHHH | 3 | 2 | null explains it at least as well |
| 2026-07-31 | HLHHL | 8 | 26 | interesting residual case, post-hoc only |
| 2026-08-04 | HHLLL | 8 | 3 | null explains it better |

Thus two of the three previously encouraging flow ranks are largely geometric. The 2026-07-31 case is worth retaining as a hypothesis seed but provides no confirmatory evidence.

## 5. Candidate compression remains unresolved

The frozen Candidate Lattice union contains 38 main numbers.

For any fixed 38-number basket under exchangeability:

- `P0(5/5 survival) = 0.23690366`;
- `P0(4+/5 survival) = 0.65496894`.

Therefore one 5/5 or 4+/5 basket success at K=38 would not establish useful candidate discovery.

The 12 excluded Friday numbers are:

`1,2,14,15,16,24,28,29,32,39,41,42`.

The excluded set contains `16,24,29`, three members of the immediately previous draw. Under IID sampling, the probability that at least one of those three specific coordinates appears in the next main draw is `0.27602041`. Track this as explicit exclusion risk rather than assuming repeats are unlikely.

## 6. Gemini's gap-space proposal is mathematically useful after correction

Gemini's original internal gaps omitted the `-1` adjustment needed to count only unselected numbers.

Correct representation:

`G = (S1-1, S2-S1-1, S3-S2-1, S4-S3-1, S5-S4-1, 50-S5)`.

The components are nonnegative and sum to 45.

For `16,24,29,34,38`:

`G = (15,7,4,4,3,12)`.

The exact IID gap null is not an ordinary multinomial. It is equivalent to:

`DirichletMultinomial(N=45, alpha=[1,1,1,1,1,1])`,

which is exactly uniform across all weak six-part compositions of 45 and therefore across all legal sorted 5/50 lines.

This reparameterization is a valid architectural coordinate system. It is not evidence of predictive temporal structure.

## 7. Gap-space clarifies why HLR vectors are correlated

For corrected gaps:

`S_j = j + sum_{i=1..j} G_i`.

Therefore:

`Delta S_j = sum_{i=1..j} Delta G_i`.

And because every draw satisfies `sum(G_i)=45`:

`sum(Delta G_i)=0`.

The five HLR states are therefore signs of cumulative movements in a constrained six-component composition rather than five independent primitive states. This provides a structural explanation for why multiplying independent HLR marginals is wrong and why a 243-vector ranker can rediscover geometry.

## 8. Gap-residual predictive value is unproven

Under IID independence, every gap has mean `7.5` next draw regardless of the current draw.

The expected change from current gap `G_i,t` is `7.5-G_i,t`.

A residual written as:

`Delta G_i - (7.5-G_i,t)`

simplifies to `G_i,t+1-7.5`.

This is useful conceptually because it separates structural mean reversion from a fitted temporal story, but it does not itself create a predictive feature. A gap model must forecast future deviation from the exact null using only prior information and must beat `NULL_GAP_DM` prospectively.

## 9. Do not fit a six-parameter Dirichlet model now

With only ~19 active draws, estimating six separate `alpha_i` values would create excessive degrees of freedom.

The first allowed descriptive alternative is a symmetric one-parameter concentration model:

`alpha_i = c` for all six gaps, with null `c=1`.

Even this remains descriptive until it has a frozen prospective scoring protocol.

A boundary-vs-interior two-parameter model may be considered later only after evidence and sample size justify it.

## 10. Candidate-engineering ideas from Gemini

### Skip-state partitioning

Retain only as a weak experimental feature. Do not hard-code candidate quotas. Active-era never-observed coordinates are censored at the regime boundary.

### Spatial decile bounding

Hard per-decile caps are rejected as candidate pruning because they can destroy 5/5 recall by construction. Decile occupancy can remain a diagnostic/diversity metric.

### Multi-model consensus

The ensemble principle is acceptable but feature stages must remain separated. Recency can be coordinate-level; co-occurrence is coalition-level; last-digit and consecutive-pair structure belong to morphology/assembly.

### Meta-basket cascading

The combinatorics are correct but do not constitute predictive evidence. A larger meta-basket increases random 5/5 capture simply by retaining more exposure. If revisited, test a dynamic K frontier and scenario-conditioned sub-baskets against exact same-exposure controls rather than treating 13 as a privileged size.

## 11. Strongest supporting evidence

- Claude independently reproduced the 19-row frequency/recency near-null result.
- Claude's exact per-slot HLR null calculations were independently verified.
- Exhaustive enumeration confirms that two of the three previously encouraging actual flow-vector ranks were already top structural-null outcomes.
- Gap-space has a clean exact one-to-one combinatorial representation.

## 12. Strongest counterargument

The active-era sample is extremely small. Failure to demonstrate incremental information at n≈19 does not prove no such information exists. The 2026-07-31 flow case is one example where the learned ranker materially outranked the exact null.

## 13. Likely failure mode

Post-hoc expansion of HLR/VVD/gap models can always discover apparently attractive patterns in a tiny sample. Without frozen probability outputs and proper scoring versus exact nulls, added complexity will likely manufacture rather than discover signal.

## 14. Replication requirement

Required.

Future AI models should independently reproduce:

1. exact per-slot order-statistic nulls;
2. exact joint 243-vector counts;
3. corrected gap composition and Dirichlet-Multinomial equivalence;
4. prospective HLR/VVD proper-score comparisons.

## 15. Recommended next action

Do not add another candidate-selection expert yet.

Run the prospective championship defined in `protocol.yaml`:

`NULL_HLR_STRUCTURAL vs MAIN_HLR_SLOT`,

then:

`NULL_VVD_STRUCTURAL vs MAIN_VVD_DELTA`,

while logging `NULL_HLR_JOINT_243` and gap-space diagnostics.

Only after a learned state model demonstrates incremental predictive information should HEPS increase Candidate Lattice compression authority.

## 16. Current decision recommendation

`INSUFFICIENT_EVIDENCE` — keep exact structural nulls as required methodological baselines; keep learned HLR/VVD/gap models experimental and diagnostic until prospective scoring justifies more authority.
