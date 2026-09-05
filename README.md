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
11. latest relevant handoff, currently `knowledge/HEPS_V35_3_CROSS_SESSION_PREDICTION_HANDOFF_2026-09-04.md`
12. for pattern-triage work, `knowledge/PATTERN_CONSTRAINT_K13_HANDOFF_2026-09-04.md`, `experiments/E0028/`, and `experiments/E0029/`
13. only task-relevant experiment/cycle/review artifacts.

Do not recursively ingest all legacy contributions before consulting the registries and deprecation map.

## Current architecture

**HEPS v35.3 — Joint-Distribution-First Staged Mixture-of-Experts with Candidate-Frozen Pattern Triage**

```text
Exact Structural Controls
        -> Transition / Slot Forecast
        -> Scenario-Constrained Slot-Routed Candidate Funnel
        -> Freeze K13
        -> Enumerate all C(13,5)=1,287 lines
        -> Candidate-Frozen Pattern Constraint Triage (E0029 shadow)
        -> Coalition / Winner-Float Ranking
        -> Portfolio Optimization

Separate Matrix B:
        -> PowerBall 1-16
```

The current mathematical doctrine is:

> **Joint distribution first, compression second.**

For a sorted slot, HLR, VVD, terminal digit and exact target coordinate are deterministic views of one signed transition. They may be scored for interpretation, but may not be multiplied or counted as independent expert evidence.

Main acquisition research should preserve **candidate + admissible slot(s) + scenario probability**, use coherent legal-line normalization where feasible, score the full probability field first, and only then compress at fixed K.

Pattern recognition from E0028/E0029 acts primarily **after K13 freeze** and currently has shadow authority only.

See `governance/current_method_doctrine.md` and `governance/methodology_deprecations.md`.

## Latest Main cycle lesson — 2026-09-04

Verified Main result:

`4,7,27,38,50 | PB10`

Previous:

`14,16,31,34,40 | PB4`

Realized signed slot transition:

`[-10,-9,-4,+4,+10]`

Realized HLR:

`LLLHH`

The frozen slotwise BARP modal HLR was `LHLHH`, so four of five directional signs were correct. The official K13 retained only `50`, making **candidate acquisition the first binding failure stage**. E0029/E0013/Johnson cannot receive blame or credit for the exact winner line because four winning coordinates were already absent upstream.

The superseded E0026-R K13 retained `38` and `50`, with both realized in their primary routed slots S4 and S5. This remains `INSUFFICIENT_EVIDENCE`, but it supports continued slot-routed acquisition research rather than unrestricted anywhere-coordinate collapse.

The frozen E0028 LDSAD diagnostic landed at `11`, inside its pre-draw `11..13` discovery band on its first fresh target. This is one prospective shadow success only and does not confer hard-pruning authority.

## Repository structure

```text
AGENTS.md                     Current AI constitution/read order
governance/                   Current doctrine, deprecations, research rules
data/                         Canonical active-era draw ledgers and manifests
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
- unrestricted anywhere-coordinate probability may not erase E0026 slot/scenario provenance.
- pure structural-null global mobility cannot select candidates because every Main coordinate has IID global inclusion probability 0.1.
- E0029 Pattern-OR has no production hard-pruning authority yet.
- Johnson covering has zero candidate-discovery authority.
- original JOS-HDR exact-line density under the exact uniform gap null is rejected.
- E0016 Richardson geometric-mean message passing is heuristic, not exact joint inference.
- raw K recall without matched exposure is invalid evidence.
- one successful draw may not trigger parameter retuning or expert promotion.

## Data doctrine

- Canonical Main ledger: `data/draw_history.jsonl`
- Main manifest: `data/draw_manifest.json`
- Canonical XTRA ledger: `data/powerball_xtra_history.jsonl`
- XTRA manifest: `data/powerball_xtra_manifest.json`
- **Active Main and XTRA winning-draw history begins on 2026-06-02.**
- **No pre-June 2026 winning rows may enter either active canonical ledger or active fitted state.**
- Current Main ledger: 28 rows through `2026-09-04`
- Current XTRA ledger: 28 rows through `2026-09-04`
- Game format: 5/50 + PowerBall 1/16
- Main and XTRA remain independently fitted lanes.
- `game_format`, `draw_method`, and `machine_name` are separate metadata concepts.
- Slot1-Slot5 are sorted order statistics, not physical draw order.
- Unknown method/machine must remain `unknown`; never infer them from outcomes/date alone.
- Physical/machine hypotheses require provenance and strong controls.
- Legacy Excel/PRNG-era data have no active prediction authority.

## Quick validation

```bash
python scripts/validate_draws.py data/draw_history.jsonl
python scripts/sync_manifest.py --check
python scripts/validate_active_data.py
python scripts/check_stationarity.py
python scripts/simulate_null_model.py --trials 100000 --seed 20260704
python -m unittest discover -s tests -v
```

## Per-draw learning rule

Before the draw, freeze data state, expert formulas/authority, probability fields, K baskets, line rankings and paper-trading slate.

After the draw, score the frozen artifacts, trace winner survival, identify the first failure stage, update claim/failure registries, and learn only for the next target under preregistered rules.

Never regenerate historical predictions after outcome reveal.

A pre-draw frozen artifact may only be superseded by a new version **before result knowledge**, under `governance/pre_draw_supersession_policy.md`. Earlier versions remain immutable evidence.

## Legacy compatibility

`workspace/contributions/`, `workspace/reviews/`, and older outputs are preserved for provenance. They should not be mass-deleted, but they should not be treated as current doctrine.

See `workspace/contributions/README.md` for warning-first use.

## Safety frame

All HEPS prediction artifacts are `paper_trading_only`. Do not present them as guaranteed, financially reliable, or proof of a durable lottery edge without prospective, matched-exposure, multiplicity-aware evidence.
