from bertopic import BERTopic
from numpy import ndarray

from clusview.metrics.base_metric import BaseMetric


class AverageTopicSize(BaseMetric):
    """
    Average size of topics.
    """

    def perform_metric(self, topic_model: BERTopic, embeddings: ndarray) -> float:
        topic_df = topic_model.get_topic_info()
        topic_df = topic_df[topic_df["Topic"] != -1]
        if topic_df.empty:
            return 0
        else:
            return topic_df["Count"].mean()
