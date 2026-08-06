# Red-Team Review — ChatGPT Sol Coalition Assembly Research

**Date:** 2026-08-01  
**Proposal reviewed:** `workspace/contributions/contributor_chatgpt_sol_2026-08-01_coalition_assembly.md`  
**Verdict:** retain as challenger; do not merge into accepted architecture

## 1. Strongest finding

The most defensible result is the combinatorial maximum-coverage finding, not the retrospective 2026-07-31 pair pattern.

Conditional on an `n`-number candidate pool already containing all five winners, selecting the ten lines jointly can materially improve the probability that at least three winning numbers appear together on one line. In the search reported by the contribution:

- `n=18`: optimized 3+ coverage about `78.99%` versus matched-random about `64.66%`;
- `n=17`: optimized about `86.26%` versus random about `71.06%`;
- `n=14`: optimized about `99.55%` versus random about `89.69%`.

This is a real combinatorial portfolio effect. It does not depend on a physical lottery hypothesis.

## 2. Critical limitation: exact 5/5 is not solved

The user’s motivating failure was exact coalition assembly. The coverage optimizer does not solve that problem by itself.

If all five-subsets of the candidate pool are equally likely, every set of ten distinct submitted lines has the same exact-hit probability:

`10 / C(n,5)`.

Therefore the optimizer can improve 3+ coverage while leaving exact 5/5 unchanged. Any claim that the assembler now "knows" which five candidates belong together would be unsupported.

A genuine exact-line improvement requires a validated non-uniform coalition posterior.

## 3. Oracle-conditioned benchmark is intentionally artificial

The 98-target legacy benchmark guaranteed that all five true winners were present in each 18-number pool. This is useful for isolating assembly, but it is not a prediction backtest.

The injected winners were not given improved scores, which makes the test severe and methodologically clean for the narrow question. However, the result cannot be translated into an unconditional lottery success rate because real HEPS candidate pools often fail to contain all five winners.

Reports must retain the phrase **conditional on complete candidate recall**.

## 4. Legacy workbook must remain non-active

The 811 pre-2026 rows were used only to learn broad structural priors and stress-test algorithms. The repository doctrine explicitly forbids old pre-transition history as an active modelling dependency.

Accordingly:

- do not commit the workbook;
- do not wire the active prediction pipeline to it;
- do not tune current mechanical-era expert weights from those rows;
- if broad structural priors are later adopted, they require a separate justification and active-era recalibration.

## 5. Historical scorer results are negative evidence

The majority of score-ranked assemblers underperformed the matched-random conditional 3+ portfolio baseline in the oracle benchmark. This is valuable negative evidence.

It implies that the tested node scores, pair weights and role rewards did not contain enough coalition information to justify concentrating the portfolio around their top-ranked lines.

The proposal must resist the temptation to hide this result behind the successful coverage design.

## 6. 2026-07-31 is vulnerable to retrospective overfitting

The winning line `10,11,37,45,46` contains two adjacent pairs and a hot anchor. After observing the result, a pair-of-pairs narrative is easy to construct.

The retrospective diagnostic is still useful because the candidate pool was frozen before the draw, but the **new assembler was not**. Therefore:

- the 4-main graph line is a retrospective architecture diagnostic;
- rank 19 for the true line in the pair-pair-anchor generator is not a pre-draw prediction;
- dual-adjacency must not be promoted without prospective evidence.

## 7. Candidate compression is not validated

Reducing the frozen 17-number pool to 14 candidates greatly improves the theoretical assembly search space and happened to preserve all five 2026-07-31 winners under one role-aware rule.

But the same rule degraded holdout recall. This is a classic recall/precision trade-off. A smaller pool is beneficial only if the candidate stage can preserve winner recall.

No compression rule should be made mandatory at this stage.

## 8. Maximum-coverage objective can optimize the wrong KPI

A portfolio designed to maximize 3+ coverage may sacrifice:

- 4+ concentration;
- exact-line probability under a non-uniform posterior;
- PowerBall pairing quality;
- accepted HEPS lane diversity.

The reported 4+ improvement from unweighted coverage optimization is small. A future selector should therefore use a multi-objective function and report all primary KPIs.

## 9. Required prospective controls

Before promotion, freeze and compare at least the following selectors on unseen mechanical-era draws:

1. current HEPS lane allocator;
2. current scores + ordinary top-ten ranking;
3. unweighted maximum 3+ coverage;
4. posterior-weighted maximum coverage;
5. pair/hypergraph challenger;
6. matched random portfolio with the same candidate-pool size and line count.

For each target record:

- candidate-pool recall;
- best main overlap;
- number of 3+, 4+ and 5 lines;
- same-line PowerBall result;
- unique pair and triple coverage;
- exact submitted-line denominator;
- null percentile.

## 10. Red-team conclusion

**Do not merge into core.**

The maximum-coverage selector is a legitimate engineering improvement candidate because it directly addresses portfolio redundancy and has a mathematically demonstrable conditional benefit for 3+ coverage.

The pair/hypergraph scoring components remain experimental. The exact 5/5 assembly problem is unresolved until HEPS demonstrates a non-uniform coalition model that survives prospective matched-null evaluation.
