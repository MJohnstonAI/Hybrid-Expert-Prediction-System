# HEPS Agent Rules

This file establishes the operating rules for all AI coding agents, LLM reviewers, and automation scripts interacting with this repository.

## 1. Operating mode

This repository is a private, proprietary, paper-trading research workspace for South African PowerBall HEPS.

All prediction slates are experimental. Do not present them as guaranteed, financially reliable, or as evidence of a durable lottery edge.

## 2. Active data doctrine

- Use the post-May/June 2026 South African PowerBall 5/50 + PB 1/16 regime for active modelling.
- Do not require Excel files for active processing; legacy spreadsheets may be used only as explicitly labeled diagnostic priors.
- Use `data/draw_history.jsonl` as the canonical ledger.
- Use `data/draw_manifest.json` as current dataset state.
- Earlier algorithms may be reused only with current-regime recalibration/validation.
- Do not assume PowerBall became primary electronic RNG on 2026-06-22. Treat mechanism as mechanical-primary-or-unconfirmed until direct operator evidence resolves it.

## 3. Source-of-truth hierarchy

1. `data/draw_history.jsonl`
2. `data/draw_manifest.json`
3. `configs/agent.md`
4. `core/heps_architecture.md`
5. `core/heps_strategy.md`
6. `workspace/contributions/`
7. `workspace/reviews/`
8. `outputs/`

## 4. Data validation

Before prediction/backtest/post-draw work verify:

- unique chronological draw dates;
- five unique sorted main integers 1–50;
- PowerBall integer 1–16;
- `macro_sum` equals the main-number sum;
- each row has `regime`;
- machine name is `unknown` rather than guessed when evidence is absent.

Known correction: `21+26+40+42+44 = 173`, not 193.

## 5. Architecture review discipline

Use:

1. `workspace/contributions/` proposal;
2. `workspace/reviews/red_team_*` critique;
3. grounding/Q&A when factual uncertainty matters;
4. `workspace/reviews/merge_decision_*` decision;
5. only accepted experimental methodology enters core docs.

HEPS v33.4 accepts the Pair-of-Pairs assembler from v33.3 plus the Candidate Recall Guard and Directional Scenario Router as experimental core workflow. This is an architecture claim, not a predictive-edge claim.

## 6. Required prediction pipeline

### Stage A — Expert nominations

Generate candidate evidence from accepted experts including void, shadow, sorted-position, stale-hot, midfield/structural rescue, register/tri-cluster and controls. Preserve provenance before aggregation.

### Stage A2 — Dual candidate pools

Maintain and publish:

- `core_pool` (research range 13–18);
- `rescue_pool` (roughly 22–26).

Report pool size with every recall metric. Larger pools mechanically improve expected recall and must not be presented as model skill.

### Stage B — H/L/R scenarios

Publish at least:

- `null_geometry` scenario from exact fair order-statistic H/L/R probabilities;
- `hlr_motif_challenger` frozen before the target;
- optional `director_motif` if the user explicitly freezes one pre-draw.

HLR is a scenario router, never a hard veto. Different scenarios receive different lines.

### Stage C — Pair-of-Pairs + Anchor

Preferred topology:

`pair_A + anchor + pair_B`

Preserve pair/anchor expert provenance. Dual compact clusters are legal.

### Stage D — 20-line default research slate

Unless the user explicitly requests another volume:

- 8 core-pool coalition lines;
- 4 rescue-pool specialist coalitions;
- 4 directional-scenario lines;
- 2 maximum-coverage rescue lines;
- 2 matched random/control lines.

For 10-line experiments, label them as a separate v33.3/reduced-budget benchmark.

All submitted lines stay in the denominator after the result.

## 7. Matrix B PowerBall protocol

Score three separate layers:

1. **Direction** H/L/R relative to current PB;
2. **VVD/displacement** challenger, with an explicit definition;
3. **Exact PB ranking**.

Exact fair direction probabilities from current PB `p` are:

- `P(L)=(p-1)/16`
- `P(R)=1/16`
- `P(H)=(16-p)/16`

Never evaluate H/L/R against a naïve 1/3 baseline.

Do not silently equate the director's intuitive VVD with absolute numerical delta.

## 8. Prediction artifact requirements

Every frozen prediction artifact must contain:

- target date;
- ledger cutoff;
- architecture version;
- generation timestamp;
- `paper_trading_only` status;
- core and rescue pools with provenance;
- HLR/null/director scenarios;
- supported pairs and top Pair-of-Pairs coalitions;
- all submitted lines and class labels;
- coverage/redundancy diagnostics;
- PB direction base rates;
- VVD hypothesis if used;
- exact PB ranking;
- matched-control design;
- uncertainty/evidence boundary.

## 9. Post-draw attribution order

1. core-pool candidate recall;
2. rescue-pool candidate recall;
3. HLR/scenario direction accuracy versus exact null;
4. pair-edge recall;
5. coalition generation;
6. final portfolio routing;
7. PB direction;
8. PB VVD/displacement;
9. exact PB;
10. matched random comparison;
11. retrospective Main/XTRA cross-score only if useful.

Failure labels include candidate, scenario, pair-edge, anchor, coalition, final-routing, PB-direction, PB-VVD, PB-exact, regime/machine uncertainty and null-equivalent.

## 10. PowerBall XTRA / machine rules

PowerBall and PowerBall XTRA are separate draws. A main-game prediction cannot receive prospective XTRA credit unless XTRA was explicitly targeted pre-draw.

Record machine identity only from a trustworthy source. Do not infer a machine swap from numerical similarity or from which slate would have performed better.

## 11. Caution rules

- Sorted slots are order statistics, not physical draw order.
- Physical/mechanical hypotheses remain provisional.
- No hard entropy, macro-sum, parity, decade or adjacency vetoes.
- Do not promote HLR or VVD from one successful directional call.
- Do not retune expert weights aggressively after one target.
- Maximum coverage improves conditional assembly, not exact-win probability under a uniform posterior.
- Every claim of predictive advantage requires prospective/walk-forward evidence and matched-null comparison.
