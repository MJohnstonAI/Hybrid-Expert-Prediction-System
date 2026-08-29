# E0017 Red Team — Gemini Claim Falsification Protocol

## Objective

Determine whether Gemini's reported 2026-08-28 XTRA success reflects:

1. a genuinely pre-draw frozen predictive result;
2. a useful but poorly documented algorithm that HEPS failed to reproduce;
3. target leakage / post-draw reconstruction;
4. a broad-exposure result with no material edge over matched random controls.

This protocol does not assume deception. It is designed so that provenance, reproducibility and future predictive value are tested separately.

## Test A — Forensic provenance of the 2026-08-28 claim

Gemini must provide the original pre-draw artifacts, not a post-draw narrative:

- exact prompt used before the draw;
- exact model response containing Primary, Secondary and Tertiary main tiers;
- exact 11 PowerBall attractors;
- complete ordered board list including alleged Board 19;
- creation timestamp / conversation timestamp / immutable file metadata;
- model/version used;
- exact historical dataset or ledger snapshot supplied to the model;
- evidence that the 2026-08-28 result was absent from the input and unavailable to any preprocessing step;
- if code was used, the exact code/notebook and random seed.

### Provenance verdict

- If a timestamped artifact created before the draw contains the claimed tiers and exact Board 19, preserve the result as genuine prospective evidence even if the later explanation is defective.
- If only post-draw summaries exist, award zero prospective credit.
- If the pre-draw prompt contains the target winners as examples/hints, classify the affected result as target contaminated.

## Test B — Exact algorithm specification challenge

Before any further evaluation Gemini must resolve every ambiguity in writing and executable code.

### Spectral stage

Specify exactly:

- whether A_ij is binary or weighted by co-occurrence count;
- whether the diagonal is zero;
- treatment of disconnected/zero-degree nodes;
- normalized Laplacian convention;
- eigenvalue sorting and tolerance for zero eigenvalues;
- whether k={2,3,4} means matrix indices or the three smallest strictly positive eigenpairs;
- eigenvector normalization/sign handling;
- exact Score_spectral formula;
- deterministic tie-break rule.

### Gap residual stage

Specify exactly:

- definition of current gap g_i;
- definition of historical gap intervals;
- minimum appearances required;
- behavior when a number has 0 or 1 prior appearance;
- behavior when sigma_i=0;
- whether mean/SD are population or sample estimates;
- any Bayesian/shrinkage prior;
- deterministic ranking/tie break after R_i >= 1.20.

This is mandatory because number 38 had only one prior post-June XTRA appearance before 2026-08-28 under the HEPS ledger, so a conventional recurrence mean and SD are not defined.

### Entropy/filler stage

Specify exactly:

- objective function for decade entropy;
- candidate set eligible for tertiary inclusion;
- whether tiers must be disjoint;
- exact greedy/optimization algorithm;
- whether 1 and 50 are mandatory or merely candidates;
- deterministic tie breaks.

### PowerBall stage

Specify exactly:

- orientation of P_jk;
- smoothing/pseudocounts;
- treatment of unseen transitions;
- exact modular recurrence-gap formula;
- normalization of its score;
- exact blend weight between Markov and recurrence components;
- deterministic tie break.

This is mandatory because prior observed successors from PB16 were 16 and 10; PB15 cannot be reproduced from first-order transition counts alone.

### Assembly stage

Specify exactly:

- the Maximum-Entropy Convergence Vector formula;
- number of boards generated;
- board-generation candidate universe;
- all constraints/morphology rules;
- board ranking formula;
- deterministic tie breaks/random seed.

No phrase such as 'targeting 03,04,16,35', 'capturing 38', or 'prioritizing 15' may appear in the frozen specification.

## Test C — Independent clean-room reproduction

HEPS implements Gemini's final frozen specification independently without copying Gemini's generated candidate lists.

Input boundary:

- XTRA only;
- 2026-06-02 onward;
- target excluded;
- no Main state;
- no pre-June Plus/XTRA.

