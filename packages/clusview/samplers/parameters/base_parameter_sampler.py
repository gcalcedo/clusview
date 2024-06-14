from abc import ABC, abstractmethod
from typing import Iterable


class BaseSampler(ABC):
    """
    Base class for all parameter samplers.
    """

    def __init__(self, parameter_name: str, lower_bound: int, upper_bound: int):
        self.parameter_name = parameter_name
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    @abstractmethod
    def sample_range(self) -> Iterable:
        pass

    def get_sampling_count(self) -> int:
        return len(self.sample_range())
