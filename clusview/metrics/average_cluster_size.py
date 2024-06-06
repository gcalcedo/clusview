from typing import Any

import numpy as np
from numpy import ndarray

from clusview.metrics.base_metric import BaseMetric


class AverageClusterSize(BaseMetric):
    """
    Average size of clusters.
    """

    def perform_metric(self, **kwargs: Any) -> float:
        clusters: ndarray = kwargs["clusters"]
        if np.all(clusters == -1):
            return 0

        clusters = clusters[clusters != -1]
        unique_clusters, cluster_counts = np.unique(clusters, return_counts=True)
        average_size = np.mean(cluster_counts)
        return average_size