Reproduce the 2026-08-28 cutoff using only data through 2026-08-25.

The implementation passes only if it reproduces Gemini's claimed pre-draw output exactly, or within explicitly predeclared numerical/tie tolerances.

Failure to reproduce means the 2026-08-28 mechanism claim remains unsupported even if a genuine pre-draw board artifact exists.

## Test D — Historical expanding-window replay

Once the formula is frozen, run target-blind walk-forward replay over every eligible post-June XTRA target.

Do not retune parameters between targets.

Score separately:

### Primary K12

- total winner-coordinate capture;
- mean winner rank;
- 3+/5, 4+/5 and 5/5 rates;
- matched random K12 controls;
- simple frequency K12;
- simple recency K12;
- incumbent HEPS K12/K13-equivalent comparator where available.

The primary-tier 4/5 result is the scientifically interesting claim because random K12 has a low probability of 4+/5 on one draw.

### Primary + Secondary

Use the actual unique union size. If tiers overlap, do not call it K26 without checking unique exposure.

Report matched-random same-K controls.

### Full K36

- 5/5 rate;
- mean recall;
- matched random K36.

A K36 5/5 event must not be presented without its large random baseline.

### PowerBall K11

- actual PB rank;
- Top1/Top3/Top11;
- log loss if a complete 1..16 probability field is available;
- matched random K11 and uniform controls.

### Assembly

Condition on the identical candidate universe and identical number of generated boards.

Report:

- best-line match count;
- exact-line rank;
- number of 3+/4+/5 boards;
- matched random assembly using the same K and board count.

No assembly credit is awarded for candidate numbers absent upstream.

## Test E — Prospective sealed challenge

This is the decisive test.

For each of the next untouched XTRA draws:

1. update only through the immediately previous verified XTRA draw;
2. run Gemini's frozen executable algorithm with no LLM judgment inside the numerical loop;
3. save the complete output to `cycles/YYYY-MM-DD/pre_draw/`;
4. commit it to GitHub before the draw;
5. record the commit SHA and UTC timestamp;
6. do not modify the artifact;
7. reveal the result and score it afterward.

Freeze at minimum:

- ordered spectral ranking 1..50;
- Primary K12;
- ordered gap-residual ranking and Secondary tier;
- Tertiary tier;
- unique K36 union;
- full PB 1..16 ranking plus K11;
- complete board list and board ranking;
- code commit SHA;
- ledger cutoff/hash;
- parameter hash/random seed.

Initial review: 10 prospective targets.
Stronger review: 20+ prospective targets.
One successful draw cannot promote the method.

## Test F — Adversarial controls

Try to destroy the result with:

- weighted versus binary graph ablation, preregistered before scoring;
- eigenvector/eigenvalue sensitivity audit;
- leave-one-draw-out graph stability;
- recency/frequency residualization of spectral scores;
- gap-score shrinkage sensitivity only as separately frozen derivatives;
- draw-order permutation;
- random graph edge-weight permutation preserving node degrees where feasible;
- random same-K candidate baskets;
- morphology-matched random board assembly;
- leave-one-stage-out pipeline ablation;
- multiple-testing accounting for every formulation inspected.

## Evidence decisions

### BREAKTHROUGH

Only after a preregistered prospective test materially beats matched controls after multiplicity correction and independent reproduction.

### PROVISIONAL_SIGNAL

Repeated prospective lift at fixed exposure, not dominated by one draw, with credible reproducibility but insufficient confirmatory power.

### INSUFFICIENT_EVIDENCE

Interesting output or authentic pre-draw success without stable matched-control lift.

### REJECT

The frozen formulation fails independent reproduction or prospective matched-control testing sufficiently to falsify its predictive claim.

## Interpretation rule

A genuine pre-draw exact Board 19 and a defective explanatory prompt can both be true. Conversely, a mathematically elegant post-draw reconstruction is not predictive evidence. Provenance and algorithmic validity must therefore be scored separately.
