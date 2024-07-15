"""The Metric Maps module (mmaps) provides a set of functions to generate, manipulate,
and compare multi-dimensional matrices representing single-value metric measurements
across a Cartesian product space of hyperparameters."""

import numpy as np
import polars as pl
import sklearn.metrics
from scipy.interpolate import griddata
from scipy.ndimage import gaussian_filter


class MetricMap:
    """Multi-dimensional matrix representing single-value metric measurements across a
    Cartesian product space of hyperparameters.

    Parameters
    ---
    sampling (`pl.DataFrame`): Sampling of hyperparameters and their corresponding metric values.
    Must adhere to the following shape, where all columns except the last one are hyperparameters
    and the last one is the metric value.

    >>> sampling
    ┌─────────┬─────────┬─────┬──────────┐
    │ param_1 ┆ param_2 ┆ ... ┆ metric_X │
    │ ------- ┆ ------- ┆ --- ┆ -------- │
    │ i64     ┆ i64     ┆ i64 ┆ f64      │
    ╞═════════╪═════════╪═════╪══════════╡
    │ 0       ┆ 0       ┆ ... ┆ 0.1      │
    │ 0       ┆ 1       ┆ ... ┆ 0.2      │
    │ ...     ┆ ...     ┆ ... ┆ ...      │
    └─────────┴─────────┴─────┴──────────┘

    Each row represents a single sample for a given set of hyperparameters.

    Missing values are linearly interpolated to form a complete grid that spans the entire
    hyperparameter space, defined by the minimum and maximum values of each hyperparameter.
    This allows for sampling across the space, not having to compute the metric for every
    possible combination.

    If `sampling` is `None`, an empty one-dimensional metric map is created.
    >>> metric_map = MetricMap()
    >>> metric_map.mapping
    []
    >>> metric_map.metric_name
    "Empty"

    Examples
    ---
    >>> sampling = pl.DataFrame(
    ...     {
    ...         "param_1": [0, 0, 0, 1, 1, 1, 2, 2, 2],
    ...         "param_2": [0, 1, 2, 0, 1, 2, 0, 1, 2],
    ...         "metric_X": [0.1, 0.2, 0.3, 0.2, 0.5, 0.4, 0.3, 0.2, 0.1],
    ...     }
    ... )
    ┌─────────┬─────────┬──────────┐
    │ param_1 ┆ param_2 ┆ metric_X │
    │ ------- ┆ ------- ┆ -------- │
    │ i64     ┆ i64     ┆ f64      │
    ╞═════════╪═════════╪══════════╡
    │ 0       ┆ 0       ┆ 0.1      │
    │ 0       ┆ 1       ┆ 0.2      │
    │ 0       ┆ 2       ┆ 0.3      │
    │ 1       ┆ 0       ┆ 0.2      │
    │ 1       ┆ 1       ┆ 0.5      │
    │ 1       ┆ 2       ┆ 0.4      │
    │ 2       ┆ 0       ┆ 0.3      │
    │ 2       ┆ 1       ┆ 0.2      │
    │ 2       ┆ 2       ┆ 0.1      │
    └─────────┴─────────┴──────────┘

    >>> metric_map = MetricMap(sampling)
    >>> metric_map.mapping
    [[0.1, 0.2, 0.3]
     [0.2, 0.5, 0.2]
     [0.3, 0.4, 0.1]]


    >>> metric_map.metric_name
    "metric_X"

    Fields
    ---
    - mapping (`np.ndarray`): The multi-dimensional matrix representing the metric values.
    - metric_name (`str`): The name of the metric column in the sampling.

    Methods
    ---
    - `normalize()` -> `tuple[float, float]`: Normalize the metric map to the range [0, 1].
    - `smooth(passes: int, sigma: float)` -> `None`: Smooth the metric map using a Gaussian filter.
    """

    def __init__(self, sampling: pl.DataFrame | None = None):
        if sampling is None:
            self.mapping = np.array([])
            self.metric_name = "Empty"
            return

        number_of_cols = sampling.width

        sampled_ranges = []
        for col in sampling.columns:
            if col == sampling.columns[number_of_cols - 1]:
                self.metric_name = col
                continue
            sampled_ranges.append(
                slice(sampling[col].min(), sampling[col].max() + 1, 1)
            )

        points = sampling.select(pl.exclude(sampling.columns[-1])).to_numpy()
        metric_values = sampling.select(pl.nth(number_of_cols - 1)).to_numpy().flatten()

        self.mapping = griddata(
            points, metric_values, tuple(np.mgrid[sampled_ranges]), method="linear"
        )

    def normalize(self) -> tuple[float, float]:
        """Normalize the metric map to the range [0, 1].

        Returns
        ---
        - `tuple[float, float]`: The minimum and maximum values of the metric map before normalization.

        Examples
        ---
        >>> metric_map.mapping
        [[1.0, 2.0, 3.0]
         [4.0, 5.0, 6.0]]
        >>> minimun, maximum = metric_map.normalize()
        >>> metric_map.mapping
        [[0. , 0.2, 0.4]
         [0.6, 0.8, 1. ]]
        >>> minimum
        1
        >>> maximum
        6
        """

        map_min = np.min(self.mapping)
        map_max = np.max(self.mapping)

        if map_max == map_min:
            return map_max, map_min

        self.mapping = (self.mapping - np.min(self.mapping)) / (
            np.max(self.mapping) - np.min(self.mapping)
        )

        return map_min, map_max

    def smooth(self, passes: int, sigma: float) -> np.ndarray:
        """Smooth the metric map using a Gaussian filter.

        This is sensible for reducing noise when the metric map has been built
        from a sparse sampling of hyperparameters, or when only a limited number
        of embeddings have been used for each set of hyperparameter values.

        Parameters
        ---
        - passes (`int`): The number of times to apply the filter.
        - sigma (`float`): The standard deviation of the Gaussian kernel.

        Returns
        ---
        - `np.ndarray`: The original metric map before smoothing.

        Examples
        ---
        >>> metric_map.mapping
        [[1.0, 2.0, 3.0]
         [4.0, 5.0, 6.0]]
        >>> old_mapping = metric_map.smooth_metric_map(1, 1)
        >>> metric_map.mapping
        [[1. , 2. , 3. ]
         [3.5, 4.5, 5.5]]
        >>> old_mapping
        [[1.0, 2.0, 3.0]
         [4.0, 5.0, 6.0]]
        """
        old_mapping = self.mapping.copy()

        for _ in range(passes):
            self.mapping = gaussian_filter(self.mapping, sigma=sigma)

        return old_mapping


