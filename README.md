# Explainable Zero-Trust Anomaly Detection

PhD portfolio project — Tier III. Detect insider-threat and lateral-movement anomalies,
and make the model justify every flag it raises before it reaches a zero-trust policy
decision.

## The gap

Industry coverage for 2026 consistently pairs zero-trust and identity security with
AI-driven behavioral analytics, but flags explainability as the unresolved half of that
story — a SOC analyst won't act on a flag they can't audit, and a zero-trust policy
engine needs a decision an auditor can reconstruct.

## The project

- Build a user/entity behavior anomaly detector over a public insider-threat dataset
- Feed its output into a simple zero-trust policy simulation (grant / challenge / deny)
- Wrap every decision in a post-hoc explanation (SHAP or attention-based) readable by a
  non-ML analyst
- Evaluate on both detection accuracy and explanation fidelity, not accuracy alone

## Status

Scaffold stage — pipeline stages and interfaces defined, implementations pending.

## Repository layout

```
src/
  detection/  UEBA anomaly detection model
  policy/     zero-trust grant/challenge/deny simulator
  explain/    SHAP / attention-based explanation layer
data/         insider-threat dataset (not committed)
```

## Roadmap

1. Load a public insider-threat / UEBA dataset and establish a baseline anomaly detector
2. Wire detector output into the zero-trust policy simulator
3. Add the explanation layer; define an explanation-fidelity metric
4. Evaluate detection accuracy and explanation fidelity together, not separately

## Related work

- 2026 industry trend coverage on zero-trust + AI-driven behavioral analytics
  (identity security, UEBA)
- AI ethics / explainability requirements increasingly cited alongside zero-trust
  architecture in 2026 cybersecurity trend analyses

## License

MIT
