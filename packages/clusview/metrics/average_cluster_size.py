from typing import Any

import numpy as np
from metrics.base_metric import BaseMetric
from numpy import ndarray


class AverageClusterSize(BaseMetric):
    """
    Calculates the average size of clusters.

    This metric calculates the average size of clusters by counting the number of elements in each cluster and
    taking the mean of those counts.

    Args:
        clusters (ndarray): An array containing the cluster assignments for each element.

    Returns:
        float: The average size of clusters.

    Examples:
        >>> clusters = np.array([0, 0, 1, 1, 1, 2, 2, 2, 2])
        >>> metric = AverageClusterSize()
        >>> result = metric.perform_metric(clusters=clusters)
        >>> print(result)
        3.0
    """

    def perform_metric(self, **kwargs: Any) -> float:
        clusters: ndarray = kwargs["clusters"]
        if np.all(clusters == -1):
            return 0

        clusters = clusters[clusters != -1]
        unique_clusters, cluster_counts = np.unique(clusters, return_counts=True)
        average_size = np.mean(cluster_counts)
        return average_size
