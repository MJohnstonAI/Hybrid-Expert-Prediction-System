# HEPS External Contribution Decomposition Protocol

## Purpose

Outside AI models, human researchers, papers, code agents, and other contributors may identify useful mathematics while assigning it the wrong interpretation, data scope, terminology, architectural stage, or authority.

HEPS therefore does **not** treat an outside contribution as an all-or-nothing architecture proposal. The required default is to decompose it into testable information operators, place each operator at the HEPS stage where it could plausibly add information, and test it against the correct controls.

The objective is to avoid two symmetric errors:

1. adopting an attractive but unsupported external architecture wholesale; and
2. discarding a potentially valuable algorithm merely because the contributor used bad data, weak terminology, an incorrect mechanism story, or the wrong pipeline stage.

This protocol does not weaken HEPS evidence standards. It changes how external ideas enter the research pipeline.

---

## 1. Contribution intake: separate source claims from mathematical content

For every outside contribution, preserve the original artifact and extract separately:

- claimed mechanism or narrative;
- mathematical transformations/operators;
- input variables and data requirements;
- hyperparameters and thresholds;
- proposed output;
- proposed HEPS stage or authority;
- claimed performance metrics;
- source dataset/provenance;
- implementation/code, if supplied.

Do not assume that the contributor's narrative, terminology, stage assignment, or claimed performance is correct merely because an underlying mathematical operator is interesting.

Conversely, a provenance or terminology failure does not by itself reject every mathematical operator contained in the contribution.

## 2. Semantic tolerance, mathematical precision

HEPS is not concerned with superficial vocabulary differences between agents when the mathematics is equivalent.

When two contributors use different names for the same mathematical object:

- map both to the binding HEPS identifier where one exists;
- preserve the contributor's original wording in the source record;
- evaluate the mathematics rather than penalizing harmless wording differences.

When the same name is used for materially different mathematics, binding HEPS nomenclature still controls the repository implementation.

The important distinction is **semantic equivalence versus mathematical non-equivalence**, not stylistic consistency.

## 3. Algorithm extraction

Decompose the contribution into the smallest meaningful testable operators. Examples:

- coordinate score;
- pair/graph affinity;
- transition matrix;
- dimensionality reduction;
- regime classifier;
- displacement distribution;
- morphology score;
- pruning rule;
- portfolio objective;
- uncertainty controller;
- state-dependent weight update.

Do not require the complete external architecture to succeed before testing a component that can be isolated.

Where code and prose specify different algorithms, treat them as separate variants until reconciled.

Where essential parameters are missing, do not silently invent one privileged implementation. Either:

- request the missing specification; or
- define a small explicit challenger family, record every variant tested, and treat the exercise as exploratory with full multiple-testing exposure.

## 4. Stage-remapping requirement

For each extracted operator, ask where its information naturally belongs in the canonical staged architecture:

1. Slot Forecast;
2. Candidate Funnel;
3. Coalition Assembly;
4. Morphology;
5. Winner-Float Ranking;
6. Portfolio Optimization;
7. PowerBall Matrix;
8. methodology/control only.

An operator must not be rejected solely because it fails in the contributor's proposed stage.

When mathematically plausible, test at least one alternative stage before declaring the underlying operator unhelpful.

Example principle:

> A pair/co-occurrence graph may fail to identify which coordinates will appear, yet still contain information about which already-acquired coordinates belong together. In that case it belongs in Coalition Assembly rather than Candidate Funnel.

This is the **right-mathematics / wrong-role** safeguard.

## 5. Canonical-data reconstruction

External performance claims receive no HEPS evidence credit until reconstructed or independently reproduced against the canonical ledger and declared data boundaries.

If an external artifact used:

- unknown data;
- legacy data;
- synthetic data;
- mixed Main/XTRA data;
- target-contaminated data;
- an unapproved mechanism boundary;

then its claimed performance is provenance-qualified or rejected as evidence. The underlying algorithm may still enter a fresh HEPS experiment using valid data.

Main and XTRA remain separate. Cross-game contributions may transfer methodology, but coordinates, fitted constants, motifs, and state parameters require explicit cross-game validation.

## 6. Algorithm-extraction championship

When an external contribution contains several ideas, HEPS should run an **algorithm-extraction championship** where feasible.

For each operator or small variant family:

1. identify the HEPS stage being tested;
2. define a stage-appropriate output;
3. select the exact structural/null, simple, and incumbent baselines;
4. use canonical no-leakage walk-forward data;
5. preserve matched exposure;
6. measure the stage-specific metric;
7. record all variants searched;
8. perform adversarial controls designed to destroy superficial explanations;
9. classify the operator independently of the contributor's complete proposal.

