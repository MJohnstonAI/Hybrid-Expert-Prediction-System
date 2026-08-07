# HEPS Agent Configuration — Compatibility Shim

`AGENTS.md` is now the single authoritative constitution for AI models and coding agents in HEPS.

This file is retained for backward compatibility with tools or prompts that still expect `configs/agent.md`.

## Required action

Before substantive HEPS work, read:

1. `AGENTS.md`
2. `governance/nomenclature.md`
3. `governance/research_protocol.md`
4. `governance/collaboration_protocol.md`
5. `core/heps_architecture.md`
6. `core/expert_registry.yaml`

If this file conflicts with `AGENTS.md`, the root `AGENTS.md` governs.

## Data anchors

- Canonical draw ledger: `data/draw_history.jsonl`
- Dataset manifest: `data/draw_manifest.json`
- Active game format: `powerball_50_16`
- Main field: five unique integers from 1-50
- PowerBall: one integer from 1-16
- `draw_method` and `machine_name` are separate from game format and must not be inferred from date alone
- Sorted Slot1-Slot5 values are order statistics, not physical draw order
- Prediction artifacts are paper-trading research only

## Architecture changes

Do not promote an unreviewed model idea directly into core doctrine. New structured research should use `experiments/`; legacy `workspace/contributions/` and `workspace/reviews/` remain valid historical evidence.

Promotion follows `governance/promotion_policy.md`.
