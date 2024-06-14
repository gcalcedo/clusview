from typing import Any

from numpy import ndarray

from clusview.metrics.base_metric import BaseMetric


class ClusterCount(BaseMetric):
    """
    Cluster Count is the number of topics generated, including the outliers topic.
    """

    def perform_metric(self, **kwargs: Any) -> float:
        clusters: ndarray = kwargs["clusters"]
        return len(set(clusters))
