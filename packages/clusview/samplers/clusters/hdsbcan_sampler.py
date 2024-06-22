from itertools import product
from typing import List

from hdbscan import HDBSCAN
from samplers.parameters.base_parameter_sampler import BaseSampler


class HDBSCANSampler:
    """
    A class that generates configurations for HDBSCAN clustering algorithm by sampling parameters.

    Args:
        parameter_samplers (List[BaseSampler]): A list of parameter samplers used to sample the parameters for HDBSCAN.

    Returns:
        None

    Examples:
        >>> sampler1 = LinearSampler(...)
        >>> sampler2 = PolynomialSampler(...)
        >>> sampler3 = LinearSampler(...)

        >>> sampler = HDBSCANSampler([sampler1, sampler2, sampler3])

        >>> for configuration in sampler.iterate_configurations():
        ...     # Perform operations with the generated configuration
        ...     ...
    """

    def __init__(self, parameter_samplers: List[BaseSampler]) -> None:
        self.parameter_samplers = parameter_samplers

    def generate_combinations(self):
        samplings = [sampler.sample_range() for sampler in self.parameter_samplers]

        for combination in product(*samplings):
            yield combination

    def iterate_configurations(self):
        for combination in self.generate_combinations():
            hdbscan = HDBSCAN()
            for config, value in zip(self.parameter_samplers, combination):
                setattr(hdbscan, config.parameter_name, value)
            yield hdbscan
