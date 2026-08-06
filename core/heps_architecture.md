# HEPS Master Architecture

## Architecture

**HEPS v34.0 — Collaborative Staged Mixture-of-Experts**

Status on this branch: migration candidate pending review.

## Purpose

HEPS is an AI-driven, multi-agent, paper-trading research system for South African PowerBall. The repository is both the executable research doctrine and the shared scientific memory used by independent AI models to propose, test, reproduce, falsify, synthesize, and improve the architecture.

The active architecture is deliberately separated from experimental research. Expert status and authority are machine-readable in `core/expert_registry.yaml`.

## Data doctrine

- Canonical ledger: `data/draw_history.jsonl`
- Dataset state: `data/draw_manifest.json`
- Active regime: post-May/June 2026 mechanical-era South African PowerBall
- Main field: five unique main numbers from 1-50
- PowerBall field: one number from 1-16
- Slot1-Slot5 are sorted order statistics, not physical draw order

Older draw history may be used for explicitly labelled discovery, calibration, null, transfer, or robustness analysis. Active mechanical-era claims require validation on the active regime.

## Scientific governance

- Agent constitution: `AGENTS.md`
- Nomenclature: `governance/nomenclature.md`
- Research standard: `governance/research_protocol.md`
- Autonomous collaboration: `governance/collaboration_protocol.md`
- Promotion rules: `governance/promotion_policy.md`
- Expert state: `core/expert_registry.yaml`
- Open questions: `knowledge/open_questions.md`
- Experiment index: `experiments/registry.csv`

No single AI research session may promote its own unreviewed idea directly into this file.

---

# Matrix A — Main-Number Architecture

The main field is a **staged mixture of experts**. Information should be compressed progressively so that failure can be localized to a specific stage.

## Stage 1 — Slot Forecast

Purpose: forecast state/direction for each sorted slot before candidate selection.

Production architecture currently retains sorted-position diagnostics. Experimental slot-direction systems may run in shadow mode according to `core/expert_registry.yaml`.

### Experimental interface: `MAIN_HLR_SLOT`

When enabled in an experiment, HLR must output one committed direction for every sorted slot:

`Slot1..Slot5 -> LOW | REPEAT | HIGH`

Its forecast is mandatory **within that experiment**, but its authority is separate. Until promoted, HLR may not hard-eliminate conflicting coordinates.

## Stage 2 — Candidate Funnel

Purpose: rank coordinates and preserve sufficient exposure before combination assembly.

Current production-capable experts include:

- `MAIN_STICTION_SHADOW` — exact repeat and +/-1 or +/-2 coordinate support;
- `MAIN_VOID_BRIDGE` — starvation/canyon support;
- `MAIN_SORTED_SLOT_DENSITY` — order-statistic slot support;
- `MAIN_HARMONIC_BOUNDARY` — boundary/high-register exposure control.

Shadow/experimental candidate experts may contribute diagnostic scores without production authority, including `MAIN_GPR8` and `MAIN_VVD_DELTA` according to the registry.

### Authority principle

Candidate experts should prefer soft scoring and exposure adjustment over hard elimination unless a separate promotion decision grants veto authority.

## Stage 3 — Coalition Assembly

Purpose: estimate which candidate coordinates belong in the same five-number line.

This stage may use pair, graph, pair-of-pairs, anchor, or other explicitly tested interaction features.

Current coalition research such as `COALITION_PAIR_OF_PAIRS_ANCHOR` remains experimental until independently validated.

## Stage 4 — Combination Morphology

Purpose: score completed legal combinations by structural features without confusing common morphology with intrinsic probability of an exact line.

Current/experimental morphology families include:

- `MORPH_SUM_SPREAD`;
- `MAIN_TRI_CLUSTER`;
- `MORPH_SLDV`;
- gap morphology;
- parity/register structure;
- terminal-digit structure.

Every morphology expert should be evaluated against the combinatorial base rate of the structure it prefers.

A useful morphology filter compresses combination space while retaining winning lines disproportionately well.

## Stage 5 — Winner-Float Ranking

Purpose: rank surviving legal combinations so that evidence-supported combinations rise relative to false positives.

The canonical research target is future winning-line rank, not retrospective ability to refit a known winner.

`RANK_WINNER_FLOAT` is currently experimental.

Required evaluation should include where applicable:

- exact winning-line rank;
- percentile in survivor universe;
- Top-100K / Top-10K / Top-1K / Top-500 / Top-100 / Top-20 survival;
- paired comparison against random ordering and simpler frozen rankers;
- leave-one-expert-out attribution after the target is known.

## Stage 6 — Portfolio Optimization

