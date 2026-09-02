# Hybrid Expert Prediction System

HEPS is a private, AI-driven, multi-agent, paper-trading research system for South African PowerBall.

The repository is shared scientific memory: hypotheses, frozen predictions, failures, reproductions, deprecations, and current architecture. Historical research is preserved for auditability, but **old files are not automatically current advice**.

## Core principle

Research is promoted through evidence:

`hypothesis -> experiment -> reproduction -> red-team -> synthesis -> promotion/deprecation -> active architecture`

Every target draw uses immutable pre-draw artifacts followed by post-draw Physics-of-Failure analysis.

## Mandatory AI entry point

Every AI model starts with `AGENTS.md`.

Current read order:

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
12. only task-relevant experiment/cycle/review artifacts.

Do not recursively ingest all legacy contributions before consulting the registries and deprecation map.

## Current architecture

**HEPS v35.0 — Joint-Distribution-First Staged Mixture-of-Experts**

```text
Exact Structural Controls
        -> Transition / Slot Forecast
        -> Candidate Funnel
        -> Coalition Assembly
        -> Combination Morphology
        -> Winner-Float Ranking
        -> Portfolio Optimization

Separate Matrix B:
        -> PowerBall 1-16
```

The current mathematical doctrine is:

> **Joint distribution first, compression second.**

For a sorted slot, HLR, VVD, terminal digit and exact target coordinate are deterministic views of one signed transition. They may be scored for interpretation, but may not be multiplied or counted as independent expert evidence.

New Main acquisition research should prefer one regularized signed-displacement field, exact legal-line normalization where feasible, proper-score evaluation, then fixed-K compression.

See `governance/current_method_doctrine.md`.

## Important 2026-09-01 lesson

Verified Main result:

`14,16,31,34,40 | PB4`

Previous:

`19,22,24,25,47 | PB11`

Realized HLR was `LLHHL`, exactly matching the frozen BARP modal HLR prediction `LLHHL`.

This is positive one-target prospective evidence, not a promotion.

The first failure remained candidate compression:

- E0019 K13 retained only 31 and 34;
- wider diagnostic exposure additionally retained 40;
- useful 14/16 evidence was partly lost because it was assigned to adjacent sorted slots.

This motivated the fixed-K adjacent-slot preservation challenger and E0021 corrected signed-displacement architecture.

## Repository structure

```text
AGENTS.md                     Current AI constitution/read order
governance/                   Current doctrine, deprecations, research rules
data/                         Canonical draw ledger and manifest
core/                         Active architecture and expert metadata
experiments/                  Self-contained hypothesis/review packages
knowledge/                    Claims, failures, open questions, handoffs
cycles/                       Immutable pre/post-draw cycle artifacts
collaboration/                Agent intent/reviews/synthesis
workspace/                    Historical/raw contributions; warning-first reading
scripts/                      Validation/scoring/research utilities
tests/                        Mathematical/no-leakage tests
archive/                      Explicit archives
```

## Evidence states

Every material claim uses exactly one:

- `BREAKTHROUGH`
- `PROVISIONAL_SIGNAL`
- `INSUFFICIENT_EVIDENCE`
- `REJECT`

Architecture status is separate:

- `production`
- `shadow`
- `experimental`
- `archived`

`production` means pipeline-available, not proven predictive edge.

## Current forward-use warnings

Consult `governance/methodology_deprecations.md` before copying formulas from old experiments.

In particular:

- E0019 HLR×VVD residual-product field is rejected for forward reuse; its complete-line containment objective is retained.
- E0020 terminal×HLR×VVD multiplicative acquisition chain is rejected; terminal diagnostics remain shadow-only.
- pure structural-null global mobility cannot select candidates because every Main coordinate has IID global inclusion probability 0.1.
- Johnson covering has zero candidate-discovery authority.
- original JOS-HDR exact-line density under the exact uniform gap null is rejected.
- E0016 Richardson geometric-mean message passing is heuristic, not exact joint inference.
- raw K recall without matched exposure is invalid evidence.
- one successful draw may not trigger parameter retuning or expert promotion.

## Data doctrine

- Canonical Main ledger: `data/draw_history.jsonl`
- Manifest: `data/draw_manifest.json`
- Current Main ledger through 2026-09-01 / draw id 27
- Game format: 5/50 + PowerBall 1/16
- `game_format`, `draw_method`, and `machine_name` are separate metadata concepts
- Slot1-Slot5 are sorted order statistics, not physical draw order
- Unknown method/machine must remain `unknown`; never infer from outcomes/date alone
- physical/machine hypotheses require provenance and strong controls

## Quick validation

```bash
python scripts/validate_draws.py data/draw_history.jsonl
python scripts/sync_manifest.py --check
python scripts/check_stationarity.py
python scripts/simulate_null_model.py --trials 100000 --seed 20260704
```

## Per-draw learning rule

Before the draw, freeze data state, expert formulas/authority, probability fields, K baskets, line rankings and paper-trading slate.

After the draw, score the frozen artifacts, trace winner survival, identify the first failure stage, update claim/failure registries, and learn only for the next target under preregistered rules.

Never regenerate historical predictions after outcome reveal.

## Legacy compatibility

`workspace/contributions/`, `workspace/reviews/`, and older outputs are preserved for provenance. They should not be mass-deleted, but they should not be treated as current doctrine.

See `workspace/contributions/README.md` for warning-first use.

## Safety frame

All HEPS prediction artifacts are `paper_trading_only`. Do not present them as guaranteed, financially reliable, or proof of a durable lottery edge without prospective, matched-exposure, multiplicity-aware evidence.