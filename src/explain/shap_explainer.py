"""Post-hoc explanation layer for the UEBA anomaly detector's decisions.

TODO: implement SHAP-based feature attribution per flagged decision, and a
plain-language rendering suitable for a non-ML SOC analyst.
"""


def explain_decision(model, x_instance) -> dict:
    raise NotImplementedError


def explanation_fidelity(explanations, ground_truth) -> float:
    """TODO: metric for how well explanations track the model's true
    decision drivers, not just plausibility."""
    raise NotImplementedError
