# HEPS Main Session Handoff — 2026-08-27

## Purpose

This file is a durable handoff from the long-running ChatGPT Main PowerBall research session so a fresh ChatGPT session can reconstruct the same scientific context from the repository without relying on the exhausted chat context window.

Repository: `MJohnstonAI/Hybrid-Expert-Prediction-System`

The repository is authoritative. This handoff summarizes the conversation-specific state and recent lessons, but if any draw, experiment, registry, or decision here conflicts with a newer repository artifact, the current repository wins.

## New-session instruction

Before doing any prediction, post-draw audit, architecture change, or research synthesis, read the mandatory repository order from `AGENTS.md`:

1. `AGENTS.md`
2. `governance/nomenclature.md`
3. `governance/research_protocol.md`
4. `data/draw_manifest.json`
5. `core/heps_architecture.md`
6. `core/expert_registry.yaml`
7. `knowledge/open_questions.md`
8. `experiments/registry.csv`
9. relevant experiment/cycle/contribution files

Use `data/draw_history.jsonl` as the canonical Main ledger.

## Scientific operating style

Act as:

- external auditor / red-team quantitative researcher;
- creative strategy generator, but never confuse elegance with evidence;
- lead data interpreter who converts HEPS outputs into concise actionable research decisions.

Use only the evidence labels:

- `BREAKTHROUGH`
- `PROVISIONAL_SIGNAL`
- `INSUFFICIENT_EVIDENCE`
- `REJECT`

Never retrofit a result into a frozen pre-draw artifact. Keep pre-draw prediction and post-draw scoring separate. Exact legal lines are equiprobable under the IID lottery null unless a validated mechanism is demonstrated.

## Data boundaries

Active Main work uses the June-2026-onward ledger. Legacy PRNG-era Excel files `Train on Main.xlsx` and `Train on Plus.xlsx` have no active prediction authority.

Director-approved public result sources remain:

- `powerball.net/southafrica/results`
- `lottery.co.za/powerball/results`
- `nationallottery.co.za/results/powerball/`

Do not substitute other lottery-result sites without explicit director approval.

Main and PowerBall XTRA are separate systems. XTRA may contribute methodology, but Main must not import XTRA coordinates or motifs without an explicitly tested cross-game protocol.

## Current repository state at handoff

As of this handoff, `data/draw_manifest.json` reports:

- latest draw id: `25`
- latest draw date: `2026-08-25`
- latest Main: `[5,34,39,43,45]`
- latest PowerBall: `1`
- row count: `25`

This is newer than the final result discussed inside the long chat, which was the verified 2026-08-21 Main draw `[2,4,5,24,49] | PB4`. Always reload the current manifest and ledger before forecasting.

## Key architecture doctrine

Canonical staged pipeline:

`Slot Forecast -> Candidate Funnel -> Coalition Assembly -> Morphology -> Winner-Float Ranking -> Portfolio Optimization`

PowerBall remains a separate matrix.

Critical principles:

- Candidate acquisition remains the primary bottleneck.
- Johnson covering is assembly-only and has zero candidate-discovery authority.
- K13 is an operational research target, not a proven optimum or hard scientific truth.
- Expert forecast and expert authority are separate.
- HLR and VVD are sorted-order-statistic concepts, not physical draw-order trajectories.
- Structural nulls are mandatory comparators, not predictive experts.
- Global candidate existence `P(n appears anywhere)` must remain distinct from exact-slot probability `P(S_j=n)`.
- Algebraic/motif experts must never receive hindsight credit.

## Important recent Main results and lessons from this chat

### 2026-08-18

Reported/recorded result:

`3,7,20,31,39 | PB13`

From previous `[14,15,19,39,44] | PB3`:

- Main HLR: `LLHLL`
- Main VVD: `[11,8,1,8,5]`
- PB direction: HIGH
- PB VVD: `10`

E0008 first prospective target was negative:

- primary S1 reflected VVD9 -> 5 missed actual S1=3 / VVD11;
- primary S4 VVD4 HIGH -> 43 missed actual S4=31 / VVD8 LOW;
- matrix-wide VVD6 convergence produced `0/6` exact VVD hits.

Conclusion: cross-lane algebraic motifs remain diagnostic/residual only and should not override calibrated distributions.

### 2026-08-21

Verified Main result:

`2,4,5,24,49 | PB4`

From previous `[3,7,20,31,39] | PB13`:

- Main HLR: `LLLLH`
- Main VVD: `[1,3,15,7,10]`
- PB direction: LOW
- PB VVD: `9`

This was not treated as a true statistical black swan. It was a tail-regime draw that exposed over-concentration.

Main failure diagnosis:

1. over-concentration in the wrong HLR regime;
2. insufficient tail-VVD protection;
3. hypothesis churn, where attractive motifs displaced calibrated probability mass;
4. candidate acquisition failed before downstream assembly could help.

Important forensic points:

