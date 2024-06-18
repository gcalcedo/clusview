from typing import Any

import numpy as np
from numpy import ndarray
from sklearn.metrics import v_measure_score

from metrics.base_metric import BaseMetric


class VMeasureScore(BaseMetric):
    """
    V-Measure Score metric implementation.

    The V-Measure Score is a metric used to evaluate the quality of clustering results.
    It measures the homogeneity and completeness of the clustering results by computing
    the harmonic mean of these two measures.

    The homogeneity score measures the extent to which each cluster contains only samples
    from a single class. A perfectly homogeneous clustering assigns all samples from the
    same class to the same cluster.

    The completeness score measures the extent to which all samples from the same class
    are assigned to the same cluster. A perfectly complete clustering assigns all samples
    from the same class to the same cluster.

    The V-Measure Score combines these two measures into a single score that ranges from 0 to 1.
    A score of 1 indicates a perfect clustering, while a score of 0 indicates a completely random
    clustering.

    Args:
        groundtruth_clusters (ndarray): The ground truth labels or clusters.
        beta (float): The weight of recall in the harmonic mean.

    Returns:
        float: The V-Measure Score.

    Examples:
        >>> clusters = np.array([0, 0, 1, 1, 2, 2])
        >>> groundtruth = np.array([0, 0, 1, 1, 1, 2])
        >>> metric = VMeasureScore(groundtruth_clusters=groundtruth, beta=1.0)
        >>> metric.perform_metric(clusters=clusters)
        0.739667376800759

    References:
        - [Scikit-learn V-Measure Score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.v_measure_score.html)
    """

    def __init__(self, groundtruth_clusters: ndarray, beta: float = 1.0) -> None:
        super().__init__()
        self.beta = beta
        self.groundtruth_clusters = groundtruth_clusters

    def perform_metric(self, **kwargs: Any) -> float:
        clusters: ndarray = kwargs["clusters"]

        indices = np.where(clusters != -1)[0]

        if len(indices) == 0:
            return 0

        labels = clusters[indices]
        groundtruth_labels = self.groundtruth_clusters[indices]

        return v_measure_score(groundtruth_labels, labels, beta=self.beta)
