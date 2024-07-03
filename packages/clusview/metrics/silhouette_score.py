from typing import Any

import numpy as np
from numpy import ndarray
from sklearn.metrics import silhouette_score

from .base_metric import BaseMetric


class SilhouetteScore(BaseMetric):
    """
    Calculate the Silhouette Score for clustering evaluation.

    The Silhouette Score is a measure of how well each data point in a clustering
    algorithm is matched to its own cluster compared to other clusters. It provides
    a way to assess the quality of a clustering solution by quantifying the
    separation between clusters and the compactness of data points within clusters.

    Args:
        clusters (ndarray): The cluster assignments for each data point.
        embeddings (ndarray): The embeddings of the data points.

    Returns:
        float: The Silhouette Score, ranging from -1 to 1. A higher score indicates
        better clustering quality, where values close to 1 indicate well-separated
        clusters and values close to -1 indicate overlapping clusters.

    Examples:
        >>> clusters = np.array([0, 1, 0, 1, 1])
        >>> embeddings = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
        >>> metric = SilhouetteScore()
        >>> score = metric.perform_metric(clusters=clusters, embeddings=embeddings)
        >>> print(score)
        0.26666666666666666

    References:
        - [Scikit-learn Silhouette Score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.silhouette_score.html)
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
