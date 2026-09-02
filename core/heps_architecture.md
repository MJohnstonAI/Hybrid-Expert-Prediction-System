# HEPS Master Architecture

## Architecture

**HEPS v35.0 — Joint-Distribution-First Staged Mixture-of-Experts**

**Updated:** 2026-09-02  
**Status:** active methodological architecture; predictive authority remains expert/experiment specific.

## Purpose

HEPS is a multi-agent, paper-trading research system for South African PowerBall. It separates:

- exact lottery geometry;
- learned residual probability fields;
- candidate acquisition;
- coalition/ranking;
- portfolio geometry;
- PowerBall modelling;
- research governance.

Historical experiments remain immutable evidence of what was tested. Current forward-use authority is controlled by `AGENTS.md`, `governance/current_method_doctrine.md`, `governance/methodology_deprecations.md`, and `core/expert_registry.yaml`.

## Data doctrine

- Canonical Main ledger: `data/draw_history.jsonl`
- Current ledger through: 2026-09-01 / draw id 27
- Game format: Main 5 unique numbers from 1-50 + PowerBall 1-16
- Slot1-Slot5 are sorted order statistics, not physical extraction order
- `game_format`, `draw_method`, and `machine_name` are distinct metadata axes
- Never infer machine/method from outcome patterns or date alone
- Pre-June legacy artifacts may be used only when explicitly allowed for discovery/robustness and may not silently set active-era parameters

## Architecture principle 1 — joint distribution first

For Main, the legal next-draw state space has:

`C(50,5)=2,118,760`

legal sorted lines.

HEPS should estimate learned information parsimoniously, but where feasible normalize the resulting field over this exact legal state space before candidate compression.

This means:

`low-dimensional residual information -> coherent legal-line probability field -> derived marginals -> K compression -> assembly -> portfolio`

not:

`many correlated feature votes -> arbitrary score -> K compression`.

## Architecture principle 2 — one transition information family

For sorted slot `j`:

`DELTA_j = X_j(t) - X_j(t-1)`.

The following are deterministic views of the same transition:

- HLR = sign(`DELTA_j`)
- VVD = abs(`DELTA_j`)
- target coordinate = previous coordinate + `DELTA_j`
- terminal digit = target coordinate mod 10

Therefore these views may not be multiplied or counted as independent expert evidence.

For new research, `MAIN_SIGNED_SLOT_TRANSITION` is the canonical transition representation. HLR/VVD/terminal remain useful diagnostics and interpretable outputs.

Historical E0019 HLR×VVD and E0020 terminal×HLR×VVD formulas are superseded for forward reuse; see `governance/methodology_deprecations.md`.

## Architecture principle 3 — proper score before compression credit

An optimized K13/K20 may look better by chance or by exploiting a misspecified score.

Therefore candidate acquisition is evaluated in this order:

1. full-support proper score vs structural/simple controls;
2. fixed-K recall and 3+/4+/5 survival;
3. catastrophic exclusions;
4. complete-line containment probability;
5. downstream coalition/ranking;
6. portfolio performance.

Better K recall with a worse probability field is not sufficient for predictive promotion.

---

# Matrix A — Main Architecture

## Stage 0 — Exact structural baseline

Required controls include:

- `NULL_ORDER_STATISTIC_SLOT`
- `NULL_HLR_STRUCTURAL`
- `NULL_VVD_STRUCTURAL`
- `NULL_HLR_JOINT_243`
- `NULL_GAP_DM`
- flat global inclusion 0.1 per coordinate

These are methodological controls, never ensemble votes.

## Stage 1 — Transition / Slot Forecast

Purpose: estimate next sorted-slot movement without double-counting derived views.

Preferred new research representation:

`MAIN_SIGNED_SLOT_TRANSITION`.

Outputs may be transformed into HLR/VVD/terminal probabilities for interpretation and scoring, but those transforms remain one information family.

Current important shadow research:

- E0005 BARP HLR state-duration model;
- E0005 VVD-R diagnostic distribution;
- E0021 corrected signed-displacement successor.

### 2026-09-01 lesson

From previous `19,22,24,25,47`, the realized HLR for `14,16,31,34,40` was `LLHHL`. The frozen BARP modal vector was also `LLHHL`, an exact 5/5 direction hit. This earns bounded one-target preservation/scenario credit, not promotion or retuning.

## Stage 2 — Candidate Funnel

Purpose: preserve useful coordinates at a declared K before combination assembly.

Key doctrine:

- exact-slot probability and anywhere-coordinate probability are separate;
- strict slot provenance may not automatically discard a strong global coordinate;
- adjacent-slot preservation may be tested prospectively at fixed K;
- K expansion receives no predictive credit;
- K13 remains the primary acquisition research target but is falsifiable.

### E0019 -> E0021 transition

Retain from E0019:

- complete-line containment objective `M(K)`.

Reject/supersede:

- HLR×VVD residual-product probability field.

E0021 is the designated corrected successor using one signed-transition information family, legal-line normalization, proper-score-first gating, and a separate adjacent-slot preservation arm.

Independent candidate shadows may include E0016 nonequilibrium current, but their incremental value must be tested after redundancy controls.

## Stage 3 — Coalition Assembly

Purpose: estimate which frozen candidate coordinates belong together.

E0013 Positive-PMI spectral remains a coalition-only `PROVISIONAL_SIGNAL` shadow.

Important correction:

