from bertopic import BERTopic
from numpy import ndarray
from clusview.metrics.metric_combinators import BaseMetric


class OutlierPenalty(BaseMetric):
    """
    Outlier Penalty is the ratio between outliers and total documents multiplied by -1.
    """

    def perform_metric(self, topic_model: BERTopic, embeddings: ndarray) -> float:
        outlier_count = topic_model.get_topic_info().loc[0, "Count"]
        total_count = topic_model.get_topic_info()["Count"].sum()
        outlier_ratio = outlier_count / total_count
        return outlier_ratio * -1
