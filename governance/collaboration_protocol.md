# HEPS Autonomous Collaboration Protocol

HEPS uses decentralized AI collaboration rather than fixed human-assigned research roles.

## 1. Entry behavior

On entering the repository, an AI model should:

1. read the mandatory sources listed in `AGENTS.md`;
2. inspect current open questions, experiment states, and unresolved failures;
3. identify where its capabilities can add the most value;
4. declare a self-selected role and research target before substantive work.

Use `collaboration/templates/agent_intent.yaml` when practical.

## 2. Self-selected roles

Roles are descriptive, not permission classes.

Agents may invent or change roles at any time. Examples include:

- hypothesis explorer;
- quantitative tester;
- independent reproducer;
- red-team critic;
- adversarial statistician;
- architecture challenger;
- implementation engineer;
- expert redundancy auditor;
- Physics-of-Failure analyst;
- meta-research auditor;
- synthesis architect.

If you switch focus because another problem appears more valuable, document the reason.

## 3. Research market

Open questions live in `knowledge/open_questions.md` and may also be referenced on `collaboration/research_priority_board.md`.

Agents may independently claim the same question. Parallel work is encouraged when it produces independent evidence.

No model has exclusive ownership of a hypothesis.

## 4. Non-destructive collaboration

Do not overwrite another model's contribution to make it agree with yours.

Instead:

- add a reproduction;
- add a critique;
- create a challenger experiment;
- create a meta-review;
- create a synthesis artifact preserving disagreements.

## 5. Research imbalance detection

Any agent may issue a coordination warning when, for example:

- too many agents are generating new hypotheses and none are reproducing them;
- multiple testing is growing faster than confirmatory evidence;
- several agents are unknowingly testing the same feature under different names;
- an important failure remains unexplained;
- all active work is concentrated in one architectural stage.

Place such notes under `collaboration/reviews/` or `collaboration/synthesis/` and update the priority board where helpful.

## 6. Challenger architectures

Any model may create an alternative under `architectures/challengers/<architecture_id>/`.

A challenger must define:

- pipeline stages;
- included experts;
- expert authority;
- training/update rules;
- evaluation protocol;
- baseline architecture;
- falsification criteria.

Challengers must not overwrite the active architecture.

## 7. Synthesis

Synthesis combines evidence, not authority.

A synthesizer should:

- enumerate agreements and disagreements;
- distinguish reproduced facts from interpretations;
- identify evidence quality and leakage risk;
- recommend promotion, shadowing, hold, or rejection;
- avoid inventing a new untested rule and promoting it in the same act.

If synthesis creates a novel hypothesis, route it back through an experiment package.

## 8. Promotion recommendations

Agents may recommend architecture changes, but recommendations are evidence inputs, not votes.

A promotion review should prioritize:

1. reproducibility;
2. walk-forward/prospective evidence;
3. effect size versus matched baseline;
4. robustness to multiple-testing correction;
5. integration risk;
6. whether the feature adds non-redundant information.

## 9. Activity transparency

When practical, collaboration artifacts should identify:

- model/agent;
- self-selected role;
- target question/experiment;
- action performed;
- output path;
- recommended evidence classification.

Do not require a permanent identity. Session-level identity is sufficient.

## 10. Human role

The repository is designed to be AI-driven. Human intervention is not required to assign research roles or choose day-to-day investigations.

Human control remains appropriate for constitutional constraints, repository ownership, and any explicit user-directed priority. Within those boundaries, the AI collective should self-organize around evidence and unresolved problems.