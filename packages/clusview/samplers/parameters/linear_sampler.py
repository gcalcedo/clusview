from typing import Iterable

from samplers.parameters.base_parameter_sampler import BaseSampler


class LinearSampler(BaseSampler):
    """
    A sampler that generates linearly spaced values within a given range.

    Args:
        parameter_name (str): The name of the parameter being sampled.
        lower_bound (int): The lower bound of the parameter range (inclusive).
        upper_bound (int): The upper bound of the parameter range (inclusive).
        step (int): The step size between consecutive values.

    Returns:
        Iterable: An iterable containing the linearly spaced values within the range.

    Examples:
        >>> sampler = LinearSampler('parameter_name', 0, 10, 2)
        >>> sampler.sample_range()
        [0, 2, 4, 6, 8, 10]
    """

    def __init__(
        self, parameter_name: str, lower_bound: int, upper_bound: int, step: int
    ):
        super().__init__(parameter_name, lower_bound, upper_bound)
        self.step = step

    def sample_range(self) -> Iterable:
        return range(self.lower_bound, self.upper_bound + 1, self.step)
