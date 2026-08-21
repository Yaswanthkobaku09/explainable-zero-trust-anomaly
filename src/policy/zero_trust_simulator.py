"""Zero-trust policy simulator: maps an anomaly score to a grant/challenge/deny
decision under configurable thresholds.

TODO: implement threshold-based policy logic and a decision log format that
the explanation layer can attach to.
"""


def decide(anomaly_score: float, thresholds: dict) -> str:
    raise NotImplementedError
