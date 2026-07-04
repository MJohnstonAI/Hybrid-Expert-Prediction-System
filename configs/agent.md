# HEPS Agent Rules

This file establishes the operating rules for all AI coding agents, LLM reviewers, and automation scripts interacting with this repository.

## 1. Operating mode

This repository is a private, proprietary, paper-trading research workspace for the South African PowerBall HEPS system.

All generated prediction slates are experimental. Do not present any slate as guaranteed, financially reliable, or suitable as gambling advice.

## 2. Active data doctrine

- Use post-May/June 2026 South African PowerBall mechanical-era data as the active modelling dataset.
- Do not require Excel files for active processing.
- Use `data/draw_history.jsonl` as the canonical ledger.
- Use `data/draw_manifest.json` as the current dataset state file.
- Earlier HEPS algorithms may be reused, but all parameters must be recalibrated on the active dataset.

## 3. File boundary and source-of-truth hierarchy

Only read and write within this repository unless the user explicitly instructs otherwise.

Source-of-truth order:

1. `data/draw_history.jsonl`
2. `data/draw_manifest.json`
3. `configs/agent.md`
4. `core/heps_architecture.md`
5. `workspace/contributions/`
6. `workspace/reviews/`
7. `outputs/`

## 4. Data validation rules

Before any prediction, backtest, or post-game analysis, validate the draw ledger.

Each draw row must satisfy:

- unique `draw_date`;
- five unique main numbers;
- main numbers are integers from 1 to 50;
- PowerBall is an integer from 1 to 16;
- main numbers are sorted ascending unless true drawn-order data is explicitly available;
- `macro_sum` equals the sum of the five main numbers;
- the draw row includes `regime`.

Known correction:

- `21 + 26 + 40 + 42 + 44 = 173`, not 193.

## 5. Architecture update rules

Do not rewrite `core/heps_architecture.md` directly because one model proposed a change.

Use this merge discipline:

1. Proposal goes to `workspace/contributions/contributor_<model>_<date>.md`.
2. Red-team critique goes to `workspace/reviews/red_team_<date>.md`.
3. Grounding Q&A goes to `workspace/reviews/qna_grounding_<date>.md`.
4. Merge decision goes to `workspace/reviews/merge_decision_<date>.md`.
5. Only accepted changes may be incorporated into `core/heps_architecture.md`.

## 6. Prediction portfolio rules

Use portfolio lanes rather than one monolithic expert.

Recommended top-10 allocation:

- 3 tri-cluster / high-register continuation lines;
- 3 void-bridge / canyon-fill lines;
- 2 stiction-shadow continuation lines;
- 1 sorted-position momentum line;
- 1 chaos / random-baseline hedge line.

Every prediction slate must include:

- branch/version;
- target draw date;
- dataset manifest reference;
- generation timestamp;
- prediction status: `paper_trading_only`;
- main-number slates;
- PowerBall candidates;
- lane rationale;
- uncertainty notes.

## 7. Evaluation rules

Primary KPIs:

- Top-10 3+ main-number overlap;
- Top-100 3+ main-number overlap;
- Top-100 4+ main-number overlap;
- PowerBall exact hit rate;
- ±1 drift support;
- macro-sum pass/fail;
- diversity / coordinate-overlap score;
- comparison against a random-filtered baseline.

Do not claim a strategy is proven without walk-forward validation and a random-filtered baseline.

## 8. Mechanical-era caution rules

- Sorted Slot1–Slot5 values are order statistics, not physical draw order.
- Do not claim physical laminar path tracking unless drawn-order data exists.
- Treat cross-chamber coupling as unproven unless strong empirical or machine-design evidence is added.
- Use tri-cluster as a portfolio lane, not a universal forced rule.
- Treat all mechanical hypotheses as provisional until enough post-transition draws exist.
