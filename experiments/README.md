# HEPS Experiment Packages

New structured research should live under `experiments/<experiment_id>/`.

Legacy research in `workspace/contributions/`, `workspace/reviews/`, and `outputs/research/` remains part of the evidence record and should not be deleted during migration.

## Package structure

```text
experiments/E####/
  hypothesis.md
  protocol.yaml
  results.json
  findings.md
  red_team/
    <reviewer>.md
  reproductions/
    <reproducer>.md or .json
  decision.md
```

## Required hypothesis fields

- experiment ID
- title
- originating agent/session if known
- self-selected role
- target architectural stage
- falsifiable hypothesis
- why the question matters
- relationship to existing claims/experts

## Required protocol fields

- dataset and cutoff rules
- discovery/training window
- untouched validation/prospective window
- feature definitions
- hyperparameters and how selected
- baselines
- metrics
- multiple-testing exposure
- falsification rule
- reproducibility instructions

## Results

Machine-readable results are preferred. Preserve raw denominators, target counts, and survivor-universe sizes.

## Reviews

Different models should add separate review files rather than rewriting the originating findings.

## Decision

Use one evidence classification:

- BREAKTHROUGH
- PROVISIONAL_SIGNAL
- INSUFFICIENT_EVIDENCE
- REJECT

Also state whether the expert remains experimental, moves to shadow, is promoted, or is archived.

## Registry

Add one row to `experiments/registry.csv` for discoverability. The registry is an index, not a substitute for the package.