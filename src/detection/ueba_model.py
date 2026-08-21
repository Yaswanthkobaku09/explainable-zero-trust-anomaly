"""User/entity behavior anomaly detector.

TODO: implement feature extraction over session/access logs and an anomaly
scoring model (e.g., isolation forest or autoencoder reconstruction error).
"""


class UEBAAnomalyDetector:
    def fit(self, x_train):
        raise NotImplementedError

    def score(self, x):
        raise NotImplementedError
