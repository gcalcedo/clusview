from typing import Iterable

import numpy as np

from clusview.samplers.parameters.base_parameter_sampler import BaseSampler


class PolynomialSampler(BaseSampler):
    """
    Polynomial parameter sampler of any degree.
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
