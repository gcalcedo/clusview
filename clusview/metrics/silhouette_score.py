from typing import Any

import numpy as np
from numpy import ndarray
from sklearn.metrics import silhouette_score

from clusview.metrics.base_metric import BaseMetric


class SilhouetteScore(BaseMetric):
    """
    Silhouette Score is obtained by averaging across the silhouette coefficient of each sample.
    The Silhouette Coefficient is defined for each sample and is composed of two scores:

    - A: The mean distance between a sample and all other points in the same class.
    - B: The mean distance between a sample and all other points in the next nearest cluster.
    """

    def perform_metric(self, **kwargs: Any) -> float:
        clusters: ndarray = kwargs["clusters"]
        embeddings: ndarray = kwargs["embeddings"]

        indices = np.where(clusters != -1)[0]

        if len(indices) == 0:
            return 0

        X = embeddings[indices]
        labels = clusters[indices]

        return silhouette_score(X, labels)
