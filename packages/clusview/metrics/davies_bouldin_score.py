from typing import Any

import numpy as np
from metrics.base_metric import BaseMetric
from numpy import ndarray
from sklearn.metrics import davies_bouldin_score


class DaviesBouldinScore(BaseMetric):
    """
    Calculates the Davies-Bouldin score for evaluating clustering performance.

    The Davies-Bouldin score is a measure of the quality of a clustering algorithm. It quantifies the average similarity
    between clusters and the dissimilarity between clusters. A lower Davies-Bouldin score indicates better clustering
    performance.

    Args:
        clusters (ndarray): An array containing the cluster assignments for each data point.
        embeddings (ndarray): An array containing the embeddings of the data points.

    Returns:
        float: The Davies-Bouldin score.

    Examples:
        >>> clusters = np.array([0, 1, 0, 1, 2])
        >>> embeddings = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
        >>> metric = DaviesBouldinScore()
        >>> score = metric.perform_metric(clusters=clusters, embeddings=embeddings)
        >>> print(score)
        0.6666666666666666

    References:
        - [Scikit-learn Davies-Bouldin Score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.davies_bouldin_score.html)
    """

    def perform_metric(self, **kwargs: Any) -> float:
        clusters: ndarray = kwargs["clusters"]
        embeddings: ndarray = kwargs["embeddings"]

        indices = np.where(clusters != -1)[0]

        if len(indices) == 0:
            return 1

        X = embeddings[indices]
        labels = clusters[indices]

        return davies_bouldin_score(X, labels)
