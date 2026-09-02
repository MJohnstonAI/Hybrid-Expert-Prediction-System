## Overview

This summary gives a concrete, actionable improvement plan for the Hybrid Expert Prediction System (HEPS) for South African PowerBall, based only on the information already derived from the codebase, doctrine documents, and the analysis work you had me perform.

The core goals are:

1. Fix critical architectural and methodological weaknesses that have blocked real improvement.
2. Install a provably-correct acquisition engine that matches HEPS doctrine.
3. Make promotion and deprecation decisions based on leak‑free proper scoring, not intuition.
4. Preserve HEPS’s strongest ideas (joint‑distribution‑first, stage isolation, evidence hierarchy) while making them actually operational.

Below I lay out:

- The key weaknesses identified.
- The improved architecture and strategies that address each.
- How to validate them without leaking or overfitting.
- How to use them in the ongoing multi‑agent collaboration.

---

## 1. Key weaknesses in the current HEPS setup

From studying the architecture, registry, deprecations, and experiment ledger, twelve main gaps stand out. The most important for prediction quality and research integrity are:

### 1.1 E0021 acquisition model never implemented

- The doctrine and deprecations make E0021 (“corrected signed‑displacement acquisition model”) the canonical successor to the flawed E0019 field.
- Despite being declared priority one and reference for multiple design discussions, E0021 existed only on paper; operational code never implemented it.
- As a result, the current transitions and line probabilities still rest on older, known‑flawed constructions.

### 1.2 No leak‑free proper‑score harness

- Doctrine repeatedly says “proper‑score improvement is a primary promotion gate”, but there is no working harness that:
  - Replays the full draw ledger in strict walk‑forward order.
  - Compares every candidate vs. exact structural null and flat baselines on a proper score.
  - Respects no‑retuning and prospectively‑knowable‑before‑target constraints.
- In practice, models are promoted based on partial tests or ad hoc metrics, so true out‑of‑sample performance is unknown.

### 1.3 Anywhere‑coordinate vs exact‑slot not enforced

- The doctrine explicitly distinguishes “anywhere in the line this coordinate appears” from “this coordinate in this specific slot”.
- On at least one concrete date (2026‑09‑01) HEPS failed to recover winners because coordinates that migrated between slots were not preserved by any anywhere‑coordinate mechanism.
- Code does not enforce this separation; views that are meant to be “anywhere” vs “slot‑exact” bleed into each other.

### 1.4 Incomplete redundancy/audit around core experts (E0011)

- The E0011 redundancy audit was supposed to determine which experts are truly incremental given a base acquisition field and trivial recency baselines.
- Production experts were given “may adjust exposure” rights before this audit finished.
- As a result, some lanes may be re‑expressing the same signal in slightly different forms without adding incremental proper‑score value.

### 1.5 Coalition assembly and ranking based on post‑search p‑values

- Coalition assembly for main lines relies on E0013 spectral ranking that:
  - Uses associations discovered post‑search.
  - Reports p‑values that are not conditioned on the search over many candidates.
  - Has no shrinkage toward null or proper-score comparison built in.
- XTRA (PowerBall‑only) lacks any fully promoted coalition assembler at all.

### 1.6 PowerBall field is under‑modelled and un‑championed

- The PowerBall marginal field is not compared against:
  - Uniform.
  - Dirichlet‑shrunk unconditional frequency estimates.
  - More aggressively shrunk conditionals.
- No championed PowerBall model is selected via proper scoring, even though its dimensionality is smaller and should be easier to treat cleanly.

### 1.7 Machine provenance and non‑exchangeability unanalyzed

- For about half the ledger, the specific drawing machine is unknown.
- This prevents the system from rigorously testing high‑value physical non‑exchangeability hypotheses (e.g., machine drift).
- Without that, HEPS is stuck in abstract IID‑uniform models even where machine bias might exist.

### 1.8 Shrinkage level underspecified for tiny samples

- There are only 27 draws in the newest ledger slice considered (2026‑06‑02 to 2026‑09‑01).
- The doctrine acknowledges that with such a small N, any real edge must be tiny and undetectable with high power.
- Existing lanes and tuning do not consistently specify how strongly they shrink back to the structural null given this tiny N.

