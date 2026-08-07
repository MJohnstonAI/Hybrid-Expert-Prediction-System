# HEPS Per-Draw Cycles

Every target draw should have a self-contained cycle directory:

```text
cycles/YYYY-MM-DD/
  cycle_manifest.json
  pre_draw/
    architecture_snapshot.json
    dataset_snapshot.json
    expert_outputs/
    slot_funnel.json
    combination_ranking.json
    prediction_slate.json
  post_draw/
    actual_result.json
    scorecard.json
    expert_attribution.json
    counterfactual_ranks.json
    physics_of_failure.md
    improvement_proposals.md
```

Not every experiment needs every large artifact committed; very large generated universes may be represented by hashes, summaries, compressed artifacts, or reproducible generation parameters. The exact frozen final slate and the information needed to reproduce its generation must be retained.

## Pre-draw freeze

Before the draw result is known, freeze:

- target date;
- dataset cutoff and manifest/hash;
- architecture ID/version;
- expert registry/weights version;
- experiment/challenger IDs used;
- slot forecasts and candidate baskets where applicable;
- ranking parameters;
- final paper-trading slate;
- generation timestamp.

Once frozen, do not regenerate these artifacts using the known outcome.

## Post-draw analysis

After the actual result is appended and validated:

1. score the exact frozen slate;
2. trace actual winning coordinates through each stage;
3. record exact winning-line rank where the line existed;
4. identify the first stage at which any winning coordinate/line was lost;
5. compute expert attribution/counterfactuals where feasible;
6. write Physics of Failure;
7. open new questions or experiments rather than directly retuning architecture from one miss.

## Learning speeds

- Fast deterministic state updates may occur after every draw.
- Medium parameter updates require a frozen learning rule.
- Slow architecture changes require promotion review.

## Legacy outputs

Existing `outputs/predictions/` and `outputs/post_game/` files remain valid historical artifacts. New cycles should reference them if they are the authoritative frozen artifacts for a target.