Purpose: compress the ranked survivor universe to the final paper-trading slate while preserving useful exposure and reducing duplicate lines.

The portfolio optimizer must report submitted-line denominator and diversity/exposure.

### Chaos control

`PORTFOLIO_CHAOS_BASELINE` remains mandatory as a methodological control/hedge. Its role is to measure and protect against overfitting, not to claim predictive superiority.

The historical fixed top-10 lane allocation remains a compatibility baseline, not a constitutional allocation. New allocations must be frozen in the relevant draw cycle and evaluated against matched controls.

---

# Matrix B — PowerBall Architecture

PowerBall remains a separate 1-16 field.

Current production research components include:

- 16-ball fulcrum center 8.5;
- upper-tier resonance/ramp diagnostics;
- provisional circuit-breaker threshold `tau = 6.8`;
- stiction and +/-1 or +/-2 support;
- low-collapse hedge.

PowerBall evidence must be evaluated independently rather than inferred from main-field success.

---

# Expert Forecast vs Expert Authority

HEPS separates an expert's **prediction** from its **authority**.

Possible authority levels progress from low risk to high risk:

1. diagnostic only;
2. shadow score;
3. soft ranking weight;
4. exposure adjustment;
5. portfolio allocation;
6. candidate pruning;
7. hard elimination/veto.

Promotion to higher authority requires stronger evidence. A 60-70% directional expert, for example, may be valuable as a score while being too brittle as a veto.

The active authority of each named expert is controlled by `core/expert_registry.yaml`.

---

# Three-Speed Self-Improvement Loop

## Fast learning — state

After every validated draw, frozen formulas may update deterministic state such as:

- recurrence/gap states;
- HLR history if the experimental module is enabled;
- VVD history;
- expert sufficient statistics;
- score ledgers.

## Medium learning — parameters

Weights, transition probabilities, shrinkage coefficients, and ranking parameters may update only through a predeclared learning algorithm or reviewed accumulated evidence.

A single post-draw miss must not trigger ad-hoc weight changes.

## Slow learning — architecture

New experts, removed experts, changed semantics, or changed authority require:

`proposal -> experiment -> reproduction -> red-team -> synthesis -> promotion decision`

Only then may this architecture or the expert registry be changed on the active branch.

---

# Per-Draw Execution Cycle

Each target draw should have `cycles/YYYY-MM-DD/`.

## Pre-draw

Freeze:

1. dataset state;
2. architecture version;
3. expert versions/authority/weights;
4. expert outputs;
5. candidate/slot funnel where applicable;
6. generated/ranked combination state where reproducibly representable;
7. final `paper_trading_only` slate.

## Post-draw

After the result is appended and validated:

1. score the frozen slate;
2. trace every winning main coordinate through the pipeline;
3. determine whether the exact winning line was generated;
4. record its rank if present;
5. compute expert attribution and counterfactual ranks where feasible;
6. write Physics of Failure;
7. create or reprioritize research questions;
8. update state under the three-speed learning rules.

Do not regenerate the frozen pre-draw artifacts after seeing the outcome.

---

# Physics of Failure

Physics of Failure is an attribution framework, not permission to retrofit the last winner.

For every target, identify the first failure stage:

- incorrect slot/state forecast;
- candidate coordinate suppressed or eliminated;
- coalition failed to assemble the correct line;
- morphology over-penalized the line;
- winner-float ranker buried the line;
- portfolio optimizer excluded a highly ranked line.

Where possible record leave-one-expert-out counterfactual rank changes. Weight changes require repeated evidence, not one target.

---

# Evidence and KPI Doctrine

All outcome rates retain their exposure denominator.

Core metrics include:

- per-slot forecast accuracy and candidate rank;
- 5/5 coordinate survival at declared basket sizes;
- exact winning-line generation rate conditional on candidate survival;
- combination-space compression versus winner retention;
- exact winning-line rank/percentile;
- Top-K rank survival;
- exact 3/4/5 main outcomes per submitted line and per game;
- same-line PowerBall outcomes;
- random/simple/current baseline comparisons;
- portfolio diversity.

A single jackpot outcome is a project milestone but does not by itself prove a durable predictive edge.

---

# Current Experimental Priorities

The canonical current questions are maintained in `knowledge/open_questions.md` rather than embedded permanently here.

As of 2026-08-06, high-value unresolved research includes:

- independent HLR validation beyond order-statistic mean reversion;
- VVD conditional movement value;
- Slot Constraint Funnel efficiency versus matched controls;
- Winner-Float ranking failure attribution;
- morphology residual value including SLDV;
- prospective GPR-8 falsification.

These are research priorities, not automatically active production rules.
