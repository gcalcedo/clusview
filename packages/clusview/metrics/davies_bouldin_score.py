from typing import Any

import numpy as np
from numpy import ndarray
from sklearn.metrics import davies_bouldin_score

from clusview.metrics.base_metric import BaseMetric


class DaviesBouldinScore(BaseMetric):
    """
    Davies-Bouldin score metric.

    The Davies-Bouldin score is a measure of the average similarity between each cluster and its most similar cluster,
    taking into account both the scatter within each cluster and the separation between clusters.
    It is defined as the average of the ratio of the within-cluster scatter to the between-cluster separation.

    The score is lower when clusters are well-separated and have low intra-cluster variance,
    indicating better clustering performance.

    Implementation based on scikit-learn:
    [scikit-learn documentation](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.davies_bouldin_score.html)
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
