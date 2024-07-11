from pprint import pprint
from typing import List

num_friends = [100, 49, 41, 40, 25, 100, 23, 3, 25, 25, 40, 100]

from collections import Counter

from matplotlib import pyplot as plt

friend_counts = Counter(num_friends)
xs = range(101)
ys = [friend_counts[x] for x in xs]
plt.bar(xs, ys)
plt.axis((0, 101, 0, 25))
plt.title("Histogram of Friend Counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")
plt.show()

num_points = len(num_friends)
largest_value = max(num_friends)
smallest_value = min(num_friends)

sorted_values = sorted(num_friends)
smallest_value = sorted_values[0]
second_smallest_value = sorted_values[1]
second_largest_value = sorted_values[-2]


# central tendencies
def mean(xs: List[float]) -> float:
    return sum(xs) / len(xs)


pprint(mean(num_friends))


def _median_odd(xs: List[float]) -> float:
    return sorted(xs)[len(xs) // 2]


def _median_even(xs: List[float]) -> float:
    xs.sort()
    mid_point = len(xs) // 2
    return (xs[mid_point - 1] + xs[mid_point]) / 2


def median(v: List[float]) -> float:
    return _median_even(v) if len(v) % 2 == 0 else _median_odd(v)


assert median([1, 10, 2, 9, 5]) == 5
assert median([1, 9, 2, 10]) == (2 + 9) / 2

pprint(median(num_friends))

# quantile - a median under which a certain percentile of data lies
# median - a value under which 50% of the data lies


def quantile(xs: List[float], p: float) -> float:
    """Returns the pth-percentile value in xs"""
    p_index = int(p * len(xs))
    return sorted(xs)[p_index]


pprint(sorted(num_friends))
pprint(quantile(num_friends, 0.10))
pprint(quantile(num_friends, 0.20))
pprint(quantile(num_friends, 0.25))
pprint(quantile(num_friends, 0.75))
pprint(quantile(num_friends, 0.90))


def mode(x: List[float]) -> List[float]:
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items() if count == max_count]


pprint(mode(num_friends))
