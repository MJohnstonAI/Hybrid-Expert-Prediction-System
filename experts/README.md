# HEPS Expert Workspaces

This directory is for expert-specific implementation notes, tests, calibration artifacts, and research links.

The authoritative status/authority of every expert lives in `core/expert_registry.yaml`.

Recommended stage folders:

```text
experts/
  slot_forecast/
  candidate_funnel/
  coalition_assembly/
  morphology/
  winner_float_ranking/
  portfolio_optimization/
  powerball_matrix/
```

Do not infer that a directory's existence means the expert is production-approved.

Each expert workspace should identify:

- canonical expert ID;
- mathematical definition;
- required inputs;
- outputs;
- dependency experts;
- authority level;
- relevant experiment IDs;
- known failure modes;
- tests/no-leakage checks;
- current evidence classification.

Novel expert ideas should begin as experiments. Create an expert workspace only when the definition is stable enough to be shared across models.