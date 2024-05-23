from abc import ABC, abstractmethod
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
