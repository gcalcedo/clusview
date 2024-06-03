from bertopic import BERTopic
from numpy import ndarray

from clusview.metrics.base_metric import BaseMetric


class OutlierRatio(BaseMetric):
    """
    Outlier Ratio is the ratio between outliers and total documents.
    """

    def perform_metric(self, topic_model: BERTopic, embeddings: ndarray) -> float:
        topic_info = topic_model.get_topic_info()
        outlier_info = topic_info.loc[0]

        outlier_count = outlier_info["Count"] if outlier_info["Topic"] == -1 else 0
        total_count = topic_info["Count"].sum()

        outlier_ratio = outlier_count / total_count

        return outlier_ratio
