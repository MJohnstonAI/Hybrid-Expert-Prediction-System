# E0016 Reproduction Lane

Reproduce each component independently using only the canonical post-June target-system ledger.

Required boundaries:

- Main: `data/draw_history.jsonl`, 2026-06-02 onward only.
- XTRA: `data/powerball_xtra_history.jsonl`, 2026-06-02 onward only.
- No 2018-2025 workbooks.
- No target leakage.
- Main/XTRA fitted state must remain independent.

Required reproductions:

1. Main probability-current replay and prospective shadow scoring.
2. Main Lévy tail diagnostic versus `NULL_VVD_STRUCTURAL` using proper displacement scores.
3. XTRA Richardson pair-dispersion replay and prospective K13/K20 scoring at matched exposure.

Report code reproduction and independent implementation separately. Preserve discrepancies rather than editing the E0016 originating results.
