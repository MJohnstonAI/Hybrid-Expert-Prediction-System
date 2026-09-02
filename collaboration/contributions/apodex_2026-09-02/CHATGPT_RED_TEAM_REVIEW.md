# ChatGPT Red-Team Review — Apodex HEPS Contribution

**Date:** 2026-09-02  
**Reviewer:** ChatGPT GPT-5.6 Sol  
**Scope:** supplied reports and `heps_improved_acquisition_engine.py`  
**Evidence status:** component-specific; no predictive promotion

## Executive decision

Apodex contributes useful HEPS infrastructure ideas and some correct computational operators, but the supplied engine must **not** replace E0021 as-is.

The original source code executed and its bundled unit tests passed. Independent review then identified three material implementation defects that the bundled tests do not detect.

## Reproduced positives

### 1. Exact-null recovery machinery

The dynamic-programming legal-line machinery reproduces the exact order-statistic slot marginals and global anywhere-inclusion probability 0.1 when the residual field is neutral.

The supplied tests passed:

- exact slot-null recovery;
- exact anywhere inclusion 5/50;
- `M(K)` DP versus brute-force containment;
- Top-20 beam versus brute-force within a K13;
- probability-budget consistency.

This is useful implementation infrastructure for a repaired E0021 engine.

### 2. Complete-line containment objective

The `M_k_containment` dynamic program is a practical implementation of the retained E0019/E0021 complete-line-containment objective and matched brute force in the supplied test.

### 3. Walk-forward harness architecture

The overall replay structure correctly attempts to fit on `history[:t]` before scoring target `t`, and reports proper-score deltas plus fixed-K recall. This is the right orchestration pattern even though some component models inside it need repair.

### 4. Canonical-ledger replay reproduced the reported neutral K13 result

Using the 27 Main mechanical-era draws from 2026-06-02 through 2026-09-01, the supplied engine reproduced approximately:

- mean K13 hits: `1.25` versus IID expectation `1.30`;
- mean marginal log-loss delta versus structural null: about `-0.855` (worse than null under the engine's sign convention where positive is improvement);
- mean inclusion-Brier delta versus structural null: about `-0.00136` (worse than null);
- adjacent-slot preserved K13 mean hits: also `1.25`.

This supports Apodex's honest conclusion that the supplied model does not demonstrate a predictive edge on the current ledger.

## Material defects

### Defect A — the claimed signed-displacement model is not actually conditional on the previous coordinate

Supplied form:

`q_j(x | p) proportional to P0_j(x) * exp(phi_j * (x - p))`.

For fixed previous coordinate `p`:

`exp(phi*(x-p)) = exp(phi*x) * exp(-phi*p)`.

The `exp(-phi*p)` factor is constant over all candidate `x` and cancels in normalization. Therefore:

`q_j(x | p) = q_j(x)`.

The fitted distribution is an exponential **slot-coordinate tilt**, not a signed-displacement transition model conditioned on `p`.

Independent numerical check gave essentially zero difference between the normalized field for different previous coordinates (floating error ~`2e-17`).

This is a semantic and mathematical mismatch with E0021's intended transition model.

### Required repair

Use a genuinely `p`-dependent low-dimensional potential, for example a single coherent transition family containing basis functions such as:

- `sign(delta)`;
- `log(1+abs(delta))`;
- a small preregistered interaction or spline basis;

with `delta=x-p` and strong shrinkage. These may be basis functions inside **one** transition model; they must not be treated as independent HLR/VVD expert votes.

## Defect B — the adjacent-slot preserver cannot normally change a Top-13 basket

The routine starts from `base_k13 = Top13(p_anywhere)`.

It permits an outside coordinate `v` to replace a retained member only if:

`p_anywhere[v] > min(p_anywhere[m] for m in base_k13)`.

But by definition every coordinate outside the Top-13 has probability less than or equal to the weakest Top-13 member (apart from tie-order edge cases). Therefore the replacement condition is normally impossible.

Independent test on a non-null field produced no displacement; logically this follows from Top-K ordering itself.

This explains why the real-ledger replay reported identical base and 'preserved' K13 hit rates.

### Required repair

Adjacent-slot preservation must trade seats using a **different preregistered objective** from the base anywhere marginal—for example expected containment-mass change, bounded adjacent-slot residual evidence, or a separate target-blind migration score—while maintaining K=13. It cannot require an omitted coordinate to beat the Top-13 cutoff on the same score that omitted it.

## Defect C — the PowerBall championship implementation is invalid

In `pb_shrunk_field`:

- the uniform quantity is calculated as `16 * log(1/16)`, which is negative;
- shrunk quantities are sums of `-log(probability)`, which are positive;
- `min(...)` therefore mechanically selects the negative uniform value.

Additionally, the routine is not scoring the probability assigned to the **withheld realized PB target** in walk-forward fashion; it sums losses over the full 1..16 support instead.

Independent check returned a negative uniform 'log loss' around `-44.36` against positive shrunk scores, forcing uniform selection.

### Required repair

For each withheld PB target `y_t`, compare preregistered fields using target log loss `-log p_t(y_t)` and/or multiclass Brier score. Accumulate only out-of-sample target scores. Hyperparameters must be frozen before the prospective target or selected using nested/pre-target rules.

## Additional caution — coalition 'PMI' is not a normalized PMI probability model

The supplied coalition shadow uses smoothing denominators that do not correspond to the actual total singleton and pair event counts (five singleton inclusions and ten unordered pairs per draw). Its score is better interpreted as a shrunk association heuristic than literal PMI.

This does not automatically make the ranking useless, but the probability interpretation should be removed and the operator should enter an E0013 challenger experiment only after a marginal-conditioned derivation and oracle-K13 tie-safe comparison.

## Component disposition

| Component | Decision |
|---|---|
| Legal-line DP / exact null recovery | ACCEPT AS METHODOLOGICAL INFRASTRUCTURE CANDIDATE |
| `M(K)` containment DP | ACCEPT AS METHODOLOGICAL INFRASTRUCTURE CANDIDATE |
| Walk-forward proper-score harness skeleton | ACCEPT FOR REPAIR/INTEGRATION |
| One-parameter `phi*(x-p)` acquisition model | REJECT AS E0021 SIGNED-TRANSITION IMPLEMENTATION; REWORK |
| Adjacent-slot preservation routine | REJECT CURRENT FORM; REWORK |
| PB championship routine | REJECT CURRENT FORM |
| Shrunk coalition shadow | INSUFFICIENT_EVIDENCE / RE-DERIVE |
| Machine-provenance backfill | ACCEPT AS DATA-QUALITY PRIORITY |
| Search-exposure registry | ACCEPT AS GOVERNANCE/INFRASTRUCTURE PRIORITY |
| Automated first-failure tracing | ACCEPT AS GOVERNANCE/DIAGNOSTIC PRIORITY |
| Scenario-mixture allocator | PROPOSED RESEARCH; requires preregistration and matched-budget test |

## Forward use recommendation

Do **not** copy the whole source file into production code.

Instead extract the validated infrastructure into a repaired E0021 implementation and create explicit tests for:

1. previous-state sensitivity: changing `p` must change the transition distribution when learned transition parameters are non-zero;
2. neutral-field exact uniform legal-line recovery;
3. fixed-K adjacent-preservation seat trades that can actually occur under a preregistered alternative score;
4. no preservation trade unless the declared objective improves;
5. PB walk-forward proper scores against uniform and shrunk baselines;
6. canonical Main walk-forward replay with all target rows excluded from fitting;
7. exact 1,287-line assembly enumeration when K13 contains the winners.

## Predictive conclusion

The Apodex package does **not** establish prediction lift. Its own reproduced Main replay is slightly worse than the exact null on proper scores and slightly below random K13 expectation. The value of the contribution is presently architectural and implementation-oriented: it supplies reusable DP/harness scaffolding and exposes a sensible roadmap, but its central transition and PB implementations require correction before use in Friday or later prediction slates.