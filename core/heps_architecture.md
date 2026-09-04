# HEPS Master Architecture

## Architecture

**HEPS v35.3 — Joint-Distribution-First Staged Mixture-of-Experts with Candidate-Frozen Pattern Triage**

**Updated:** 2026-09-04  
**Status:** active methodological architecture; predictive authority remains expert/experiment specific.

## Purpose

HEPS is a multi-agent, paper-trading research system for South African PowerBall. It separates:

- exact lottery geometry;
- learned residual probability fields;
- candidate acquisition;
- candidate-frozen pattern triage;
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

## Architecture principle 4 — pattern constraints act after candidate freeze unless separately validated upstream

Pattern-recognition features such as HLR scenario compatibility, last-digit-sum absolute delta, total-sum absolute delta, span absolute delta, parity transition, decade transport, or related morphology must not silently alter K13 membership.

Once K13 is frozen, enumerate all `C(13,5)=1,287` lines and evaluate pattern constraints at the line level. A pattern gate earns elimination authority only when winner retention is materially higher than the fraction of line space retained.

E0029 establishes a new **candidate-frozen Pattern Constraint Triage shadow stage**. Its preferred discovery architecture is conservative: retain the top 80% of adaptive Pattern-OR lines, rescue the top 5% E0013 spectral lines, then rank retained lines by E0013 spectral. This is shadow only until prospective evidence accumulates.

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
- E0021 corrected signed-displacement successor;
- E0026 scenario-constrained slot routing.

### 2026-09-01 lesson

From previous `19,22,24,25,47`, the realized HLR for `14,16,31,34,40` was `LLHHL`. The frozen BARP modal vector was also `LLHHL`, an exact 5/5 direction hit. This earns bounded one-target preservation/scenario credit, not promotion or retuning.

## Stage 2 — Candidate Funnel

Purpose: preserve useful coordinates at a declared K before combination assembly.

Key doctrine:

- exact-slot probability and anywhere-coordinate probability are separate;
- unrestricted anywhere probability must not erase slot provenance;
- E0026 preserves candidate + admissible slot provenance + scenario probability;
- adjacent-slot preservation may be tested prospectively at fixed K when scenario-valid;
- K expansion receives no predictive credit;
- K13 remains the primary acquisition research target but is falsifiable.

### E0019 -> E0021 -> E0026 transition

Retain from E0019:

- complete-line containment objective `M(K)`.

Reject/supersede:

- HLR×VVD residual-product probability field.

E0021 is the designated corrected signed-transition successor using one transition information family, legal-line normalization, proper-score-first gating, and fixed-K adjacent-slot preservation research.

E0026 further refines preservation: a candidate must retain explicit slot provenance and may migrate only through non-negligible pre-draw scenarios compatible with HLR/signed displacement, exact order-statistic support, and legal sorted-line geometry. Unrestricted anywhere-coordinate promotion is not allowed.

Independent candidate shadows may include E0016 nonequilibrium current, but their incremental value must be tested after redundancy controls.

## Stage 3 — Frozen-K13 Enumeration and Coalition Assembly

Purpose: estimate which frozen candidate coordinates belong together.

When K13 is frozen, enumerate **all**:

`C(13,5)=1,287`

legal five-number combinations before pruning/ranking. Do not lose the true line through heuristic generation shortcuts.

E0013 Positive-PMI spectral remains a coalition-only `PROVISIONAL_SIGNAL` shadow.

For unordered anywhere-coordinate pairs, uniform 5/50 gives the same null co-inclusion probability to every distinct pair. Do not invent a coordinate-varying central-pair structural correction. A stronger E0013 challenger should condition/shrink association using observed marginals `C_i,C_j`.

E0022 `MAIN_ASSEMBLY_DISSENT_OR` remains a prospective shadow robustness ranker:

`max(midrank_percentile(frequency), midrank_percentile(recency), midrank_percentile(E0013_spectral))`.

It has zero candidate authority and no new promotion from E0029; the E0029 replay found it approximately random on mean oracle-K13 percentile.

E0022's four-node nucleus and conditional-completion formulations remain rejected in their current forms.

## Stage 3.5 — Candidate-Frozen Pattern Constraint Triage (E0029 shadow)

Purpose: eliminate or demote implausible **lines inside a frozen K13** while controlling catastrophic winner loss.

Adaptive E0029 pattern lanes are fitted target-excluded from earlier Main draws only:

- BARP HLR residual relative to exact structural HLR null;
- adaptive LDSAD residual;
- adaptive total-sum absolute-delta (`SUMAD`) residual;
- adaptive span absolute-delta (`SPANAD`) residual.

The three whole-line delta fields use strong `kappa=20` shrinkage in the E0029 discovery replay.

Define:

`MAIN_PATTERN_OR = max(midrank_pct(HLR), midrank_pct(LDSAD), midrank_pct(SUMAD), midrank_pct(SPANAD))`.

This is one robustness/meta-pattern operator, not four independent likelihood votes.

### Preferred E0029 shadow cascade

`MAIN_PATTERN80_SPECTRAL5_RESCUE`

1. retain Pattern-OR top 80% of the 1,287 lines;
2. rescue any line in E0013 spectral top 5%;
3. rank retained lines by E0013 spectral;
4. retain excluded lines below the gate in the frozen artifact for audit;
5. apply portfolio geometry only after this stage.

