from typing import Iterable

from clusview.samplers.parameters.base_parameter_sampler import BaseSampler


class LinearSampler(BaseSampler):
    """
    Linear parameter sampler.
    """

    def __init__(
        self, parameter_name: str, lower_bound: int, upper_bound: int, step: int
    ):
        super().__init__(parameter_name, lower_bound, upper_bound)
        self.step = step

    def sample_range(self) -> Iterable:
        return range(self.lower_bound, self.upper_bound + 1, self.step)
