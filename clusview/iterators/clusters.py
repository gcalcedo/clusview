from itertools import product
from typing import List, NamedTuple
from hdbscan import HDBSCAN


class ParameterRange(NamedTuple):
    """
    Defines a set of possible values for a single parameter.

    ### Args
    - `parameter_name : str`: name of the parameter in the target object.
    - `lower_bound : int`: minimum number in the value range.
    - `upper_bound : int`: maximum number in the value range.
    - `step : int`: rate of change between consecutive values.
    """

    parameter_name: str
    lower_bound: int
    upper_bound: int
    step: int


class HDBSCANIterator:
    """
    Iterates over HDSBCAN setups based on a complete set of combinations
    for a given list of parameter ranges.

    ### Args
    - `parameter_configurations : List[ParameterRange]`: list of parameter ranges.
    """

    def __init__(self, parameter_configurations: List[ParameterRange]) -> None:
        self.parameter_configurations = parameter_configurations

    def generate_combinations(self):
        ranges = [
            range(config.lower_bound, config.upper_bound + 1, config.step)
            for config in self.parameter_configurations
        ]

        for combination in product(*ranges):
            yield combination

    def iterate_configurations(self):
        for combination in self.generate_combinations():
            hdbscan = HDBSCAN()
            for config, value in zip(self.parameter_configurations, combination):
                setattr(hdbscan, config.parameter_name, value)
            yield hdbscan
