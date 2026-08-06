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

The 2026-08-01 Coulomb Pair-of-Pairs + Anchor Coalition Assembler has completed this review path and is accepted as an **experimental core assembly module** in HEPS v33.3.

## 6. Prediction portfolio rules

Use diversified expert evidence, but do not publish expert-lane seed lines independently without coalition synthesis.

### Required synthesis order

1. Generate candidate evidence from tri-cluster/high-register, void-bridge, stiction-shadow, sorted-position, stale-hot/return-horizon, and other accepted experts.
2. Preserve candidate provenance; do not flatten all expert identities into a single score too early.
3. Build supported pair edges and pair-of-pairs + anchor challenger lines.
4. Permit dual-cluster topology when supported, including one low pair plus one high pair joined by an anchor.
5. Select the nine model-driven final lines jointly using coalition rank plus maximum-coverage/redundancy control.
6. Keep one chaos/random-control line outside the optimized selector.

### Required top-10 allocation

- 3 pair-of-pairs + anchor coalition champion lines;
- 2 void-led coalition lines;
- 2 tri-cluster/high-register coalition lines;
- 1 stiction-shadow or sorted-structure coalition line;
- 1 cross-expert maximum-coverage coalition line;
- 1 chaos / random-baseline hedge line.

Every prediction slate must include:

- branch/version;
- target draw date;
- dataset manifest reference;
- generation timestamp;
- prediction status: `paper_trading_only`;
- candidate hierarchy and expert provenance;
- supported-pair summary;
- pair-of-pairs + anchor challenger summary;
- main-number slates;
- PowerBall candidates/ranking;
- coalition/lane rationale;
- portfolio coverage and redundancy diagnostics;
- uncertainty notes.

## 7. Coalition assembly rules

The preferred synthesis topology is:

`pair_A + anchor + pair_B`

where the two pairs are disjoint and the anchor is distinct from both.

Pair support may come from:

- Coulomb void / temporal starvation;
- stiction and ±1/±2 shadow;
- adjacency / short-span geometry;
- stale-hot return horizon;
- pair-bridge evidence;
- sorted-position compatibility;
- cross-expert consensus;
- complementary expert roles.

Each coalition line must retain:

- pair A and its supporting experts;
- pair B and its supporting experts;
- anchor and its supporting experts;
- candidate scores before assembly;
- coalition score / interaction rationale;
- portfolio marginal-coverage contribution.

Do not reject a line solely because it contains two separated adjacent/compact pairs. The 2026-07-31 diagnostic showed that the actual winning topology `10,11,37,45,46` can be represented as `(10,11) + 37 + (45,46)`.

## 8. Evaluation rules

Primary KPIs:

- candidate-pool recall of the five winning mains;
- pair-edge recall of winning pairs;
- per-line and per-game exact 3, 4, and 5 main-number outcomes;
- best assembled overlap conditional on candidate recall;
- same-line 3+ main numbers plus PowerBall;
- same-line 4+ main numbers plus PowerBall;
- same-line 5 main numbers plus PowerBall (ultimate outcome);
- Top-10 3+ main-number overlap;
- Top-100 3+ main-number overlap;
- Top-100 4+ main-number overlap;
- PowerBall exact hit rate;
- anchor hit rate;
- unique-pair / unique-triple portfolio coverage;
- ±1 drift support;
- macro-sum pass/fail;
- diversity / coordinate-overlap score;
- comparison against the previous selector and a matched random-filtered baseline.

Always report submitted line volume with hit counts. Candidate discovery and assembly must be scored separately.

The accepted 2026-08-01 breakthrough is an **assembly-architecture improvement**: the previous 31 July portfolio assembled at most 2/5 from a candidate hierarchy that contained all five winners, while the retrospective coalition diagnostic assembled 4/5 and generated the exact winning line among its challenger set. This does not by itself prove a durable predictive edge.

Do not claim a strategy is proven without walk-forward/prospective validation and a random-filtered baseline.

## 9. Mechanical-era caution rules

- Sorted Slot1–Slot5 values are order statistics, not physical draw order.
- Do not claim physical laminar path tracking unless drawn-order data exists.
- Treat cross-chamber coupling as unproven unless strong empirical or machine-design evidence is added.
- Use tri-cluster as a portfolio component, not a universal forced rule.
- Treat all mechanical hypotheses as provisional until enough post-transition draws exist.
- Do not describe retrospective 4/5 assembly as a guaranteed or proven exact-win method.
