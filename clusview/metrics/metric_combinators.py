from abc import ABC, abstractmethod
from typing import List, Tuple

from bertopic import BERTopic
from numpy import ndarray


class BaseMetric(ABC):
    """
    Base class for metrics.
    """

    @abstractmethod
    def perform_metric(self, topic_model: BERTopic, embeddings: ndarray) -> float:
        """
        Performs the specification of this metric.
        """
        pass


class BaseCombinator(ABC):
    """
    Base class for metric combinators.
    """

    @abstractmethod
    def combine(self, topic_model: BERTopic, embeddings: ndarray) -> float:
        """
        Performs metric on `topic_model` and combines them.
        """
        pass


class LinearCombinator(BaseCombinator):
    """
    Linearly combines metrics.

    ### Args
    - `weighted_metrics`: list of tuples containing a metric and its corresponding weight.

    ### Returns
    - `float`: linear combination of the `weighted_metrics`.
    """

    def __init__(self, weighted_metrics: List[Tuple[BaseMetric, float]]) -> None:
        self.weighted_metrics = weighted_metrics
        self.normalize()

    def normalize(self):
        total_weight = sum(weight for _, weight in self.weighted_metrics)
        normalized_weights = [
            (metric, weight / total_weight) for metric, weight in self.weighted_metrics
        ]
        self.weighted_metrics = normalized_weights

    def combine(self, topic_model: BERTopic, embeddings: ndarray) -> float:
        combined_value = 0.0
        for metric, weight in self.weighted_metrics:
            metric_value = metric.perform_metric(topic_model, embeddings)
            combined_value += metric_value * weight

        return combined_value
