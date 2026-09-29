# E0033 — Oracle-K13 Replacement and Geometry-First Top20 Assembly Stress Test

## Status

`POST-HOC STAGE-ISOLATION / DISCOVERY ONLY`

Evidence classification: `INSUFFICIENT_EVIDENCE`.

Paper trading only.

## Research question

Conditional on HEPS having all five actual Main winners inside a fixed K13, can assembly surface a 4/5 or exact 5/5 combination into a Top-10 or Top-20 slate more reliably than current direct coalition ranking?

## Targets

- 2026-09-01
- 2026-09-04
- 2026-09-08

Main active-era data begin 2026-06-02. Every assembly score for a target uses only draws strictly before that target.

## Oracle-K13 replacement protocol

Start from the actual frozen K13 used for that target. Preserve any true winners already present. Inject every missing true winner. Keep K fixed at 13 by retaining exactly eight of the original K13 non-winners.

To avoid cherry-picking which predicted non-winners are dropped, exhaustively enumerate every valid eight-decoy subset from the original K13 non-winners:

- 2026-09-01: frozen K13 already held 2/5 winners; 165 oracle-adjusted K13 variants.
- 2026-09-04: frozen K13 held 1/5; 495 variants.
- 2026-09-08: frozen K13 held 1/5; 495 variants.

Total: 1,155 oracle-adjusted K13 universes.

This construction gives zero candidate-acquisition credit. It isolates assembly only.

## Assembly arms

### Direct five-line rankers

Within every K13 enumerate all `C(13,5)=1,287` lines and score using target-excluded state:

- E0013 spectral coalition score;
- additive frequency;
- additive recency;
- simple positive-PMI pair score;
- E0022 Dissent-OR.

### Four-node nucleus completion

Enumerate all `C(13,4)=715` four-number nuclei. Rank nuclei with the same score families. For the top nucleus, submit all nine possible fifth-number completions. Use line 10 as the best direct-ranker hedge. For Top-20, add completions of the second-ranked nucleus, deduplicate, and fill any remaining positions from the direct line ranker.

If a nucleus contains 4 true winners, exhaustive completion guarantees exact 5/5 among its nine completions. If it contains 3 true winners, exhaustive completion guarantees at least two 4/5 lines among its nine completions.

### Geometry-first portfolio

Use the accepted E0022 `four_plus_first` Johnson geometry on the full K13. At budget 20 it selects a deterministic 20-line set for 4+/5 winner-state coverage. Reorder the already-selected 20 lines by pre-target rankers without changing membership or coverage. This tests whether ranking can float a covered 4+/5 state upward without sacrificing deterministic Top-20 coverage.

## Random nucleus controls

With 5 winners and 8 decoys inside K13, a uniformly random four-number nucleus has:

- `P(overlap=4) = 5/715 = 0.6993%`;
- `P(overlap>=3) = 85/715 = 11.8881%`.

Two random distinct nuclei have approximately:

- `P(any overlap>=3) = 22.3776%`;
- `P(any overlap=4) = 1.3947%`.

## Primary metrics

- best overlap in Top-10;
- best overlap in Top-20;
- exact 5/5 presence in Top-10 and Top-20;
- first rank at which a 4+/5 line appears;
- exact winning-line direct rank among 1,287;
- best true four-node nucleus rank among 715;
- robustness across all oracle-replacement variants.

## Integrity rules

- target outcome is used only to force the oracle stage-isolation K13 and score results;
- no target outcome enters feature/ranker fitting;
- no K expansion;
- no historical artifact is modified;
- all findings are retrospective discovery and cannot receive prospective predictive credit.