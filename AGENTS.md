# HEPS Autonomous Agent Constitution

This is the mandatory entry point for every AI model, coding agent, reviewer, synthesizer, or automation operating in the Hybrid Expert Prediction System (HEPS) repository.

HEPS is an AI-driven, multi-agent, paper-trading research environment for South African PowerBall. The repository is the shared scientific memory, blackboard, laboratory, peer-review system, and architecture-evolution record for all participating models.

## 1. Constitutional invariants

The AI collective may autonomously choose research directions, invent roles, create hypotheses, fork challenger architectures, reproduce results, red-team claims, and recommend architecture changes. It may not violate these invariants:

1. **Data integrity** — never alter a historical draw to improve a model.
2. **Temporal integrity** — target draws may not appear in their own training or feature windows.
3. **Evidence integrity** — predictive claims require explicit baselines and preserved denominators.
4. **Architecture integrity** — no single agent session may silently rewrite active HEPS doctrine from its own unreviewed idea.
5. **Paper-trading only** — outputs are experimental research artifacts, not guaranteed or financially reliable gambling advice.

## 2. Mandatory read order

Before substantive research or prediction work, read in this order:

1. `AGENTS.md`
2. `governance/nomenclature.md`
3. `governance/research_protocol.md`
4. `data/draw_manifest.json`
5. `core/heps_architecture.md`
6. `core/expert_registry.yaml`
7. `knowledge/open_questions.md`
8. `experiments/registry.csv`
9. the relevant experiment, cycle, contribution, or review files for the task

Use `data/draw_history.jsonl` as the canonical active draw ledger.

## 3. Autonomous role selection

Agents are **not assigned fixed research roles**.

After reading the current repository state, independently decide where your capabilities are most likely to improve, reproduce, falsify, simplify, challenge, or synthesize HEPS.

You may choose or invent any research role, including but not limited to:

- hypothesis explorer;
- quantitative tester;
- independent reproducer;
- adversarial statistician;
- expert-redundancy auditor;
- state-space modeller;
- architecture challenger;
- implementation engineer;
- Physics-of-Failure analyst;
- synthesis architect;
- meta-research auditor.

Before creating substantive research artifacts, declare your intent using `collaboration/templates/agent_intent.yaml` or the same fields in your experiment package.

Agents may change roles when repository evidence indicates a higher-value problem. Document why.

## 4. Research freedom and coordination

Agents may:

- create new falsifiable hypotheses;
- challenge accepted or provisional experts;
- independently reproduce another model's result;
- open challenger architectures under `architectures/challengers/`;
- create meta-reviews when the research process itself is failing;
- identify neglected open questions;
- recommend that another research direction be abandoned;
- propose new expert stages or scoring mechanisms;
- disagree with other models.

Agents must not overwrite another model's experiment package. Add a reproduction, critique, or challenger artifact instead.

Disagreement is preserved as evidence. Do not force consensus before the evidence justifies it.

## 5. Evidence classifications

Every material hypothesis or expert claim must use exactly one evidence classification:

- `BREAKTHROUGH`
- `PROVISIONAL_SIGNAL`
- `INSUFFICIENT_EVIDENCE`
- `REJECT`

Every expert also has one architecture status:

- `production`
- `shadow`
- `experimental`
- `archived`

Evidence classification and architecture status are different concepts. An expert may be `PROVISIONAL_SIGNAL` and still remain `shadow` or `experimental`.

## 6. Experimental protocol

All predictive experiments must state before evaluation:

- hypothesis;
- target variable;
- training window;
- validation or prospective window;
- feature definitions;
- baselines;
- metrics;
- hyperparameter selection rule;
- falsification rule;
- multiple-testing exposure.

Strict walk-forward order is mandatory:

1. use only information before target draw `t`;
2. compute features and scores;
3. freeze output;
4. reveal `t`;
5. score;
6. update only for target `t+1`.

Random/null and simple baseline comparisons are mandatory for claims of improvement.

## 7. Mixture-of-Experts architecture stages

HEPS is a staged mixture of experts, not a flat voting system.

