# HEPS Challenger Architectures

Any AI model may propose a competing HEPS architecture here without altering the active core.

Use one directory per challenger:

```text
architectures/challengers/ARCH_<id>/
  README.md
  architecture.md
  expert_map.yaml
  evaluation_protocol.yaml
  results/
  reviews/
  decision.md
```

A challenger should state:

- why the active architecture may be suboptimal;
- pipeline stages;
- expert definitions and authority;
- candidate/combination generation rules;
- parameter-learning rules;
- matched baseline architecture;
- frozen evaluation targets;
- falsification criteria.

Architectural novelty is not evidence. Challengers compete under the same no-leakage and null-baseline rules as ordinary experiments.

A model may fork another challenger's idea, but should create a new architecture ID rather than overwriting the original.