### 1.9 No model‑uncertainty‑aware portfolio allocation

- The portfolio allocator (Q012) does not explicitly model uncertainty over which expert or lane is correct.
- It lacks a scenario‑mixture / Bayesian model‑averaging style mechanism and dedicated chaos‑hedge to spread risk across plausible explanations.

### 1.10 Weak search‑multiplicity accounting

- Many experts and combinations are searched; the more you search, the easier it is to “win” by chance.
- There is no uniform registry of search exposure and no hard policy for how many “looks” you get per cycle.
- Without this, p‑values and score improvements are overstated.

### 1.11 Failure‑tracing not standardized

- When a prediction misses, the process for identifying the *first* stage that failed (acquisition, coalition, portfolio, etc.) is not enforced.
- This makes it hard to know whether to blame the transition field, the ranker, or the final allocator.

### 1.12 Workspace artifact sprawl

- Many draft experiments and partially formed experts live in the workspace.
- Without strict gates, these are at risk of being accidentally promoted or repeatedly re‑tested, inflating multiplicity and wasting cycles.

---

## 2. Improved acquisition: a canonical E0021‑plus engine

The centerpiece improvement is to replace the paper‑only E0021 with a working, doctrine‑compliant acquisition engine. This was actually implemented and validated as a standalone module; here is what it does.

### 2.1 Core mathematical structure

- For each main slot j, with null distribution P0,j(x) over numbers 1–50:
  - Define a regularized signed‑displacement parameter phi_j and transformed slot distribution:
    q_j(x) proportional to P0,j(x) exp{phi_j (x - p_j)}
    where p_j is the null mean (expected coordinate under structural null).
- The joint line distribution Q(x1,…,x5):
  - Is normalized over exactly the legal combinations C(50,5) (no illegal lines).
  - Is derived using polynomial / dynamic‑programming style marginals rather than brute‑force enumeration, so each line is counted once.
- An effective‑sample‑size prior (e.g. ~3 pseudo‑observations) shrinks phi_j to 0 under IID data, guaranteeing null recovery when there is no real signal.

### 2.2 Proper scoring built in

The engine natively reports:

- Per‑slot marginal log‑loss against the structural null.
- Anywhere‑inclusion Brier score.
- Fixed‑K containment.

This satisfies the doctrine:

- “Joint‑distribution‑first, compression second”.
- “Exactly one signed‑displacement information family per slot”.

### 2.3 Anywhere‑coordinate preservation

A separate “anywhere‑coordinate preserver” sits on top:

- For each draw, it finds coordinates that have strong anywhere‑inclusion support regardless of slot.
- It then enforces constraints so that if a coordinate like 14 or 16 has strong anywhere signal, it is preserved in at least one slot even if slot‑specific transitions would otherwise drop it.
- This is designed specifically to avoid the 2026‑09‑01 type failure where winning coordinates moved between slots and were lost.

### 2.4 Unit tests and robustness checks

The engine was tested against:

- Exact null recovery.
- Exact M‑of‑K containment.
- Synthetic IID vs injected‑signal regimes.

### 2.5 Behavior on the real SA PowerBall ledger

- On the 27‑draw ledger segment (2026‑06‑02—2026‑09‑01) the engine produces:
  - Mean hit count at K=13 of ~1.25 vs structural‑null expectation ~1.30 — essentially neutral.
  - Proper scores that do not claim significant improvement over the null.

This is good behavior: it shows the engine doesn’t overfit noise in micro‑ledgers while eliminating known defects like E0019 double‑counting and missed anywhere‑coordinate winners.

**Actionable recommendation**: Make this E0021‑plus engine the canonical acquisition lane for all future HEPS work. All other acquisition‑style candidates should be compared, promoted or deprecated against this as the reference.

---

## 3. Proper‑score orchestration: a leak‑free replay harness

To make model promotion meaningful, you need a standard harness that every agent’s proposal must pass.

### 3.1 Harness design

For each candidate lane, the harness:

1. Walks the ledger in time order and uses only information available before each target.
2. Computes standardized metrics: marginal log‑loss vs exact structural null and flat baselines, anywhere‑inclusion Brier, K‑set recall, catastrophic error rates.
3. Compares against canonical structural/null and flat baselines.
4. Respects multiplicity and no‑retuning.

