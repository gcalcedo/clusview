from typing import Any

from numpy import ndarray

from .base_metric import BaseMetric


class ClusterCount(BaseMetric):
    """
    Calculates the count of unique clusters in a given set of clusters.

    Args:
        clusters (ndarray): An array containing the cluster assignments.

    Returns:
        float: The count of unique clusters.

    Examples:
        >>> clusters = [0, 1, 0, 2, 1, 2]
        >>> metric = ClusterCount()
        >>> count = metric.perform_metric(clusters=clusters)
        >>> print(count)
        3
    """

    def perform_metric(self, **kwargs: Any) -> float:
        clusters: ndarray = kwargs["clusters"]
        return len(set(clusters))
