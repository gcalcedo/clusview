from abc import ABC, abstractmethod
from typing import Any


class BaseMetric(ABC):
    """
    Base class for metrics.
    """

    @abstractmethod
    def perform_metric(self, **kwargs: Any) -> float:
        """
        Performs the specification of this metric.
        """
        pass
