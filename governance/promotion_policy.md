# HEPS Architecture Promotion Policy

`core/heps_architecture.md` is the end of the research pipeline. It is not a scratchpad.

## 1. Promotion path

Normal path:

`proposal -> experiment -> reproduction -> red-team -> synthesis -> promotion decision -> active architecture`

Emergency direct edits are discouraged and must be explicitly justified and auditable.

## 2. Evidence and architecture states

Evidence states:

- `BREAKTHROUGH`
- `PROVISIONAL_SIGNAL`
- `INSUFFICIENT_EVIDENCE`
- `REJECT`

Architecture states:

- `production`
- `shadow`
- `experimental`
- `archived`

A promising signal may remain shadow-only. Evidence status never automatically grants production authority.

## 3. Minimum promotion questions

Before any expert or rule gains production authority, reviewers must answer:

1. Is the feature definition unambiguous and registered?
2. Does the result survive strict no-leakage testing?
3. Is there an appropriate random/simple/current baseline?
4. Was multiple-testing exposure recorded?
5. Has the result been independently reproduced where practical?
6. Does it add information beyond already active experts?
7. What authority is requested: score, exposure adjustment, veto, portfolio lane, or parameter update?
8. What is the rollback/falsification rule?
9. How will it be measured prospectively?

## 4. Authority ladder

Prefer the lowest authority needed to test a promising idea:

1. diagnostic only;
2. shadow score;
3. soft ranking weight;
4. exposure adjustment;
5. portfolio allocation;
6. candidate pruning;
7. hard elimination/veto.

Hard veto is the highest-risk authority and requires substantially stronger evidence than a soft score.

## 5. Weight changes

Do not change expert weights because one target succeeded or failed.

Weight learning must be either:

- governed by a frozen algorithm; or
- proposed from accumulated evidence and reviewed through this policy.

## 6. Challenger promotion

Whole challenger architectures may be compared against the active architecture on identical frozen targets. Promotion may merge only selected components if the evidence supports them independently.

## 7. Required decision artifact

A promotion decision should state:

- claim/experiment IDs;
- evidence classification;
- requested architecture state;
- accepted/rejected authority;
- baseline comparison;
- known failure modes;
- prospective falsification rule;
- exact core files changed.

## 8. Rejection and archiving

Rejected strategies remain in the historical record. Do not erase them: future agents need to know what was tested, why it failed, and whether a similarly named new concept is genuinely different.