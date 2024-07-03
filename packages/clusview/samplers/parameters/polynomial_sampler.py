from typing import Iterable

import numpy as np

from .base_parameter_sampler import BaseSampler


class PolynomialSampler(BaseSampler):
    """
    A sampler that generates samples based on a polynomial function.

    Args:
        parameter_name (str): The name of the parameter being sampled.
        lower_bound (int): The lower bound of the parameter range.
        upper_bound (int): The upper bound of the parameter range.
        number_of_samples (int): The number of samples to generate.
        degree (int): The degree of the polynomial function.

    Returns:
        Iterable: A list of unique samples generated by the polynomial function.

    Examples:
        >>> sampler = PolynomialSampler("x", 0, 10, 5, 2)
        >>> samples = sampler.sample_range()
        >>> print(samples)
        [0, 1, 4, 9, 10]
    """

    def __init__(
        self,
        parameter_name: str,
        lower_bound: int,
        upper_bound: int,
        number_of_samples: int,
        degree: int,
    ):
        super().__init__(parameter_name, lower_bound, upper_bound)
        self.number_of_samples = number_of_samples
        self.degree = degree

    def sample_range(self) -> Iterable:
        num_samples = self.number_of_samples
        start = np.power(self.lower_bound, 1 / self.degree)
        end = np.power(self.upper_bound, 1 / self.degree)
        samples = np.linspace(start, end, num_samples) ** self.degree
        samples = np.round(samples).astype(int)
        unique_samples = sorted(set(samples))
        return unique_samples
