from itertools import product
from typing import List

from hdbscan import HDBSCAN

from clusview.samplers.parameters.base_parameter_sampler import BaseSampler


class HDBSCANSampler:
    """
    Iterates over HDSBCAN configurations based on a complete set of combinations
    for a given list of parameter samplers.

    ### Args
    - `parameter_samplers : List[BaseSampler]`: list of parameter samplers.
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
