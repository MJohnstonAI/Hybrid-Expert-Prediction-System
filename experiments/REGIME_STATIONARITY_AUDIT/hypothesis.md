# REGIME_STATIONARITY_AUDIT — Hypothesis

Origin: Claude (Anthropic) contribution supplied 2026-08-06.

## Original concern

The canonical ledger historically encoded every row as `regime="mechanical_50_16"`. Claude argued that this conflated fixed PowerBall pool rules with the possibility of a mid-ledger draw-mechanism transition, and proposed investigating a candidate boundary around 2026-06-22.

The methodological claim was broader than the date-specific claim:

> A walk-forward training window can be temporally clean but still mix distinct generating mechanisms, so target-leakage protection alone is insufficient.

## Questions under review

1. Is there evidence of a PowerBall-specific mechanical-to-electronic transition on or around 2026-06-22?
2. Does the canonical data model incorrectly conflate game format with draw method?
3. Does HEPS need explicit draw-method/machine metadata and a stationarity diagnostic?
4. Should physical experts be required to disclose machine/method mixing in their training windows?

## Predeclared guardrail

No boundary date may be selected by scanning draw outcomes for the split that produces the largest difference. Mechanism boundaries must come from external operator/equipment evidence.
