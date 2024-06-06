from typing import Any

from numpy import ndarray

from clusview.metrics.base_metric import BaseMetric


class OutlierRatio(BaseMetric):
    """
    Outlier Ratio is the ratio between outliers and total documents.
    """

    def perform_metric(self, **kwargs: Any) -> float:
        clusters: ndarray = kwargs["clusters"]
        outlier_count = (clusters == -1).sum()
        total_count = clusters.size
        outlier_ratio = outlier_count / total_count
        return outlier_ratio