- S1 `3 -> 2` was only VVD1 and should have survived via structural mass + simple shadow support.
- S2 `7 -> 4` was VVD3, also not extreme.
- S3 `20 -> 5` was the true tail displacement, VVD15.
- S5=49 was structurally ordinary for Slot5 and should not have been crowded out by a narrow exact-number shortlist.

This motivated E0009.

## E0009 — Distribution-First State Convergence and Tail-Rescue

Read `experiments/E0009/` before the next Main forecast.

Core doctrine under test:

`state -> direction distribution -> displacement distribution -> coordinate probability -> convergence -> candidate compression -> assembly`

Key ideas:

- S1 Anchor Gate: preserve LOW/REPEAT/HIGH probability mass; S1 is a sorted-state routing anchor, not a physical cause.
- HLR scenario mixture: no single HLR vector should hard-veto competing regimes.
- full VVD distributions before exact-point forecasts;
- target-blind tail-rescue at fixed total exposure;
- global coordinate mobility separate from exact-slot provenance;
- confidence increases only when genuinely independent residual paths converge.

## XTRA methodological lesson relevant to Main

The XTRA session performed exceptionally well on 2026-08-21 XTRA, reportedly predicting three Main XTRA numbers and PB2. The most useful transferable lesson is methodological, not numerical:

For PowerBall, do not predict the exact ball first. Predict:

1. HLR state: LOW / REPEAT / HIGH;
2. VVD displacement distribution;
3. exact-state successor distribution conditioned on the current PB;
4. VVD-state successor distribution conditioned on the current PB VVD;
5. translate only legal direction/displacement combinations to exact balls;
6. increase exact-ball confidence only when independently defined paths converge;
7. diversify when the paths disagree.

The Main PB analysis before 2026-08-21 had LOW direction correct but several incompatible exact-ball stories (`8`, `11`, `5` etc.), so there was no true convergence. Do not manufacture a primary exact PB when the state models disagree.

## Ox Alpha contribution and disposition

Ox Alpha / Cline contributed a null-first architecture proposal and algebraic VVD red-team review on 2026-08-24.

The contribution was not accepted wholesale.

The subsequent corrected repository synthesis is **E0011 — Null-Control, Residual Convergence and Conditional PowerBall Transitions**. Read `experiments/E0011/`.

Key disposition:

- ACCEPT / high priority: statistical-power honesty gate;
- ACCEPT / high priority: expert residualization and redundancy audit;
- REWORK: null-first pipeline is a control/comparator, not a predictive K13 selector;
- REJECT as written: null-derived global-mobility rescue, because under IID 5/50 `P(n appears anywhere)=0.1` for every coordinate;
- REWORK: unconditional PB Dirichlet frequency model into conditional transition shrinkage `P(PB_{t+1}=n | PB_t=s)` plus `P(VVD_{t+1}=d | VVD_t=v)`;
- algebraic motifs remain diagnostic and correlated lane agreement cannot be counted as independent votes;
- non-significance means no detected edge at the tested exposure/sample, not proof of zero effect.

Critical mathematical point:

A pure structural-null global coordinate field is flat:

`P(n appears anywhere)=5/50=0.1` for every `n=1..50`.

Therefore exact structural nulls are excellent calibration controls but cannot rank one predictive K13 coordinate basket over another under the IID null.

## Current high-value research priorities

Prioritize repository state over this list, but the recent direction is:

1. candidate acquisition / safe exclusion at fixed exposure;
2. E0009 distribution-first field;
3. E0011 expert residualization / non-redundant convergence;
4. VVD-R full displacement distributions against `NULL_VVD_STRUCTURAL`;
5. S1 scenario routing without hard regime collapse;
6. global candidate mobility / coordinate preservation;
7. target-blind tail rescue at fixed K;
8. conditional PowerBall transition model;
9. expert redundancy audit;
10. machine-conditioned surveillance only as a long-horizon bias-detection research stream.

## Conversation-specific warnings

- Do not resurrect the rejected broad algebraic VVD closure as if recent examples prove it.
- Do not let an attractive exact-number story override the probability field without prospective evidence.
- Do not treat different formula rewrites as independent convergence paths.
- Do not treat HLR as a hard gate while it remains experimental.
- Do not call Slot1 a physical causal anchor; it is an architectural/state-space anchor because sorted-order geometry conditions downstream legal states.
- Do not give wrong-slot candidates exact-slot credit; distinguish anywhere-coordinate survival from exact-slot accuracy.
- Do not import XTRA coordinates into Main. Transfer only validated methodology.
- Do not reconstruct missing frozen predictions after results are known.

## Recommended first action in the new ChatGPT session

After reading the mandatory repository files and this handoff:

1. confirm the current Main ledger/manifest and latest verified draw;
2. inspect `experiments/E0009/`, `experiments/E0011/`, and any newer experiment IDs;
3. inspect the latest Main cycle under `cycles/`;
4. state clearly what is already frozen for the next target and what remains unfrozen;
5. only then perform new analysis or construct the next slate.

The goal is continuity with scientific integrity, not continuity with any one chat narrative.
