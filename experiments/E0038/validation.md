# E0038 validation — 2026-11-05

- `python scripts/validate_draws.py data/draw_history.jsonl`: passed, 45 rows.
- `python scripts/sync_manifest.py --check`: passed.
- `python scripts/validate_active_data.py`: passed for both 45-row ledgers, provenance and pre-draw pointers.
- `python scripts/check_stationarity.py`: advisory correctly reports mixed Main methods/machines; saved in `stationarity.json`.
- `python scripts/simulate_null_model.py --trials 100000 --seed 20260704`: completed; saved in `null_simulation.json`.
- `python scripts/structural_null.py --draw-id 39 --basket-size 13 --basket-size 20`: completed, including exact joint enumeration for the previous draw at the new block boundary.
- E0022 geometry reproduction: `oracle_k13_assembly_evolution.four_plus_cover(13,20)` agrees with `greedy_johnson_cover(..., four_plus_first)` at 788/1287 covered 4+ states and 20 exact-five states. No new coalition-rank lift is claimed.
- `python experiments/E0038/replay.py`: completed twelve target-excluded forecasts and scores.
- `python experiments/E0038/verify.py`: passed. All twelve target scores, Brier scores, PB deltas and K13 selections reproduce the unchanged E0037 scorer. Mutating all six target/future outcomes leaves each lane's first forecast unchanged. All forecast hashes, prefixes and twenty-line portfolio legality/uniqueness checks pass.
- `python -m unittest discover -s tests -v`: **88 tests passed**, 133.999 seconds. Log: `test_log_verified.txt`. TEMP/TMP pointed to `.cache/test-tmp` within the workspace.
- Initial run retained in `test_log.txt`: one stale E0035 historical-window assertion and one sandbox temp-directory permission error. Repaired the test fixture to its original cutoff and used writable test temporary storage; did not change historical experiment models/results.
- Ledger original 39-row prefixes match their pre-update SHA-256 byte hashes. No historical winning rows, older experiment files or pre-draw artifacts changed.

No code commit, push, deployment, production authority change or live wager was performed.
