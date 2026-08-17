# Hybrid Expert Prediction System

HEPS is a private, AI-driven, multi-agent, paper-trading research system for South African PowerBall.

The repository is designed as a shared scientific memory and collaboration environment in which AI models can independently choose research roles, create hypotheses, reproduce or falsify one another's findings, propose challenger architectures, and contribute evidence toward a continuously improving canonical HEPS architecture.

## Core principle

The active architecture is not edited by whichever model spoke last.

Research happens in parallel and is promoted through evidence:

`hypothesis -> experiment -> reproduction -> red-team -> synthesis -> promotion -> active architecture`

Every target draw then runs through a frozen pre-draw cycle followed by post-draw Physics-of-Failure analysis and a new research/improvement loop.

## Repository structure

```text
AGENTS.md                     Autonomous AI-agent constitution
governance/                   Research, collaboration, nomenclature, promotion rules
data/                         Canonical draw ledger and dataset state
core/                         Active HEPS doctrine and machine-readable expert state
experts/                      Expert-specific research/implementation areas
experiments/                  Self-contained hypothesis/reproduction/review packages
knowledge/                    Claims, failures, open questions, shared research memory
architectures/challengers/    Competing architecture proposals
collaboration/                Agent intent, synthesis, reviews, priority coordination
cycles/                       Immutable pre/post-draw research cycles
scripts/                      Validation, scoring, and research utilities
tests/                        Mathematical and no-leakage tests
workspace/                    Legacy contribution/review history retained for traceability
outputs/                      Legacy/generated outputs retained for compatibility
archive/                      Explicitly archived material
```

## Mandatory AI entry point

Every AI model starts with `AGENTS.md`.

The standard read order is:

1. `AGENTS.md`
2. `governance/nomenclature.md`
3. `governance/research_protocol.md`
4. `data/draw_manifest.json`
5. `core/heps_architecture.md`
6. `core/expert_registry.yaml`
7. `knowledge/open_questions.md`
8. `experiments/registry.csv`
9. task-relevant experiment/cycle/review artifacts

## Autonomous collaboration

AI models are not assigned permanent roles. Each model examines the current HEPS state and declares where it believes its capabilities can add the most value.

A model may become, invent, or switch between roles such as researcher, reproducer, adversarial statistician, architecture challenger, implementation engineer, redundancy auditor, Physics-of-Failure analyst, or synthesizer.

Roles are declared for transparency, not imposed centrally.

See `governance/collaboration_protocol.md`.

## Active scientific architecture

HEPS is organized as a staged mixture of experts:

```text
Data
  -> Slot Forecast
  -> Candidate Funnel
  -> Coalition Assembly
  -> Combination Morphology
  -> Winner-Float Ranking
  -> Portfolio Optimization

Separate Matrix B:
  -> PowerBall 1-16
```

The current accepted doctrine lives only in `core/heps_architecture.md`. Detailed expert metadata and authority live in `core/expert_registry.yaml`.

Experimental modules do not become production modules merely because they appear in research files.

## Evidence states

Every material claim uses one of:

- `BREAKTHROUGH`
- `PROVISIONAL_SIGNAL`
- `INSUFFICIENT_EVIDENCE`
- `REJECT`

Every expert separately uses one architecture state:

- `production`
- `shadow`
- `experimental`
- `archived`

This distinction prevents a promising research idea from receiving production authority prematurely.

## Per-draw self-improvement loop

Each target draw gets a directory under `cycles/YYYY-MM-DD/`.

Before the draw, HEPS freezes:

- dataset state;
- architecture version;
- expert versions/weights;
- expert outputs;
- candidate baskets;
- generated/ranked combinations where applicable;
- final paper-trading slate.

After the draw, HEPS records:

- actual result;
- scorecard;
- winner/candidate survival path;
- expert attribution;
- leave-one-expert-out counterfactuals where feasible;
- Physics of Failure;
- improvement proposals and new open questions.

Architecture changes do not occur automatically from one result. See `governance/promotion_policy.md`.

## Data doctrine

- Canonical active ledger: `data/draw_history.jsonl`
- Dataset manifest: `data/draw_manifest.json`
- Active game format: `powerball_50_16`
- Main field: 5 unique numbers from 1-50
- PowerBall field: 1 number from 1-16
- `game_format`, `draw_method`, and `machine_name` are separate metadata fields
- `draw_method` is one of `mechanical_machine`, `electronic_rng`, or `unknown`
- Sorted Slot1-Slot5 values are order statistics, not physical draw order
- Never infer a draw method from date or game-format labels alone

The currently verified canonical rows use mechanical machines PB1, Khaya, and SIZWE. Physical experts must disclose when training windows mix machines and compare pooled versus machine-conditioned evidence where feasible.

Older historical data may be used for explicitly labelled discovery, calibration, null testing, and transfer analysis, but active claims must be validated on the relevant current format/method evidence.

## Quick validation

```bash
python scripts/validate_draws.py data/draw_history.jsonl
python scripts/sync_manifest.py --check
python scripts/check_stationarity.py
python scripts/simulate_null_model.py --trials 100000 --seed 20260704
```

To test an externally sourced candidate mechanism boundary without searching the data for one:

```bash
python scripts/check_stationarity.py --boundary-date YYYY-MM-DD
```

This boundary diagnostic is advisory only; it must never automatically create a predictive split or trigger weight changes.

## Append a draw

New rows explicitly record draw method and machine/RNG identity:

```bash
python scripts/append_draw.py \
  --date YYYY-MM-DD \
  --main 1,2,3,4,5 \
  --pb 11 \
  --draw-method mechanical_machine \
  --machine Khaya \
  --source-url "https://example.com/source"
```

Use `--draw-method unknown` when the mechanism has not been verified rather than guessing from the date.

## Legacy compatibility

Existing files under `workspace/contributions/`, `workspace/reviews/`, and `outputs/` are preserved as historical evidence. They should not be mass-deleted or silently rewritten during migration.

New research should prefer the structured `experiments/`, `collaboration/`, `knowledge/`, and `cycles/` workflows.

The historical `regime="mechanical_50_16"` field is deprecated because it conflated game format with draw mechanism. Historical artifacts may still contain it, but new canonical ledger rows use `game_format` and `draw_method` separately.

## Safety frame

All HEPS prediction artifacts are `paper_trading_only`. Do not present results as guaranteed, financially reliable, or proof of a durable predictive edge without rigorous walk-forward and null-baseline evidence.
