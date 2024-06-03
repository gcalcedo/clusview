from bertopic import BERTopic
from numpy import ndarray

from clusview.metrics.base_metric import BaseMetric


class TopicCount(BaseMetric):
    """
    Topic Count is the number of topics generated, including the outliers topic.
    """

    def perform_metric(self, topic_model: BERTopic, embeddings: ndarray) -> float:
        return len(topic_model.get_topic_info().index)
