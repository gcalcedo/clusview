from typing import Any

from numpy import ndarray

from metrics.base_metric import BaseMetric


class OutlierRatio(BaseMetric):
    """
    Calculates the outlier ratio of a clustering result.

    Args:
        clusters (ndarray): An array representing the clustering result, where -1 indicates outliers.

    Returns:
        float: The outlier ratio, defined as the ratio of outliers to the total number of data points.

    Examples:
        >>> clusters = np.array([0, 1, 0, -1, 1, 0, -1, -1])
        >>> metric = OutlierRatio()
        >>> metric.perform_metric(clusters=clusters)
        0.375
    """

    def perform_metric(self, **kwargs: Any) -> float:
        clusters: ndarray = kwargs["clusters"]
        outlier_count = (clusters == -1).sum()
        total_count = clusters.size
        outlier_ratio = outlier_count / total_count
        return outlier_ratio
