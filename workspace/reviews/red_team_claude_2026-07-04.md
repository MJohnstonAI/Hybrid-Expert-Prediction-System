# HEPS Red-Team Review — Claude (Anthropic)
**Reviewer:** Claude
**Date:** 2026-07-04
**Proposal Reviewed:** Full repository state as of first access (README, agent.md, heps_architecture.md, heps_strategy.md, docs/architecture_history.md, workspace/qna_grounding.md, workspace/red_team_critique.md, data/*, scripts/*)

---

## Data Integrity Check

- **Latest ledger row (before this review):** draw_id 9, 2026-06-30 — stale. A confirmed draw (3 July 2026: `9, 14, 27, 32, 34`, PB 15, macro_sum 116) was missing from the canonical ledger despite existing publicly since that date.
- **Action taken:** Appended via `scripts/append_draw.py` with a source URL. Ledger now validates at 10 rows; `sync_manifest.py --check` passes.
- **Row count:** 10 (was 9).
- **Duplicate dates:** none found.
- **Invalid numbers:** none found — `validate_draws.py` passed cleanly both before and after the append.
- **Stale assumptions found:** three, detailed below. All three share the same root cause: a numeric boundary was fixed early and never re-checked against new draws as they arrived, even though the doctrine documents (`agent.md` §8) explicitly warn against exactly this.

## Methodology Check

- **Is this walk-forward?** The KPI list and `tests/test_checklist.md` correctly require it in principle ("No target draw appears inside the training window"), but nothing in the repository currently *enforces* that check mechanically — it's a checklist item, not a script. Recommend a `scripts/check_no_leakage.py` that fails CI if a slate file's `generated_at` timestamp postdates the `target_draw_date`'s actual result being present in the ledger.
- **Any target leakage?** One historical instance, already partially self-corrected: `docs/architecture_history.md` records that earlier framing (VVD, ink-mass) was killed specifically because it was unfalsifiable given sorted (not drawn-order) data. That correction is good and should be treated as a model for how the *stiction* and *tri-cluster* lanes ought to be scrutinized next — see Statistical Concerns below.
- **Baseline included?** Yes — `scripts/simulate_null_model.py` is a real, working null-model generator and is wired into CI. This is a genuine strength; most prior HEPS documents in this project's history did not have an executable, checked-in baseline.
- **Sample size adequate?** No, and the repository is honest about this in places (`agent.md` §8: "treat all mechanical hypotheses as provisional until enough post-transition draws exist") but inconsistent about it in others — several fixed numeric thresholds are already contradicted by the 10 draws now in the ledger. See below.

## Statistical Concerns

### 1. Sorted-position momentum bounds are already falsified by the repo's own data
`core/heps_strategy.md`, Lane 3, states as a **hard rejection rule**: "restricts Slot 1 to its historical boundary ($1 \le X_{(1)} \le 15$) and Slot 5 to its boundary ($35 \le X_{(5)} \le 50$)... Rejects any candidate combination where the numbers cross their respective slot-bound statistical distributions."

Checked against the current 10-row ledger:
- Slot 1 has recorded values 16, 17, and 21 — three separate violations of the stated upper bound of 15.
- Slot 5 has recorded a value of 34 (3 July draw) — a violation of the stated lower bound of 35.

If applied literally as a hard filter, this rule would have rejected the actual real-world outcome on at least two separate draws. **Recommendation:** downgrade from a hard rejection rule to a soft scoring weight, and derive the bound from a rolling window of the active dataset rather than a fixed constant — recompute it every time `sync_manifest.py` runs rather than hand-setting it once.

### 2. The macro-sum boundary band is already falsified twice
`docs/architecture_history.md` (§2.2) and the Sum/Spread Governor description both cite a fixed acceptable band of **110 ≤ sum ≤ 160**, used to reject slates outside it.

Checked against the ledger: draw 3 (9 June) has macro_sum 92, and draws 8 and 9 (26/30 June) have macro_sum 165 and 173. **Three of ten actual observed outcomes fall outside the band claimed to bound "acceptable" outcomes.** Same recommendation as above: this should be a soft governor, recalculated from the live dataset, not a fixed constant carried over from an earlier (and much smaller) sample.

### 3. `outputs/post_game/self_improvement.md` still contains the exact failure pattern that caused a prior documented error
This file instructs: "If the actual macro-sum varies from the predicted sum by more than ±25, scale the compression factor (γ) dynamically by a factor of 0.15 × ΔVariance." This is an unconditional, automatic reaction to a single data point — the same pattern that, earlier in this project's history, caused a bad hand-typed macro-sum (193 instead of the correct 173) to trigger a 45% parameter change before anyone checked the arithmetic. The number itself has since been corrected in the ledger and in `agent.md`, but the *procedure* that would blindly react to it is still written down as doctrine in this file, unguarded.

Recommendation: any automatic parameter reaction should (a) require a minimum sample size before acting at all — this repository already uses "insufficient data until enough draws exist" language elsewhere, this file should say the same — and (b) require the triggering number to be independently recomputed from raw `main_numbers`, never taken from a cached or hand-entered field. This file also references `/data/draw_history.json` (no `l`) — a stale filename that no longer matches the actual canonical file (`draw_history.jsonl`).

### 4. The PowerBall pool size (16 vs 20) is asserted more confidently than the evidence supports
`workspace/qna_grounding.md` states: "Any calculation treating the bonus pool midpoint as 10.5 belongs to the deprecated 20-ball machine and must be rejected immediately." I checked how much the observed data actually supports this: if the pool were still 1–20 and the 16-ball figure were wrong, the probability of all 11 observed PowerBalls landing at ≤16 purely by chance is **8.6%** — not vanishingly small. This doesn't mean the 16-ball claim is wrong; it means it isn't yet *proven by the draw data alone*, and the doctrine document states it as settled fact rather than as "current working assumption, pending confirmation from an operator source." Recommend adding a citation requirement here specifically, since a wrong pool-size assumption would silently bias every PowerBall-related calculation in the system.

## Engineering Concerns

- `scripts/validate_draws.py`, `append_draw.py`, and `sync_manifest.py` are genuinely well-built: they cross-check `macro_sum` against the actual sum of `main_numbers` rather than trusting a stored value, enforce strict chronological and sequential ordering, and are wired into a real CI workflow. This is a substantive improvement over earlier hand-authored HEPS documents in this project and should be the standard the rest of the repository is held to — including the two files flagged above that don't yet meet it.
- `core/heps_strategy.md` references `scripts/score_prediction.py` in its synthesis protocol description; no such file exists in the repository. Either the file is missing or the reference is aspirational and should be marked as not-yet-implemented rather than stated as active.
- Tone/rigor inconsistency: `configs/agent.md` and `core/heps_architecture.md` are written with careful hedging and an explicit rejected-claims section. `core/heps_strategy.md`, `docs/architecture_history.md`, and `outputs/post_game/self_improvement.md` are written in more dramatized physical-mechanism language ("pneumatic suction chamber," "heavy-ink ball dynamics," "Idolized Signal Efficiency") without the same hedging. Recommend passing every core/ and outputs/ file through the same discipline agent.md already models — the file that sets the rules should not be the most careful document in the repository.

## What's already working well (stated plainly, not as a courtesy)

- The decision to kill the ink-mass hypothesis was correct and for the right reason: it was unfalsifiable given sorted, not drawn-order, data. That's exactly the right instinct and should be applied to the tri-cluster and stiction-shadow lanes next — both currently lack an explicit statement of what observation would falsify them.
- Correctly identifying that VVD was measuring ordinary order statistics rather than a distinct physical phenomenon, and demoting it accordingly, is good epistemic hygiene.
- The merge discipline in `agent.md` §5 (proposal → red-team → grounding → merge decision, with `core/heps_architecture.md` never edited directly) is the right structure and this review follows it.

## Decision

- [ ] Accept
- [x] Rework
- [ ] Reject

## Conditions for Merge

1. Convert the two hard numeric rejection rules (Slot1/Slot5 bounds; macro-sum band) into soft, dataset-derived weights, recalculated on every `sync_manifest.py` run.
2. Rewrite `outputs/post_game/self_improvement.md` to require a minimum sample size before any automatic parameter change, and to always recompute the triggering statistic from raw fields rather than trusting a cached value. Fix the stale `.json`/`.jsonl` filename reference while editing.
3. Add a citation or explicit "unconfirmed working assumption" label to the PowerBall pool-size claim in `workspace/qna_grounding.md`.
4. Either implement `scripts/score_prediction.py` or mark the synthesis protocol reference in `core/heps_strategy.md` as not-yet-implemented.
5. Ledger gap is already fixed as part of this review (draw 10 / 3 July appended, manifest re-synced, both validators re-run and passing).
