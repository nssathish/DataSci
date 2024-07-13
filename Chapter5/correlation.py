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

    def correlation(self, xs: List[float], ys: List[float]) -> float:
        """Measures how much xs and ys varies in tandem about their means"""
        stdev_x = self.dv.standard_deviation(xs)
        stdev_y = self.dv.standard_deviation(ys)
        print("standar deviations", (stdev_x, stdev_y))

        correlation = (
            self.covariance(xs, ys) / (stdev_x * stdev_y)
            if stdev_x > 0 and stdev_y > 0
            else 0
        )

        return correlation


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

pprint(cc.correlation(num_friends, daily_minutes))
pprint(cc.correlation(num_friends, daily_hours))

outlier = num_friends.index(100)  # index of outlier

num_friends_good = [x for i, x in enumerate(num_friends) if i != outlier]
daily_minutes_good = [minute for i, minute in enumerate(daily_minutes) if i != outlier]
daily_hours_good = [hour for i, hour in enumerate(daily_hours) if i != outlier]
pprint(cc.correlation(num_friends_good, daily_minutes_good))
pprint(cc.correlation(num_friends_good, daily_hours_good))

x = [-2, -1, 0, 1, 2]
y = [2, 1, 0, 1, 2]
print("correlation between x and y", CorrelationCausation().correlation(x, y))

y = [99.98, 99.99, 100, 100.01, 100.02]
print("correlation between x and modified y", CorrelationCausation().correlation(x, y))
