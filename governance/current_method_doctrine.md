# HEPS Current Method Doctrine

**Effective:** 2026-09-02  
**Status:** binding methodological interpretation layer  
**Scope:** Main and XTRA unless a game-specific protocol explicitly narrows the rule

This file exists to prevent historical experiments, exploratory formulas, and superseded combination rules from being mistaken for current HEPS doctrine. It does not erase prior work. It controls how prior work may be interpreted and reused.

## 1. Joint-distribution-first doctrine

HEPS now uses the stronger principle:

> **Joint distribution first, compression second.**

For Main, the legal next-draw state space is the `C(50,5)=2,118,760` sorted five-number lines. Learned information should enter through low-dimensional, regularized residual potentials, but the final probability model should be normalized over the legal state space whenever computationally feasible.

Do not estimate 2.1 million free combination probabilities from the current small sample. Factorize the *information representation*, not the evidence claim. Exact legal-state normalization remains feasible.

## 2. Functional-coupling rule: one transition, one information family

For sorted slot `j` with previous coordinate `p_j` and next coordinate `x_j`, define signed displacement:

`DELTA_j = x_j - p_j`.

The following are deterministic views of the same transition:

- `MAIN_HLR_SLOT = sign(DELTA_j)`;
- `MAIN_VVD_DELTA = abs(DELTA_j)`;
- target coordinate `x_j = p_j + DELTA_j`;
- terminal digit `x_j mod 10`.

Therefore HLR, VVD, exact slot coordinate, and terminal digit derived from the same transition **must not be multiplied or counted as independent expert evidence**.

They may be:

- reported separately for interpretability;
- scored separately against their exact structural nulls;
- used as basis functions inside one jointly fitted transition model;
- used as diagnostics or routing summaries.

They may not receive independent convergence votes merely because their names or feature spaces differ.

## 3. Preferred Main transition representation

The preferred successor to multiplicative HLR/VVD chains is a single regularized signed-displacement model.

For slot `j`, let:

- `P0_j(x)` = exact order-statistic slot null at coordinate `x`;
- `q_j(x | p_j, history)` = learned/shrunk slot transition distribution;
- `T_j(x) = q_j(x | p_j, history) / P0_j(x)` = **residual ratio** on legal support.

`q_j` may be parameterized as:

`q_j(x) proportional to P0_j(x) * exp(phi_j(x-p_j))`

or an equivalent low-dimensional shrinkage form.

`phi_j` must be estimated only from prior data and heavily regularized. Free per-displacement parameters are discouraged at the current sample size unless justified by a preregistered shrinkage hierarchy.

### Correct legal-line construction

The exact IID Main line null is uniform over legal lines:

`P0_line(x_1,...,x_5) = 1 / C(50,5)` for `x_1<...<x_5`.

The learned joint line field should therefore tilt the **uniform legal-line null by residual ratios**, not multiply the five slot null probabilities again:

`Q(x) = P0_line(x) * product_j T_j(x_j)`

for legal sorted `x`, followed by:

`P(x) = Q(x) / sum_legal_y Q(y)`.

Since `P0_line` is constant on legal lines, ranking weights are proportional to `product_j T_j(x_j)`, but the baseline interpretation remains the exact uniform legal-line null.

This construction has an essential sanity property:

> if every learned slot field equals its exact structural slot null, then every `T_j=1` and the joint model reduces exactly to the uniform legal 5/50 line null.

Do **not** use `product_j q_j(x_j)` as the legal-line field: that would multiply order-statistic geometry across dependent slots and fail to return to the exact uniform line null when no learned residual signal exists.

Pairwise residual potentials may be added only when they represent information not already encoded by the transition field, are defined relative to an appropriate exact/simple null, and survive redundancy/proper-score tests.

## 4. Proper-score-first promotion gate

Candidate-basket recall is secondary to probability calibration.

A learned acquisition model may not claim predictive lift merely because its optimized K13/K20 captures more winners in replay. Before promotion, the underlying full-support probability field must show prospective improvement versus the exact structural/simple baselines on a proper score such as log loss or Brier score.

Required interpretation:

- better K13 recall + worse proper score = possible optimization over misspecification, not established edge;
- better proper score + no K13 lift = potentially useful probability model with a compression problem;
- better proper score + better matched-K recall = strongest acquisition evidence.

## 5. Global coordinate preservation versus exact-slot provenance

HEPS must distinguish:

- `P(number appears anywhere)`;
- `P(number occupies exact sorted slot)`.

A coordinate may contain useful acquisition information even if its strongest pre-draw score occurs in an adjacent sorted slot. The 2026-09-01 Main draw provided a clear prospective example:

