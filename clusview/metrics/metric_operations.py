from bertopic import BERTopic
from numpy import ndarray

from clusview.metrics.metric_combinators import BaseMetric


class SignChange(BaseMetric):
    """
    Flips the sign of the input metric.
    """

    def __init__(self, metric: BaseMetric) -> None:
        self.metric = metric

    def perform_metric(self, topic_model: BERTopic, embeddings: ndarray) -> float:
        return self.metric.perform_metric(topic_model, embeddings) * -1
