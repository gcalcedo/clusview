from abc import ABC, abstractmethod
from typing import Iterable


class BaseSampler(ABC):
    """
    Base class for all parameter samplers.

    Attributes:
        parameter_name (str): The name of the parameter being sampled.
        lower_bound (int): The lower bound of the parameter's range.
        upper_bound (int): The upper bound of the parameter's range.
    """

    def __init__(self, parameter_name: str, lower_bound: int, upper_bound: int):
        self.parameter_name = parameter_name
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    @abstractmethod
    def sample_range(self) -> Iterable:
        pass

    def get_sampling_count(self) -> int:
        """
        Returns the number of samples in the parameter's range.

        Returns:
            int: The number of samples in the parameter's range.
        """
        return len(self.sample_range())
