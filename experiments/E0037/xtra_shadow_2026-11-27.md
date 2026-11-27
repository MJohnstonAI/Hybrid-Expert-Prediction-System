# E0037 XTRA Cold-Bucket Prospective Shadow — 2026-11-27

**Frozen before target result.**
**Production weight:** 0
**Authority:** shadow only

## Frozen method

Primary shadow feature: coordinate was absent from the previous **8 XTRA draws**.

Current fitted discovery coefficient:
`beta = +0.385`

Positive beta favors unseen coordinates. This coefficient is discovery-fitted and has zero confirmation credit; it is frozen only for prospective scoring.

## Current XTRA unseen-W8 pool

18 coordinates:

`2,3,8,9,13,14,18,22,25,30,31,34,35,38,41,46,48,50`

## Cold K13 diagnostic

Select the 13 longest-absent coordinates within the unseen pool:

`2,3,8,9,13,22,25,30,35,38,41,46,48`

Age ordering used internally:
- 30: unseen across all 51 active XTRA draws;
- 22: 17 draws absent;
- 9,25: 15;
- 2,38,46: 14;
- 41,48: 13;
- 13,35: 12;
- 3,8: 11.

This K13 is **not** the official XTRA K13 and must not replace it.

## Prospective scoring

After the 2026-11-27 XTRA result:
- count winning main numbers in the 18-number unseen pool;
- compare with conditional IID expectation `5*18/50 = 1.8`;
- count hits in the frozen cold K13;
- score UNSEEN_W8 weighted legal-line probability against uniform;
- append result without changing W=8 or beta.
