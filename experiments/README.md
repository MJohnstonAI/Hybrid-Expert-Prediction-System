# HEPS Experiment Packages

New structured research should live under `experiments/<experiment_id>/`.

Legacy research in `workspace/contributions/`, `workspace/reviews/`, and `outputs/research/` remains part of the evidence record and should not be deleted during migration.

When research originates from an outside AI/human/paper/code contribution, also follow `governance/external_contribution_protocol.md`.

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

For a derivative hypothesis extracted from an outside contribution, also record:

- source contribution path/artifact;
- mathematical operator extracted;
- what changed from the source proposal;
- original stage/authority proposed by the source;
- HEPS stage/authority being tested;
- whether the derivative was specified before or after exploratory replay.

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

For external-contribution championships or derivative experiments, multiple-testing exposure should include where relevant:

- operator variants;
- windows;
- thresholds;
- transformations;
- stage placements;
- graph/cluster formulations;
- random seeds;
- metrics inspected.

## Results

Machine-readable results are preferred. Preserve raw denominators, target counts, and survivor-universe sizes.

Stage-isolation diagnostics must be clearly labelled. In particular, an oracle candidate universe containing known target winners may be used only as a post-hoc diagnostic for coalition/ranking performance and provides zero candidate-acquisition credit.

## Reviews

Different models should add separate review files rather than rewriting the originating findings.

External contributions should preserve the original source artifact. Add audits, reproductions, decompositions, or derivative experiments rather than rewriting the source to fit HEPS.

## Decision

Use one evidence classification:

- BREAKTHROUGH
- PROVISIONAL_SIGNAL
- INSUFFICIENT_EVIDENCE
- REJECT

Also state whether the expert remains experimental, moves to shadow, is promoted, or is archived.

When an outside contribution contains materially different components, classify the components separately rather than assigning one blanket evidence label to the entire source document.

## Registry

Add one row to `experiments/registry.csv` for discoverability. The registry is an index, not a substitute for the package.
