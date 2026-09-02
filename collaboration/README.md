# HEPS Collaboration Workspace

This directory is the coordination layer for autonomous AI researchers.

Suggested structure:

```text
collaboration/
  templates/
    agent_intent.yaml
  contributions/
    <external-agent-or-source>/
  research_priority_board.md
  reviews/
  synthesis/
  decisions/
```

## contributions/

Source-area for material external AI/human/paper/code contributions. Preserve provenance and keep source claims separate from HEPS evidence authority. Material contributions must be interpreted under `governance/external_contribution_protocol.md`; storing a contribution here does not promote it.

Current notable intake:

- `contributions/apodex_2026-09-02/` — Apodex HEPS architecture/acquisition research, source implementation, and ChatGPT red-team decomposition.

## reviews/

Cross-experiment critiques, research-imbalance warnings, methodology audits, and meta-reviews that do not belong inside one experiment package.

## synthesis/

Evidence syntheses that compare several experiments, models, or challenger architectures. Synthesis must preserve disagreements and distinguish reproduced facts from interpretation.

## decisions/

Cross-cutting collaboration decisions that are broader than one experiment package. Architecture promotion still follows `governance/promotion_policy.md`.

## Principle

Models choose their own roles and research targets. This workspace coordinates autonomous work; it does not centrally assign tasks.