For unordered anywhere-coordinate pairs, uniform 5/50 gives the same null co-inclusion probability to every distinct pair. Do not invent a coordinate-varying "central pair geometry" correction. A stronger E0013 challenger should condition/shrink association using observed marginals `C_i,C_j`.

Coalition methods have zero candidate-discovery credit unless separately tested upstream.

## Stage 4 — Morphology

Purpose: evaluate completed legal lines using structural features such as:

- gaps;
- parity/register;
- sum/spread;
- SLDV/terminal morphology;
- other preregistered line-shape features.

Common morphology is not itself predictive evidence. Every morphology rule must be compared with its combinatorial base rate and matched controls.

Rejected gap-density/JOS-HDR formulations remain historical only.

## Stage 5 — Winner-Float Ranking

Purpose: rank legal surviving combinations.

Evaluate:

- exact winning-line rank;
- percentile;
- Top-N survival;
- paired delta vs random/simple/incumbent rankers;
- stage-isolated attribution.

Do not credit a ranker when the winning coordinates never survived acquisition.

## Stage 6 — Portfolio Optimization

Purpose: select a fixed paper-trading line budget while controlling concentration and duplicate exposure.

Johnson covering/maximum-coverage methods belong here or in assembly only after candidates are frozen. They have zero candidate-discovery authority.

Portfolio diversification is a robustness/variance question, not proof that expected lottery return changes.

---

# Matrix B — PowerBall Architecture

PowerBall remains a separate 1..16 process.

Near-term model championship should emphasize:

- uniform 1/16;
- strongly shrunk unconditional frequency;
- strongly shrunk exact-state conditional transitions;
- strongly shrunk VVD-state conditional transitions;
- incumbent PB comparator.

Primary evidence should be proper score. Exact hit rate is secondary.

PB HLR/VVD/terminal/exact-state representations of one transition are not independent votes.

Sparse state counts prohibit high-confidence conditional authority until prospective evidence beats simpler baselines.

---

# Independent-information doctrine

HEPS no longer defines an expert merely as a differently named feature.

An expert is a candidate information source that adds residual predictive value beyond:

- exact structural geometry;
- simple baselines;
- already-used information families.

Before expert convergence increases confidence:

1. control structural effects;
2. control simple frequency/recency where relevant;
3. examine residual dependence;
4. measure incremental proper-score or stage-isolated value.

Functionally derived views count as one information family.

---

# Machine / physical research

If a real mechanical-era edge exists, persistent or regime-specific ball/machine non-exchangeability is a higher-value hypothesis than inventing more transforms of prior winning numbers.

But:

- machine/ball-set state must be prospectively knowable or provenance-qualified;
- unknown remains a valid state;
- no outcome-optimized regime split;
- strong hierarchical shrinkage is mandatory at current sample sizes;
- physical mechanism claims require more than sorted-number behavior.

E0016 nonequilibrium current is a statistical chronology operator, not evidence of literal particle flow. Levy remains diagnostic only. Richardson pair-separation estimators may remain shadow, but historical geometric-mean message passing is heuristic rather than exact joint inference.

---

# Per-draw cycle

## Pre-draw

Freeze:

1. canonical data state;
2. governance/architecture version;
3. expert formulas and authority;
4. full probability fields where available;
5. K baskets and exact exposure;
6. coalition/ranking outputs;
7. final paper-trading slate.

## Post-draw

After result verification:

1. append/validate the result;
2. score all frozen arms;
3. trace each winner through the pipeline;
4. identify first failure stage;
5. separate exact-slot from anywhere-coordinate credit;
6. update claim/failure registries;
7. apply only preregistered next-target learning rules;
8. never regenerate old predictions.

---

# 2026-09-01 Physics of Failure summary

Actual: `14,16,31,34,40 | PB4`.

Successes:

- BARP modal HLR: exact `LLHHL` 5/5 direction hit;
- 31 retained and strongly ranked in S3 diagnostics;
- 34 retained and ranked #1 in S4 diagnostic field;
- 40 survived wider diagnostic candidate exposure;
- terminal S3=1 and S4=4 top calls were correct.

Failure:

- primary K13 retained only 31 and 34;
- 14/16 useful coordinate evidence was partly lost by strict slot provenance;
- candidate acquisition/compression remained the first binding failure.

Operational consequence for 2026-09-04 is encoded in `cycles/2026-09-04/pre_draw/expert_credit_policy.json`: bounded reward, no retuning or one-draw promotion.

---

# Evidence doctrine

Use exact evidence labels:

- `BREAKTHROUGH`
- `PROVISIONAL_SIGNAL`
- `INSUFFICIENT_EVIDENCE`
- `REJECT`

A methodological breakthrough (e.g. exact null or dependency correction) is not automatically a predictive breakthrough.

Current predictive state remains dominated by `INSUFFICIENT_EVIDENCE` and shadow/provisional components.

---

# Current priorities

See `knowledge/open_questions.md`. Highest-value active directions are:

1. E0021 corrected signed-displacement legal-line acquisition;
2. fixed-K adjacent-slot/anywhere-coordinate preservation;
3. E0011 redundancy audit;
4. E0013 marginal-conditioned/shrunk coalition challenger;
5. machine/ball-set non-exchangeability when metadata permit;
6. strongly shrunk PB championship;
7. calibrated full-support modelling to reduce catastrophic exclusions.

Avoid reopening deprecated strategies without materially new information. Use `governance/methodology_deprecations.md` as the forward-use map.