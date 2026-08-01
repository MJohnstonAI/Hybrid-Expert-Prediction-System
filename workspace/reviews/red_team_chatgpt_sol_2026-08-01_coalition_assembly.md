# Red-Team Review — Coalition Assembly Benchmark

**Date:** 2026-08-01  
**Reviewer position:** Skeptical; challenger may proceed prospectively but must not be promoted

## Review verdict

The proposed bimodal assembler is a meaningful research improvement because it cleanly separates candidate recall from line assembly and introduces a rare-topology hedge. The evidence is not sufficient to claim an end-to-end prediction breakthrough.

## What the experiment establishes

1. The existing node-score and generic triple-coverage methods are weak conditional assemblers.
2. Out-of-time learned line rankers can recover substantially more 3+ and 4+ lines when all five targets are guaranteed to be in the pool.
3. The 31 July line is out-of-distribution for the learned rankers because it contains two separated adjacent pairs.
4. A target-blind pair-motif coverage lane improves the 31 July best overlap from 2/5 to 4/5.
5. No tested method selected the exact 31 July line in its final ten.

## Critical limitations

### 1. Oracle conditioning

The central benchmark inserts the five target numbers into the candidate pool. It measures assembly only. Results must never be described as ordinary prediction performance.

### 2. Candidate recall remains the harder bottleneck

A compact target-blind reservoir rarely contains all five winners. The experiment therefore cannot support a jackpot-level claim without a separate prospective candidate-recall improvement.

### 3. Historical-to-mechanical transfer

The rankers learn from 2018–2023 Main and Plus data. Repository doctrine says old draw history is not an active modelling dependency after the mechanical transition. The models may be used only as research priors until recalibrated and validated prospectively on the mechanical era.

### 4. Multiple comparisons

Several algorithms, selectors and lane allocations were examined. Reported p-values against random do not correct fully for model search and should be treated as descriptive.

### 5. Small mechanical sample

Only 14 mechanical-era targets were evaluated. Two exact conditional assemblies by the boosted ranker are interesting but statistically and operationally insufficient.

### 6. Structural regularity is not necessarily machine information

A line ranker can outperform random inside an oracle pool by preferring ordinary sums, parity and register patterns. That does not imply that it predicts which balls the machine will draw.

### 7. The 31 July motif was discovered after the outcome

The pair-of-pairs motif is motivated by a known result. Its general value must be demonstrated prospectively. The target-blind implementation reduces, but does not eliminate, post-hoc hypothesis risk.

## Required safeguards

- Freeze candidate pools and line scores before every draw.
- Keep the boosted and motif lanes separately attributable.
- Score the full pipeline and the oracle-conditioned assembler separately.
- Retain a matched random portfolio with the same pool, line count and structural constraints.
- Do not adjust lane allocation after seeing a target.
- Record every challenger version and configuration hash.
- Require at least 30 future targets before promotion.

## Recommended implementation status

- `scripts/`: acceptable as research tooling.
- `data/research/`: acceptable as a frozen historical snapshot, clearly excluded from active doctrine.
- `workspace/contributions/`: acceptable.
- `outputs/research/`: acceptable.
- `core/`: **no change**.

## Final red-team decision

**Approve for prospective paper-trading evaluation only. Reject promotion to champion or claims of a proven predictive advantage.**