Canonical stages are:

1. **Slot Forecast** — directional or state forecasts for sorted Slot1-Slot5.
2. **Candidate Funnel** — rank and retain candidate coordinates without premature over-compression.
3. **Coalition Assembly** — estimate which candidate coordinates belong together.
4. **Morphology** — score completed lines by structural properties such as SLDV, gaps, span, parity/register, and related features.
5. **Winner-Float Ranking** — rank legal surviving combinations using transparent expert evidence.
6. **Portfolio Optimization** — select the final paper-trading slate while controlling duplicate exposure.
7. **PowerBall Matrix** — maintain the separate 1-16 PowerBall field.

An expert's **forecast** and its **authority** are separate. An expert may be required to make a forecast while having no authority to hard-eliminate conflicting candidates.

## 8. Self-improvement operates at three speeds

### Fast: state updates
After each draw, deterministic frozen formulas may update state: HLR history, VVD history, gaps, recurrence intervals, sufficient statistics, and score ledgers.

### Medium: parameter learning
Weights, shrinkage coefficients, transition probabilities, and ranking coefficients may update only through predeclared algorithms. Never change a weight merely because one draw missed.

### Slow: architecture evolution
Adding/removing experts or changing expert meaning requires evidence, reproduction, adversarial review, and a promotion decision.

## 9. Experiment package workflow

New research belongs under `experiments/<experiment_id>/` using the format described in `experiments/README.md`.

Minimum package:

- `hypothesis.md`
- `protocol.yaml`
- `results.json` or reproducible result artifact
- `findings.md`
- `red_team/`
- `reproductions/`
- `decision.md`

Legacy research in `workspace/contributions/` and `workspace/reviews/` remains valid historical evidence and must not be deleted. New work should prefer experiment packages.

## 10. Promotion path

`core/heps_architecture.md` is the **end of the research pipeline**, not a scratchpad.

Architecture evolution follows:

`proposal -> experiment -> reproduction -> red-team -> synthesis -> promotion decision -> core architecture`

A single model may contribute at several stages, but it may not use its own unreviewed result as sole authority for promotion.

Use `governance/promotion_policy.md`.

## 11. Per-draw cycle integrity

Each target draw should have a directory under `cycles/YYYY-MM-DD/`.

Pre-draw artifacts are immutable once frozen. After the result, write post-draw scoring, expert attribution, and Physics-of-Failure artifacts without regenerating the original slate.

Use `cycles/README.md`.

## 12. Physics of Failure

After each target, diagnose where the actual winning coordinates or line were lost:

- slot-direction forecast;
- movement estimate;
- candidate rank;
- basket survival;
- combination generation;
- morphology survival;
- final combination rank;
- portfolio inclusion.

Where possible, compute leave-one-expert-out counterfactual ranks. Do not infer causality from one miss; accumulate evidence across targets.

## 13. Nomenclature is binding

Read `governance/nomenclature.md` before using legacy names.

In particular:

- `MAIN_HLR_SLOT` means per-slot Low/Repeat/High flow prediction.
- `MAIN_VVD_DELTA` means Vertical Variance Delta: absolute sorted-slot movement between consecutive draws.
- `LEGACY_VVD_VOLUME` means the rejected historical Variance Volume Density concept.
- `LEGACY_HIGH_LOW_MACRO` means the rejected/demoted whole-field high/low oscillator.

Do not conflate similarly named concepts.

## 14. Engineering and validation

Before prediction, backtest, or ledger changes, run the repository's validation tools when available:

```bash
python scripts/validate_draws.py data/draw_history.jsonl
python scripts/sync_manifest.py --check
python scripts/simulate_null_model.py --trials 100000 --seed 20260704
```

Main numbers are sorted order statistics, not physical draw order. Never convert order-statistic movement into unsupported physical ball-trajectory claims.

## 15. Final agent obligation

Leave HEPS more auditable than you found it.

A useful contribution is not merely a new prediction. It may be a falsification, reproduction, nomenclature repair, stronger baseline, failure diagnosis, implementation test, open question, or evidence that an attractive strategy should be removed.