Examples of adversarial controls include:

- frequency/recency residualization;
- morphology-matched controls;
- draw-order permutation;
- random candidate universes of identical size;
- oracle candidate-universe isolation for testing assembly independently of acquisition;
- leave-one-feature/expert-out analysis;
- exact structural-null comparison.

A component that survives such diagnostics may become a separate HEPS experiment even when the original external architecture is rejected.

## 7. Stage-isolation tests

Whenever possible, isolate upstream and downstream failure.

### Candidate acquisition
Test coordinate rank/Top-K survival at identical K or exact retained probability mass.

### Coalition/assembly
Condition on an identical frozen candidate universe. When useful for research isolation, an oracle candidate universe containing the known target winners plus random decoys may be used **only as a labelled post-hoc diagnostic** to ask whether the assembler can identify the correct coalition. It provides no candidate-acquisition credit.

### Morphology
Measure winning-line retention divided by legal-space/survivor-space retention. Compression alone is not predictive lift.

### Winner-Float
Measure winning-line rank/percentile inside the identical frozen survivor universe.

### Portfolio
Compare identical line budgets and exposure/diversity constraints.

This prevents a useful downstream algorithm from being blamed for an upstream acquisition miss, and prevents a weak upstream algorithm from receiving credit for downstream geometry.

## 8. Search-budget and derivative-hypothesis accounting

External idea mining can create substantial researcher degrees of freedom.

Every championship must record:

- number of mathematical formulations tried;
- windows;
- thresholds;
- transformations;
- graph constructions;
- cluster counts;
- random seeds when material;
- stage placements;
- metrics inspected;
- other choices made after seeing results.

If a useful formulation is discovered after comparing alternatives, its retrospective result is discovery evidence only. Nominal p-values from that search are not confirmatory.

The surviving formulation must be frozen as a **derivative prospective hypothesis** before it can gain stronger evidence.

This is how a contribution may legitimately progress from:

`external idea -> decomposition -> exploratory championship -> derivative hypothesis -> prospective shadow -> reproduction -> promotion review`.

## 9. Evidence classification is component-specific

Do not assign one evidence label to an entire external document when its components differ materially.

Permitted outcomes include, for example:

- original architecture: `REJECT`;
- data provenance claim: `REJECT`;
- one algorithmic component: `PROVISIONAL_SIGNAL`;
- another component: `INSUFFICIENT_EVIDENCE`;
- a methodological correction: `BREAKTHROUGH` if it is a demonstrated mathematical/governance necessity rather than predictive superiority.

The evidence label must always state what claim it applies to.

## 10. Promotion and authority

A successful extracted operator does not inherit the authority requested by the external contributor.

Grant the lowest-risk authority needed for the next test:

1. diagnostic;
2. shadow score;
3. soft ranker;
4. exposure adjustment;
5. portfolio allocation;
6. pruning;
7. hard veto.

A component discovered in an exploratory championship should normally begin as a new shadow experiment even when its retrospective diagnostics are strong.

No outside contribution may alter an already frozen cycle artifact.

## 11. Rejection standard

Before rejecting the underlying mathematical idea of a substantial external contribution, reviewers should be able to answer:

1. Was the proposal decomposed into meaningful operators?
2. Was each operator tested at the stage proposed by the contributor?
3. Was a plausible alternative stage considered where the mathematics suggested one?
4. Were external performance claims separated from fresh HEPS reconstruction?
5. Were matched exposure and exact structural controls used?
6. Was search/multiple-testing exposure recorded?
7. Could the apparent failure be caused by an upstream/downstream stage mismatch rather than absence of information?

A reviewer may still reject immediately when the mathematics is invalid, target-leaking, non-falsifiable, or equivalent to a previously rejected operator with no genuinely new information.

## 12. Durable artifacts

For a material outside contribution, preserve where practical:

- original contribution under `collaboration/` or the relevant source area;
- red-team provenance audit;
- algorithm championship or decomposition report;
- derivative experiment package for any survivor;
- explicit decision showing accepted, reworked, and rejected components.

Do not rewrite the original source artifact to make it conform to HEPS after the fact.

## 13. Governing principle

HEPS evaluates **information**, not reputation, terminology, presentation quality, or the contributor's confidence.

An outside agent may be wrong about why an algorithm works, wrong about where it belongs, or wrong about its measured performance, while still contributing a useful mathematical transformation.

The HEPS research process should be skeptical enough to reject unsupported claims and curious enough to avoid throwing away a real signal hidden inside a flawed proposal.
