# HEPS Architecture Promotion Policy

`core/heps_architecture.md` is the end of the research pipeline. It is not a scratchpad.

## 1. Promotion path

Normal path:

`proposal -> experiment -> reproduction -> red-team -> synthesis -> promotion decision -> active architecture`

For outside AI/human/paper/code contributions, the preferred path is:

`external contribution -> decomposition -> exploratory championship -> derivative hypothesis -> prospective shadow -> reproduction -> red-team -> promotion decision -> active architecture`

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

Evidence status should attach to the specific claim or component being evaluated. An external architecture may be rejected while an extracted component remains `PROVISIONAL_SIGNAL`.

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
10. If the idea came from an external contribution, was the component tested independently of the source's full architecture and claimed authority?
11. Was plausible stage-remapping considered when the mathematics naturally belonged elsewhere?
12. If the surviving formulation was found after testing variants, has it accumulated fresh prospective evidence after that search?

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

A derivative component extracted from an external contribution normally begins at diagnostic or shadow-score authority even if the external source requested pruning or veto authority.

## 5. Weight changes

Do not change expert weights because one target succeeded or failed.

Weight learning must be either:

- governed by a frozen algorithm; or
- proposed from accumulated evidence and reviewed through this policy.

## 6. Challenger promotion

Whole challenger architectures may be compared against the active architecture on identical frozen targets. Promotion may merge only selected components if the evidence supports them independently.

Do not require a complete challenger architecture to win before preserving a component that demonstrates incremental value. Conversely, a successful component does not validate the contributor's other components.

For external contributions, component-wise promotion is preferred over wholesale adoption unless the complete architecture itself has been prospectively tested and reproduced.

## 7. External contribution promotion safeguards

Use `governance/external_contribution_protocol.md` before promoting any material outside contribution.

A component may proceed even if the source artifact has:

- incorrect terminology;
- an unsupported mechanism narrative;
- unverifiable performance claims;
- invalid or legacy source data;
- an incorrect original stage assignment;

provided the component is reconstructed independently on canonical HEPS data and passes the normal evidence gates.

However, none of those source defects may be silently converted into evidence for the derivative.

If the derivative was selected after trying several transformations, windows, stage placements, graph formulations, thresholds, or other variants, retrospective performance is discovery evidence only. Promotion requires fresh frozen evidence after selection.

## 8. Required decision artifact

A promotion decision should state:

- claim/experiment IDs;
- evidence classification;
- requested architecture state;
- accepted/rejected authority;
- baseline comparison;
- known failure modes;
- prospective falsification rule;
- exact core files changed.

For a derivative external contribution, also state:

- source contribution path;
- extracted mathematical operator;
- difference from the original proposal;
- stage(s) tested;
- search/multiple-testing exposure;
- first untouched/prospective target after the derivative was selected.

## 9. Rejection and archiving

Rejected strategies remain in the historical record. Do not erase them: future agents need to know what was tested, why it failed, and whether a similarly named new concept is genuinely different.

Reject claims at the narrowest defensible level. If an external document contains multiple independent operators, do not use the failure of one component as automatic evidence that all others are worthless.

Before rejecting the underlying mathematical idea of a substantial external contribution, reviewers should verify that decomposition, stage fit, matched controls, and plausible alternative-stage testing were considered where appropriate.
