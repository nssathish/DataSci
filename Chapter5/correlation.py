# variance - how a single variable deviates from its mean
# covariance - how 2 variables deviate in tandem from their means
from pprint import pprint
from typing import List

from Chapter5.app import num_friends
from DataMath.scratch import linear_algebra
from dispersion import DispersionVariance


class CorrelationCausation:
    def __init__(self):
        self.dv = DispersionVariance()
        self.la = linear_algebra()

    def covariance(self, xs: List[float], ys: List[float]) -> float:
        assert len(xs) == len(ys), "xs and ys must have same number of elements"

        return self.la.dot(self.dv.de_mean(xs), self.dv.de_mean(ys)) / len(xs) - 1


daily_minutes: List[float] = [
    20,
    21,
    20,
    23,
    40,
    100,
    91,
    34,
    57,
    67,
    23,
    67,
    68,
    34,
    34,
    89,
    23,
    23,
    12,
    67,
    89,
    34,
    67,
    23,
    98,
]
daily_hours: List[float] = [minute / 60 for minute in daily_minutes]
cc = CorrelationCausation()
pprint(cc.covariance(num_friends, daily_minutes))
pprint(cc.covariance(num_friends, daily_hours))
