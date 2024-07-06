from typing import Iterable

import numpy as np

from .base_parameter_sampler import BaseSampler


class GeometricSampler(BaseSampler):
    """
    Generates geometrically spaced values within a given range.

    Args:
        parameter_name (str): The name of the parameter being sampled.
        lower_bound (int): The lower bound of the parameter range.
        upper_bound (int): The upper bound of the parameter range.
        number_of_samples (int): The number of samples to generate.

    Returns:
        Iterable: An iterable containing the geometrically spaced values within the range.

    Examples:
        >>> sampler = GeometricSampler("x", 1, 100, 5)
        >>> sampler.sample_range()
        [1, 3, 10, 31, 10]

        Note that, for a number of samples close to the range size,
        samples may be generated that fall under the same value due to rounding. For example:

        >>> sampler = GeometricSampler("x", 1, 100, 90)
        >>> sampler.sample_range()
        [1, 1, 1, 1, ...]
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
        return np.geomspace(
            self.lower_bound,
            self.upper_bound,
            self.number_of_samples,
            dtype=int,
        )
