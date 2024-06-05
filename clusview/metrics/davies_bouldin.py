import numpy as np
from bertopic import BERTopic
from sklearn.metrics import davies_bouldin_score

from clusview.metrics.base_metric import BaseMetric


class DaviesBouldin(BaseMetric):
    """
    Davies-Bouldin score metric.

    The Davies-Bouldin score is a measure of the average similarity between each cluster and its most similar cluster,
    taking into account both the scatter within each cluster and the separation between clusters.
    It is defined as the average of the ratio of the within-cluster scatter to the between-cluster separation.

    The score is lower when clusters are well-separated and have low intra-cluster variance,
    indicating better clustering performance.

    Implementation based on scikit-learn:
    [scikit-learn documentation](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.davies_bouldin_score.html)
    """

    def perform_metric(self, topic_model: BERTopic, embeddings: np.ndarray) -> float:
        reduced_embeddings = topic_model.umap_model.transform(embeddings)
        topics = topic_model.topics_
        indices = [index for index, topic in enumerate(topics) if topic != -1]

        if not indices:
            return 0

        X = reduced_embeddings[np.array(indices)]
        labels = [topic for index, topic in enumerate(topics) if topic != -1]

        return davies_bouldin_score(X, labels)
