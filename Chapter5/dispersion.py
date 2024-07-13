import math
from pprint import pprint
from typing import List

import Chapter5.app
from Chapter5.app import CentralTendency
from Common.lib import DSA
from DataMath.scratch import linear_algebra

d = DSA()


class DispersionVariance:
    def __init__(self):
        self.ct = CentralTendency()
        self.la = linear_algebra()

    def data_range(self, xs: List[float]) -> float:
        return max(xs) - min(xs)

    # VARIANCE

    def de_mean(self, xs: List[float]) -> List[float]:
        """Translate xs by subtracting its (so the result has mean 0)"""
        x_bar = self.ct.mean(xs)
        return [x - x_bar for x in xs]

    def variance(self, xs: List[float]) -> float:
        """Almost the average squared deviation from the mean"""
        assert len(xs) >= 2, "variance requires at least two elements"
        n = len(xs)
        deviations = self.de_mean(xs)
        return self.la.sum_of_squares(deviations) / (n - 1)

    def standard_deviation(self, xs: List[float]) -> float:
        """The standard deviation is the square root of the variance"""
        return math.sqrt(self.variance(xs))

    def interquartile_range(self, xs: List[float]) -> float:
        """Returns the difference between the 75%-ile and the 25%-ile"""
        return self.ct.quantile(xs, 0.75) - self.ct.quantile(xs, 0.25)


dv = DispersionVariance()
pprint(dv.data_range(d.num_friends))
pprint(dv.variance(d.num_friends))
pprint(dv.standard_deviation(Chapter5.app.num_friends))
pprint(dv.interquartile_range(Chapter5.app.num_friends))
