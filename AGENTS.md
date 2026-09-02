# HEPS Autonomous Agent Constitution

This is the mandatory entry point for every AI model, coding agent, reviewer, synthesizer, or automation operating in the Hybrid Expert Prediction System (HEPS) repository.

HEPS is a multi-agent, paper-trading research environment for South African PowerBall. The repository is scientific memory, experiment ledger, peer-review record, and architecture-evolution record. Historical files are retained for auditability; they are **not automatically current advice**.

## 1. Constitutional invariants

1. **Data integrity** — never alter a historical draw to improve a model.
2. **Temporal integrity** — target draws may not appear in their own training, feature, threshold, or hyperparameter windows.
3. **Evidence integrity** — predictive claims require explicit baselines, denominators, exposure, and proper scoring where probabilities exist.
4. **Architecture integrity** — no agent may silently promote its own unreviewed idea to production authority.
5. **Paper-trading only** — HEPS outputs are research artifacts, not guaranteed or financially reliable gambling advice.
6. **Historical-precedence integrity** — when an old formula conflicts with current doctrine or a later failure/deprecation decision, the later governance interpretation controls future reuse while the old artifact remains immutable historical evidence.

## 2. Mandatory read order — optimized for current work

Read in this order before substantive prediction/research work:

1. `AGENTS.md`
2. `governance/current_method_doctrine.md`
3. `governance/methodology_deprecations.md`
4. `governance/nomenclature.md`
5. `governance/research_protocol.md`
6. `data/draw_manifest.json`
7. `core/heps_architecture.md`
8. `core/expert_registry.yaml`
9. `knowledge/open_questions.md`
10. `experiments/registry.csv`
11. latest relevant session handoff, currently `knowledge/SESSION_HANDOFF_MAIN_HEPS_2026-09-02.md`
12. for coalition/portfolio work, `knowledge/ASSEMBLY_EVOLUTION_HANDOFF_2026-09-02.md` and `experiments/E0022/`
13. only the experiment/cycle/review files directly relevant to the task.

Use `data/draw_history.jsonl` as the canonical Main ledger.

### Token-efficiency rule

Do **not** recursively ingest every historical experiment, `workspace/contributions/`, or every review. Use the registries and deprecation map to identify relevant evidence first. Read legacy material only when reproducing, auditing, or tracing provenance.

For HLR/VVD/gap/null work, `experiments/E0001/` and `knowledge/STRUCTURAL_NULL_GAP_SPACE_RESEARCH_GUIDE_2026-08-06.md` remain key context.

For outside AI/human/paper/code proposals, `governance/external_contribution_protocol.md` is mandatory.

## 3. Current mathematical doctrine — non-negotiable interpretation

The binding summary is in `governance/current_method_doctrine.md`. In particular:

- **Joint distribution first, compression second.**
- `MAIN_HLR_SLOT`, `MAIN_VVD_DELTA`, terminal digit, and exact target coordinate are deterministic views of one sorted-slot transition and belong to one information family.
- Do not multiply or vote those views as independent evidence.
- Prefer one regularized signed-displacement representation and exact legal-line normalization when feasible.
- Proper-score improvement of the underlying probability field is a primary promotion gate; raw K13/K20 recall alone is insufficient.
- Exact-slot probability and anywhere-coordinate probability are distinct artifacts.
- A coordinate strongly supported in an adjacent slot may be tested for fixed-K preservation; no union/K-expansion credit.
- Structural nulls are controls, not predictive experts.

If an old experiment contradicts these rules, consult `governance/methodology_deprecations.md` before reuse.

## 4. Autonomous role selection

Agents may choose the research role most likely to improve, reproduce, falsify, simplify, challenge, or synthesize HEPS, including:

- hypothesis explorer;
- quantitative tester;
- independent reproducer;
- adversarial statistician;
- redundancy auditor;
- state-space modeller;
- architecture challenger;
- implementation engineer;
- Physics-of-Failure analyst;
- synthesis architect;
- meta-research auditor.

Declare substantive research intent using `collaboration/templates/agent_intent.yaml` or equivalent experiment fields.

Do not overwrite another agent's experiment package. Add a reproduction, critique, challenger, or successor experiment.

## 5. Evidence classifications and architecture status

Use exactly one evidence classification:

- `BREAKTHROUGH`
- `PROVISIONAL_SIGNAL`
- `INSUFFICIENT_EVIDENCE`
- `REJECT`

Architecture status is separate:

- `production`
- `shadow`
- `experimental`
- `archived`

A component may be mathematically useful while having no predictive authority. A failed architecture may contain a reusable objective/operator; preserve component-level decisions.

## 6. Experimental protocol

Before evaluation declare:

- hypothesis and target;
- data/training window;
- validation/prospective window;
- feature definitions;
- baselines;
- metrics;
- hyperparameter selection rule;
- falsification rule;
- multiple-testing/search exposure;
- authority requested.

Strict walk-forward order:

1. use only information before target `t`;
2. compute parameters/features/scores;
3. freeze output;
4. reveal `t`;
5. score;
6. update only for `t+1`.

A sequential replay designed after outcomes are known is still discovery/post-hoc evidence.

## 7. Nulls and dependency controls

Use exact structural controls where available:

- `NULL_ORDER_STATISTIC_SLOT`
- `NULL_HLR_STRUCTURAL`
- `NULL_VVD_STRUCTURAL`
- `NULL_HLR_JOINT_243`
- `NULL_GAP_DM`

Global Main IID inclusion is exactly `5/50=0.1` for each coordinate; the pure structural global field cannot rank a predictive K basket.