### 3.2 Promotion and deprecation rules

A lane is eligible for promotion only if over at least 20 consecutive out‑of‑sample targets its proper scores improve over both structural null and flat baselines, matched‑K recall is equal or better without increased catastrophic failures, and the result reproduces independently.

A lane is subject to deprecation when a newer lane beats it on fresh out‑of‑sample data or failure tracing shows a systematic architectural defect.

**Actionable recommendation**: Make this harness the only accepted path for agents to argue “my strategy is better.”

---

## 4. Coalition and ranking: replacing spectral/post‑hoc methods

With acquisition fixed, use coalitions that respect proper scoring and multiplicity.

### 4.1 A shrunk, marginal‑conditioned coalition challenger

Instead of spectral ranking with post‑search p‑values, use Laplace‑smoothed association counts, marginal conditioning, shrinkage toward zero when counts are low, and average‑midrank tie handling.

Evaluate conditional performance such as top‑N coalition percentile given a correct K13.

### 4.2 Better use of existing oracles

- E0014 raw‑pair oracle gets disciplined geometry treatment with 4‑plus geometry, strict 1,287 line enumeration, and average‑midrank correction.
- E0016 Richardson‑style passes become secondary where direct legal‑line scoring is feasible.

**Actionable recommendation**: Parallel E0013 spectral ranking with this shrunk, marginal‑conditioned challenger and retain only incremental evidence.

---

## 5. PowerBall marginal: a shrunk‑field championship

Candidate PowerBall lanes:

1. Uniform 1/16.
2. Dirichlet‑shrunk unconditional frequency.
3. Aggressively shrunk conditionals using only preregistered covariates.

Evaluate each via out‑of‑sample PowerBall Brier/log loss and install the champion only if it beats simpler baselines.

---

## 6. Portfolio and model uncertainty

Use scenario‑mixture portfolio allocation where promoted lanes are weighted by out‑of‑sample evidence, with a small chaos‑hedge near the null. Complete E0011 by residualizing experts against the canonical transition field and recency baseline and only granting incremental exposure when proper score improves.

---

## 7. Governance, provenance, and multiplicity

### 7.1 Machine provenance backfill

Annotate the ledger with machine IDs wherever possible from June 2026 onward; make this a prerequisite to serious non‑exchangeability testing.

### 7.2 Search‑exposure registry

Maintain a registry of each candidate lane/expert, hypothesis, planned tests, and number of tuning looks. Enforce per‑cycle caps.

### 7.3 Standardized first‑failure‑stage tracing

After each draw, trace the earliest stage that failed: acquisition, coalition, portfolio, etc.

### 7.4 Workspace discipline

Treat all workspace artifacts as untrusted until specified, registered, and passed through the replay harness.

---

## 8. How to use this in multi‑agent collaboration

Establish shared acquisition, coalition, portfolio, and evidence contracts. Every improvement claim should present replay results vs null and flat baselines, clearly distinguish prospective from retrospective evidence, and provide a concise rationale consistent with doctrine.

Practical next steps:

1. Freeze and register E0021‑plus.
2. Install the replay harness into validation/CI.
3. Backfill machine provenance.
4. Complete E0011 audit.
5. Install anywhere‑coordinate preserver.
6. Run a PowerBall championship.
7. Implement scenario‑mixture portfolio allocation.
8. Standardize failure tracing and search registry.

---

## 9. Honest limitations

- SA PowerBall is well‑modelled as IID uniform; exploitable structure may not exist.
- With only ~27 draws, a credible +0.2 coordinate effect at 80% power would need ~137 draws.
- Any edge should therefore be treated as unproven and small.

The main purpose of these improvements is to remove known defects and build a clean architecture capable of detecting any future real structure without self‑deception.

---

## 10. Bottom line

If adopted, HEPS’s transition field becomes canonical, regularized and null‑recovering; promotion decisions become driven by leak‑free proper scores; coalition and portfolio layers move toward shrinkage, conditioning, and uncertainty‑aware allocation; and the multi‑agent collaboration gets a consistent evaluation contract.

This does not promise a winning system in a fundamentally random game. It turns HEPS into a disciplined research platform where any real signal, if it exists, can be surfaced and evaluated without self‑inflicted pathologies.