#############################
### METRIC MAP OPERATIONS ###
#############################
def total_distance(metric_map_A: MetricMap, metric_map_B: MetricMap) -> float:
    """Total distance between two metric maps.

    Measured as the sum of the absolute
    differences between the two metric maps, using Euclidean distance.

    Parameters
    ---
    - metric_map_A (`MetricMap`): The first metric map to compare.
    - metric_map_B (`MetricMap`): The second metric map to compare.

    Returns
    ---
    - `float`: The total distance between the two metric maps.

    Examples
    ---
    >>> metric_map_1.mapping
    [[1.0, 2.0, 3.0]
     [4.0, 5.0, 6.0]]
    >>> metric_map_2.mapping
    [[2.0, 3.0, 4.0]
     [5.0, 6.0, 7.0]]
    >>> total_distance(metric_map_1, metric_map_2)
    6.0
    """

    return np.sum(np.abs(metric_map_A.mapping - metric_map_B.mapping))


def average_distance(metric_map_A: MetricMap, metric_map_B: MetricMap) -> float:
    """Average distance between two metric maps.

    Measured as the mean of the absolute
    differences between the two metric maps, using Euclidean distance.

    Parameters
    ---
    - metric_map_A (`MetricMap`): The first metric map to compare.
    - metric_map_B (`MetricMap`): The second metric map to compare.

    Returns
    ---
    - `float`: The average distance between the two metric maps.

    Examples
    ---
    >>> metric_map_1.mapping
    [[1.0, 2.0, 3.0]
     [4.0, 5.0, 6.0]]
    >>> metric_map_2.mapping
    [[2.0, 3.0, 4.0]
     [5.0, 6.0, 7.0]]
    >>> average_distance(metric_map_1, metric_map_2)
    1.0
    """

    return np.mean(np.abs(metric_map_A.mapping - metric_map_B.mapping))


def max_distance(metric_map_A: MetricMap, metric_map_B: MetricMap) -> float:
    """Maximum distance between two metric maps.

    Measured as the maximum of the absolute
    differences between the two metric maps, using Euclidean distance.

    Parameters
    ---
    - metric_map_A (`MetricMap`): The first metric map to compare.
    - metric_map_B (`MetricMap`): The second metric map to compare.

    Returns
    ---
    - `float`: The maximum distance between the two metric maps.

    Examples
    ---
    >>> metric_map_1.mapping
    [[1.0, 2.0, 3.0]
     [4.0, 5.0, 6.0]]
    >>> metric_map_2.mapping
    [[4.0, 0.0, 2.0]
     [3.0, 6.0, 6.0]]
    >>> max_distance(metric_map_1, metric_map_2)
    3.0
    """

    return np.max(np.abs(metric_map_A.mapping - metric_map_B.mapping))


def mean_squared_error(metric_map_A: MetricMap, metric_map_B: MetricMap) -> float:
    """Mean squared error between two metric maps.

    Parameters
    ---
    - metric_map_A (`MetricMap`): The first metric map to compare.
    - metric_map_B (`MetricMap`): The second metric map to compare.

    Returns
    ---
    - `float`: The mean squared error between the two metric maps.

    Examples
    ---
    >>> metric_map_1.mapping
    [[1.0, 2.0, 3.0]
     [4.0, 5.0, 6.0]]
    >>> metric_map_2.mapping
    [[2.0, 3.0, 4.0]
     [5.0, 6.0, 7.0]]
    >>> mean_squared_error(metric_map_1, metric_map_2)
    1.0
    """

    return sklearn.metrics.mean_squared_error(
        metric_map_A.mapping, metric_map_B.mapping
    )


def linear_combination(metric_maps: list[MetricMap], weights: list[float]) -> MetricMap:
    """Linear combination of multiple metric maps.

    Parameters
    ---
    - metric_maps (`list[MetricMap]`): The metric maps to combine.
    - weights (`list[float]`): The weights to apply to each metric map.

    Returns
    ---
    - `MetricMap`: The linear combination of the metric maps.

    Examples
    ---
    >>> metric_map_1.mapping
    [[1.0, 2.0, 3.0]
     [4.0, 5.0, 6.0]]
    >>> metric_map_2.mapping
    [[2.0, 3.0, 4.0]
     [5.0, 6.0, 7.0]]
    >>> combination = linear_combination([metric_map_1, metric_map_2], [1, 2])
    >>> combination.mapping
    [[ 5.0,  8.0, 11.0]
     [14.0, 17.0, 20.0]]
    """

    linear_combination = MetricMap()
    linear_combination.mapping = np.zeros_like(metric_maps[0].mapping)
    for metric_map, weight in zip(metric_maps, weights):
        linear_combination.mapping += weight * metric_map.mapping

    linear_combination.metric_name = f"Linear Combination of {
        ', '.join([metric_map.metric_name for metric_map in metric_maps])
    }"

    return linear_combination
