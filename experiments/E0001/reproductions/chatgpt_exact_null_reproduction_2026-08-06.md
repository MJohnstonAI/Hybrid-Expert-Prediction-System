# E0001 Reproduction — Exact Structural Null

**Reproducer:** ChatGPT  
**Date:** 2026-08-06  
**Type:** independent implementation / exact enumeration  
**Status:** reproduction of mathematical baselines, not predictive validation

## Reproduced items

1. Claude's exact per-slot order-statistic HLR probabilities for previous draw `16,24,29,34,38`.
2. Exhaustive `C(50,5)=2,118,760` joint HLR-vector null.
3. Exact fixed-K 5/5 and 4+/5 basket survival probabilities.
4. Corrected six-component gap vector and uniform weak-composition / Dirichlet-Multinomial equivalence.

## Per-slot HLR reproduction

Exact probabilities matched Claude's re-review to rounding:

| Slot | Prev | LOW | REPEAT | HIGH |
|---:|---:|---:|---:|---:|
| 1 | 16 | 0.8467820801 | 0.0218882743 | 0.1313296456 |
| 2 | 24 | 0.7713851498 | 0.0282240556 | 0.2003907946 |
| 3 | 29 | 0.6161556760 | 0.0374653099 | 0.3463790141 |
| 4 | 34 | 0.4403405766 | 0.0412014575 | 0.5184579660 |
| 5 | 38 | 0.2057321263 | 0.0311715343 | 0.7630963394 |

## Joint null reproduction

Exhaustive enumeration returned all 243 possible vectors.

Highest probability vectors:

1. `LLLLH` — 405720 / 2118760 = 0.1914893617
2. `LLLLL` — 358608 / 2118760 = 0.1692537144
3. `LLLHH` — 323760 / 2118760 = 0.1528063584
4. `LLHHH` — 253350 / 2118760 = 0.1195746569
5. `LHHHH` — 170535 / 2118760 = 0.0804881157
6. `HHHHH` — 151070 / 2118760 = 0.0713011384

Frozen committed `HLHHL`:

- count: 336;
- probability: 0.0001585833223;
- probability percent: 0.01585833223%;
- competition rank: 109 / 243.

## Retrospective flow reproduction

| Target | Actual flow | Exact structural-null rank | Exact probability |
|---|---|---:|---:|
| 2026-07-28 | LHHHH | 2 | 0.1098430214 |
| 2026-07-31 | HLHHL | 26 | 0.0069380204 |
| 2026-08-04 | HHLLL | 3 | 0.1387273688 |

This confirms that 2026-07-28 and 2026-08-04 were already highly ranked by IID sorted geometry. Only the 2026-07-31 case materially favors the learned Candidate Lattice rank over the exact-null rank, and it is post-hoc.

## Gap representation reproduction

For `16,24,29,34,38`:

`G = [15,7,4,4,3,12]`.

Sum = 45.

The number of weak compositions of 45 into six nonnegative parts is:

`C(50,5)=2,118,760`.

The Dirichlet-Multinomial PMF with `N=45` and `alpha_i=1` is constant over every such composition, proving equivalence to the uniform legal-line null.

## Fixed basket reproduction

For K=38:

- 5/5 survival = 0.2369036606;
- 4+/5 survival = 0.6549689441.

For the three specific excluded previous-draw numbers `{16,24,29}`, exact probability at least one appears in the next five-number IID draw is:

`1 - C(47,5)/C(50,5) = 0.2760204082`.

## Reproducibility command

Use repository code:

```bash
python scripts/structural_null.py --draw-id 19 --basket-size 13 --basket-size 18 --basket-size 38
```

## Reproduction conclusion

The exact-null calculations are reproduced. This does not validate learned HLR/VVD or gap prediction. It strengthens the requirement that those models demonstrate incremental prospective score improvement beyond the exact structural baseline.
