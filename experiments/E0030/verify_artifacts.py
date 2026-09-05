"""Verify saved replay consistency without redoing portfolio search."""
import hashlib
import json
import math
import sys
from prototype import ROOT, HERE, N, TOTAL, BUDGET, digest, forecast, load_game, coverage, basket_mass


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


result = json.loads((HERE / "results.json").read_text())
assert result["source_sha256"] == sha(HERE / "prototype.py")
assert result["protocol_sha256"] == sha(HERE / "protocol.yaml")
checked = 0
for game, report in result["games"].items():
    rows, audit = load_game(game)
    assert report["audit"]["sha256"] == audit["sha256"]
    logs = [math.log(x) for x in (0.8, 0.1, 0.1)]
    assert len(report["records"]) == 19
    for i, record in enumerate(report["records"], 5):
        frozen, target = record["frozen"], rows[i]
        assert digest(frozen) == record["freeze_sha256"]
        assert digest(rows[:i]) == frozen["history_sha256"]
        assert target["draw_date"] == record["date"]
        assert rows[i - 1]["draw_date"] < record["date"]
        models, model, _ = forecast(rows[:i], logs)
        assert frozen["probability_weights"] == model.weights
        assert frozen["marginals"] == model.marginals
        assert math.isclose(sum(frozen["marginals"]), 5)
        basket = set(frozen["joint_K13"]["basket"])
        assert len(basket) == 13
        assert math.isclose(basket_mass(model, basket), frozen["joint_K13"]["four_plus_mass"])
        winner = set(target["main_numbers"])
        assert len(winner & basket) == record["joint_K13_hits"]
        for name, lines in frozen["portfolios"].items():
            assert len(lines) == BUDGET == len({tuple(line) for line in lines})
            assert all(len(set(line)) == 5 and line == sorted(line) and min(line) >= 1 and max(line) <= N for line in lines)
            score = record["portfolio_scores"][name]
            assert score["best_hits"] == max(len(winner & set(line)) for line in lines)
            assert math.isclose(score["null_four_plus_mass"], len(coverage(lines)) / TOTAL)
        for name, component in zip(("uniform", "frequency", "recency", "mixture"), models + [model]):
            assert math.isclose(record["losses"][name]["log_loss"], -math.log(component.probability(target["main_numbers"])))
        logs = [a + math.log(m.probability(target["main_numbers"])) for a, m in zip(logs, models)]
        checked += 1
paths = sorted((ROOT / "scripts").glob("*.py")) + [HERE / "prototype.py", HERE / "test_prototype.py", HERE / "protocol.yaml"]
evidence = {"status": "passed", "replay_targets_verified": checked, "python": sys.version,
            "source_sha256": {str(p.relative_to(ROOT)): sha(p) for p in paths},
            "results_sha256": sha(HERE / "results.json"), "ledger_values_unchanged": True,
            "independent_reproduction": False}
(HERE / "artifact_verification.json").write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"status": "passed", "replay_targets_verified": checked, "ledger_values_unchanged": True}))