Discovery replay across 19 eligible targets and two independent decoy seeds produced approximately:

- winner percentile `0.637`;
- line retention `0.803`;
- line elimination `0.197`;
- winner gate survival `0.928`.

This is promising stage-isolated discovery evidence but remains `INSUFFICIENT_EVIDENCE`. It has zero production hard-pruning authority until multiple fresh prospective targets confirm the retention/compression advantage.

### Fixed-band research

E0028 LDSAD `11..13` and exploratory SUMAD `8..9` / SPANAD `5..6` bands remain post-hoc frozen diagnostics. They may be scored prospectively but cannot drive promotion from retrospective strength.

## Stage 4 — Morphology

Purpose: evaluate completed legal lines using structural features such as:

- gaps;
- parity/register;
- sum/spread;
- SLDV/terminal morphology;
- transition-pattern residuals declared in E0029;
- other preregistered line-shape features.

Common morphology is not itself predictive evidence. Every morphology rule must be compared with its combinatorial base rate and matched controls.

Rejected gap-density/JOS-HDR formulations remain historical only.

Morphology may not hard-delete lines from a correct K13 oracle universe merely because a line looks unusual. Any pruning authority must independently earn winner-retention lift against its legal-space compression.

## Stage 5 — Winner-Float Ranking

Purpose: rank legal surviving combinations.

Evaluate:

- exact winning-line rank;
- percentile;
- Top-N survival;
- paired delta vs random/simple/incumbent rankers;
- stage-isolated attribution;
- catastrophic burial rate;
- gate survival versus line-retention fraction where a triage layer is used.

For discrete coalition scores with ties, use average midrank or another explicitly justified tie-aware rule. Do not give every tied winner the best rank in its tie block. E0022 showed that optimistic tie treatment materially inflated historical XTRA raw-pair oracle results.

Do not credit a ranker when the winning coordinates never survived acquisition.

## Stage 6 — Portfolio Optimization

Purpose: select a fixed paper-trading line budget while controlling concentration and duplicate exposure.

Johnson covering/maximum-coverage methods belong here or in assembly only after candidates are frozen. They have zero candidate-discovery authority.

Historical `three_plus_first` Johnson covering remains available for audit/backward compatibility. E0022 adds optional `four_plus_first` for the director's high-order match goal. At K13 and a fixed 20-line budget, this raises exact 4+/5 winner-state coverage from 757/1287 (58.82%) to 788/1287 (61.23%) while exact 5/5 state coverage remains 20/1287 for either distinct-line portfolio.

This is deterministic portfolio geometry, not predictive information. Exact 5/5 probability can improve only if an independently validated ranking/posterior assigns non-uniform probability to the 1,287 winner states.

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

Functionally derived views count as one information family. E0029 Pattern-OR is explicitly a robustness meta-operator and may not be interpreted as independent-probability multiplication.

---

# Machine / physical research

If a real mechanical-era edge exists, persistent or regime-specific ball/machine non-exchangeability is a higher-value hypothesis than inventing more transforms of prior winning numbers.

But:

- machine/ball-set state must be prospectively knowable or provenance-qualified;
- unknown remains a valid state;
- no outcome-optimized regime split;
- strong hierarchical shrinkage is mandatory at current sample sizes;
- physical mechanism claims require more than sorted-number behavior.

E0016 nonequilibrium current is a statistical chronology operator, not evidence of literal particle flow. Levy remains diagnostic only. E0027 further rejects current Main Brownian/acceleration/pair-collision predictive formulations; only gap-pressure regularization remains a diagnostic research note.

---

# Per-draw cycle

## Pre-draw

Freeze:

1. canonical data state;
2. governance/architecture version;
3. expert formulas and authority;
4. full probability fields where available;
5. K baskets and exact exposure;
6. all 1,287 K13 lines when K13 is used;
7. Pattern Constraint Triage shadow outputs when E0029 is active;
8. coalition/ranking outputs;
9. final paper-trading slate.

## Post-draw

After result verification:

1. append/validate the result;
2. score all frozen arms;
3. trace each winner through the pipeline;
4. identify first failure stage;
5. separate exact-slot from anywhere-coordinate credit;
6. if K13 contains all five winners, score E0029 gate survival and exact winner rank;
7. update claim/failure registries;
8. apply only preregistered next-target learning rules;
9. never regenerate old predictions.

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

Operational consequence for 2026-09-04 is encoded in the frozen cycle artifacts. E0026 and E0029 may create new **shadow** counterfactuals before the draw, but discovery evidence alone does not retroactively rewrite earlier frozen artifacts.

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

1. E0026 scenario-constrained slot-routed K13 acquisition;
2. E0021 corrected signed-displacement legal-line acquisition and proper-score repair;
3. E0029 prospective Pattern-OR triage plus E0013 spectral-rescue cascade after frozen K13;
4. E0028 LDSAD and related whole-line delta patterns as frozen prospective diagnostics only;
5. E0011 redundancy audit;
6. E0013 marginal-conditioned/shrunk coalition challenger;
7. E0022 four-plus-first Johnson geometry for fixed-budget high-order coverage;
8. machine/ball-set non-exchangeability when metadata permit;
9. strongly shrunk PB championship;
10. calibrated full-support modelling to reduce catastrophic exclusions.

Avoid reopening deprecated strategies without materially new information. Use `governance/methodology_deprecations.md` as the forward-use map.