# E0002 Reproductions

Reproductions should be added as separate artifacts and identify one of:

- `code_reproduction` — same implementation and declared seed/data;
- `independent_implementation` — new code from the written protocol;
- `conceptual_replication` — different implementation testing the same evolutionary-search thesis.

Minimum reproduction checks:

1. verify the compressed training snapshot against `data/manifest.json`;
2. run the test suite;
3. reproduce the deterministic bootstrap with seed `20260807`;
4. confirm the champion is selected on full discovery before validation is evaluated;
5. report any result difference rather than overwriting the originating result.