Sorted slots are dependent. Do not multiply per-slot structural marginals and call the product an exact joint null.

Before expert agreement increases confidence, control structural geometry, simple frequency/recency where relevant, residual dependence, and incremental proper-score value. Functionally derived features count as one information family.

## 8. Stage architecture

HEPS remains staged:

1. **Slot Forecast**
2. **Candidate Funnel**
3. **Coalition Assembly**
4. **Morphology**
5. **Winner-Float Ranking**
6. **Portfolio Optimization**
7. **PowerBall Matrix**

An expert's forecast and authority are separate. External operators should be tested in the stage implied by their information content, not automatically in the contributor's proposed stage.

Johnson covering is assembly/portfolio geometry only. It has zero candidate-discovery authority.

For K13 assembly, enumerate all `C(13,5)=1,287` legal lines before ranking. Do not hard-prune the winning line through morphology or generation shortcuts. For discrete coalition scores with ties, use average midrank or an explicitly justified tie-aware rule; E0022 showed best-in-tie scoring can materially inflate apparent lift.

## 9. Main candidate-acquisition priority

K=13 remains the preferred primary acquisition research target, but it is falsifiable and must be compared with matched K controls.

A candidate model should be evaluated in this order:

1. full-support proper score vs structural/simple controls;
2. fixed-K winner-coordinate survival;
3. catastrophic-exclusion rate;
4. complete-line containment probability;
5. downstream assembly/ranking only after acquisition is scored.

Do not promote an optimized basket if its underlying probability field is worse than flat/structural control.

## 10. Current lessons from 2026-09-01 Main draw

Verified result: `14,16,31,34,40 | PB4`.

Previous draw: `19,22,24,25,47 | PB11`.

Realized HLR: `LLHHL`.

The frozen BARP modal HLR was also `LLHHL`, an exact 5/5 directional hit. This is positive one-target prospective evidence, not a promotion.

The first failure remained candidate acquisition/compression:

- E0019 K13 retained 31 and 34;
- diagnostic K20 additionally retained 40;
- coordinate 14 had strong pre-draw adjacent-slot evidence;
- coordinate 16 had strong S1/S2 evidence;
- strict slot provenance lost useful anywhere-coordinate information.

Future work may reward this by bounded scenario allocation and fixed-K adjacent-slot preservation, never by post-hoc parameter tuning.

## 11. Draw-method and stationarity integrity

`game_format`, `draw_method`, and `machine_name` are separate concepts.

Never infer draw method/machine from a date or outcome pattern. Physical/mechanical hypotheses must disclose machine/method mixing. A regime boundary requires external evidence, not outcome-optimized split selection.

Machine/ball-set non-exchangeability is a high-value future research question only when metadata are prospectively knowable and models are strongly regularized.

## 12. PowerBall integrity

PowerBall is a separate 1..16 field.

Sparse conditional transitions require strong shrinkage and prospective comparison against uniform plus a preregistered unconditional shrunk baseline. HLR/VVD/terminal/exact-state views of the same PB transition are not independent votes.

Main-number success never transfers authority automatically to PB.

## 13. Per-draw cycle integrity

Each target should have `cycles/YYYY-MM-DD/`.

Pre-draw artifacts become immutable once frozen.

Post-draw work may add:

- verified result/provenance;
- scoring;
- expert attribution;
- Physics of Failure;
- leave-one-expert-out or stage-isolation diagnostics;
- research-priority updates.

Never regenerate the old slate after outcome reveal.

## 14. Three-speed self-improvement

**Fast — state:** frozen formulas update sufficient statistics after each validated draw.

**Medium — parameters:** update only through predeclared algorithms, never because one draw hit/missed.

**Slow — architecture:** new experts, changed semantics, changed authority, or removal requires evidence/review and a successor/deprecation record.

## 15. External contributions

A flawed external architecture can contain a valuable component. Decompose contributions into operators, reproduce claimed results on canonical data, stage-remap when mathematically appropriate, record search-degree exposure, and freeze useful derivatives prospectively.

External performance claims receive zero HEPS predictive credit until reproduced under canonical data/governance.

## 16. Nomenclature

`governance/nomenclature.md` is binding.

Key distinctions:

- `MAIN_HLR_SLOT` = direction view of sorted-slot transition.
- `MAIN_VVD_DELTA` = absolute magnitude view of the same transition.
- `MAIN_SIGNED_SLOT_TRANSITION` = canonical signed displacement representation for new research.
- `MAIN_GAP_VECTOR` = six-component sorted-line gap composition.
- structural-null identifiers are controls, not learned experts.
- legacy VVD-volume / whole-field high-low / ink-mass concepts remain rejected historical identifiers.

## 17. Validation

Before prediction/backtest/ledger changes, run available validation tools when practical:

```bash
python scripts/validate_draws.py data/draw_history.jsonl
python scripts/sync_manifest.py --check
python scripts/check_stationarity.py
python scripts/simulate_null_model.py --trials 100000 --seed 20260704
```

For relevant slot/null research also run `scripts/structural_null.py` for the previous draw and declared basket sizes.

For E0022 assembly work run `pytest -q tests/test_e0022_assembly_evolution.py` and reproduce `scripts/oracle_k13_assembly_evolution.py` before making new lift claims.

Main numbers are sorted order statistics, not physical extraction order.

## 18. Final obligation

Leave HEPS more auditable and less misleading than you found it.

Useful contributions include falsification, deprecation, reproduction, stronger nulls, cleaner dependency modelling, better calibration, failure localization, data/provenance repair, or a demonstrably independent information source. More complexity is not itself progress.