- coordinate 14 was highly ranked pre-draw in S2 but realized in S1;
- coordinate 16 ranked strongly across S1/S2 and realized in S2.

Future candidate-funnel experiments may test bounded adjacent-slot preservation at **fixed K**. No union/K expansion receives predictive credit.

## 6. 2026-09-01 Main lesson

Verified result: `14,16,31,34,40 | PB4` from previous `19,22,24,25,47 | PB11`.

Realized HLR: `LLHHL`.

The frozen BARP modal HLR scenario was also `LLHHL`, an exact 5/5 direction hit. This receives positive prospective credit but no one-draw promotion.

Candidate acquisition remained the first major failure stage:

- E0019 K13 retained only 31 and 34;
- K20 additionally retained 40;
- 14 and 16 were present in useful slot-level/adjacent-slot evidence but were not preserved by final compression.

The operational lesson is to reward correct direction by **preservation/scenario allocation**, not by multiplying HLR with VVD or terminal ratios.

## 7. Terminal motifs

Terminal-digit research remains diagnostic.

E0020 showed:

- nominal repeated same-slot L3 excess did not survive multiplicity correction;
- suffix/Markov terminal models did not beat the exact terminal null overall;
- terminal+HLR+VVD multiplication worsened proper scores monotonically;
- on 2026-09-01, S3 terminal 1 and S4 terminal 4 were top-1 hits, while other realized residues were present in secondary fields.

Therefore terminal motifs may justify bounded preservation when they agree with stronger independent evidence, but they have no standalone candidate authority and may not be multiplied into HLR/VVD as separate likelihood ratios.

## 8. Coalition doctrine

E0013 Positive-PMI spectral remains a coalition-only shadow with `PROVISIONAL_SIGNAL` discovery evidence.

Do not apply a supposed "central-coordinate structural co-occurrence correction" by subtracting `P0(i,j)` from every unordered coordinate pair. Under uniform 5-of-50, every distinct unordered coordinate pair has the same anywhere-co-inclusion null probability:

`P0(i,j)=C(48,3)/C(50,5)=20/(50*49)`.

A useful E0013 challenger should instead control for observed coordinate marginals/frequency, for example via a shrunk or conditional null for `C_ij` given `C_i` and `C_j`.

## 9. Redundancy doctrine

An expert is an information source that adds residual predictive information, not merely a different mathematical projection of an existing source.

Before multiple experts increase confidence:

1. residualize/control exact structural geometry;
2. control simple frequency/recency where relevant;
3. measure residual dependence;
4. require incremental proper-score or stage-isolated value.

Highly correlated or functionally derived views count as one information family.

## 10. Richardson / message-passing interpretation

The E0016 Richardson pair-separation estimator and pair compatibility ratio are mathematically valid shadow components. Its historical geometric-mean message-passing update is a heuristic approximation, not exact belief propagation over a five-node chain, because the protocol uses all ten slot pairs.

Where feasible, future joint models should score legal lines directly using pair potentials and normalize over the complete legal state space rather than treating the heuristic message-passing marginals as a coherent exact joint posterior.

## 11. PowerBall doctrine

The 1..16 PowerBall field remains separate.

Conditional transition models are sparse at the current sample size and require strong shrinkage. Conditional authority must be earned prospectively against uniform and a preregistered unconditional shrunk baseline on proper score.

HLR, VVD, terminal digit, and exact-state successor views of the same PB transition may not be multiplied as independent evidence without a dependency model.

## 12. Machine/mechanical research

If a durable mechanical-era edge exists, machine/ball-set non-exchangeability or regime-specific bias is a higher-value hypothesis than inventing additional transforms of the previous winning numbers.

However:

- machine identity must be known or provenance-qualified;
- no guessed machine state;
- no post-hoc split-point search presented as confirmation;
- heavy hierarchical shrinkage is mandatory at current sample sizes;
- physical claims require evidence beyond sorted-number statistics.

## 13. Historical experiment precedence

When an older experiment conflicts with this file, follow:

1. immutable frozen pre-draw artifact for historical scoring;
2. latest post-draw decision/failure record for evidence interpretation;
3. `governance/methodology_deprecations.md` for reuse authority;
4. this current-method doctrine for new work.

Historical formulas remain evidence of what was tested. They are not automatically valid templates for future models.

## 14. Breakthrough criterion

HEPS should reserve predictive `BREAKTHROUGH` claims for evidence that survives prospective, matched-exposure, multiplicity-aware testing. A compelling near-term milestone is:

- full-support field improves proper score versus structural/simple baselines;
- fixed-K candidate recall improves versus matched controls;
- improvement survives multiple targets and independent reproduction;
- any coalition/portfolio gain is stage-isolated from acquisition gain.

A single successful draw, motif, or line is never sufficient.