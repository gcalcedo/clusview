from bertopic import BERTopic
import numpy as np
from .metric_combinators import BaseMetric
from sklearn.metrics import silhouette_score


class SilhouetteScore(BaseMetric):
    """
    Silhouette Score is obtained by averaging across the silhouette coefficient of each sample.
    The Silhouette Coefficient is defined for each sample and is composed of two scores:

    - A: The mean distance between a sample and all other points in the same class.
    - B: The mean distance between a sample and all other points in the next nearest cluster.
    """

    def perform_metric(self, topic_model: BERTopic, embeddings: np.ndarray) -> float:
        reduced_embeddings = topic_model.umap_model.transform(embeddings)
        topics = topic_model.topics_
        indices = [index for index, topic in enumerate(topics) if topic != -1]

        if not indices:
            return 0

        X = reduced_embeddings[np.array(indices)]
        labels = [topic for index, topic in enumerate(topics) if topic != -1]

        return silhouette_score(X, labels)
