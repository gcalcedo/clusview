from typing import Iterable

import numpy as np

from .base_parameter_sampler import BaseSampler


class LinearSampler(BaseSampler):
    """
    Generates linearly spaced values within a given range.

    Args:
        parameter_name (str): The name of the parameter being sampled.
        lower_bound (int): The lower bound of the parameter range (inclusive).
        upper_bound (int): The upper bound of the parameter range (inclusive).
        number_of_samples (int): The number of samples to generate.

    Returns:
        Iterable: An iterable containing the linearly spaced values within the range.

    Examples:
        >>> sampler = LinearSampler('x', 0, 10, 6)
        >>> sampler.sample_range()
        [0, 2, 4, 6, 8, 10]
    """

    def __init__(
        self,
        parameter_name: str,
        lower_bound: int,
        upper_bound: int,
        number_of_samples: int,
    ):
        super().__init__(parameter_name, lower_bound, upper_bound, number_of_samples)

    def sample_range(self) -> Iterable:
        return np.linspace(
            self.lower_bound, self.upper_bound, self.number_of_samples, dtype=int
        )
