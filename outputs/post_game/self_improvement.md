# DYNAMIC SELF-IMPROVEMENT LEDGER (self_improvement.md)

## Cognitive Adaptation Framework:
1.  **Ingest Target:** Read the target draw from the canonical
    `data/draw_history.jsonl` ledger and recompute derived values from
    `main_numbers`.
2.  **Calculate Blind Score Bands:** Map generated slates against the 3-Tier Matrix:
    *   *Band 1:* Exact coordinate hits.
    *   *Idolized Signal Efficiency ($E_{band}$):* Isolate the exact 1–100 score decile that yielded the highest concentration of $>4$ hit events.
3.  **Record Calibration Evidence:** Run `scripts/score_prediction.py` against
    the stored pre-draw slate and record portfolio and lane metrics. A single
    macro-sum deviation or hit result must not change $\gamma$ or expert
    weights.
4.  **Review Gate:** Accumulate at least 20 independently generated and scored
    target slates, compare lanes against random/null baselines, and use the
    contribution and red-team workflow for any proposed parameter change. Do
    not rewrite `core/heps_strategy.md` automatically.
