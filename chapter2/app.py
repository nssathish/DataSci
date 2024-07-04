# list comprehensions

even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)

square_dict = {x: x * x for x in range(5)}
print(square_dict)
print(type(square_dict))

square_set = {x * x for x in {1, -1}}
print(square_set, type(square_set))

# 2-D co-ordinates
pairs = [(x, y) for x in range(3) for y in range(3)]
print(pairs, type(pairs))

increasing_pairs = [(x, y) for x in range(3) for y in range(x + 1, 3)]
print(increasing_pairs, type(increasing_pairs))

assert 1 + 1 == 2, "1 + 1 should equal 2 but didn't"


def smallest_item(xs):
    assert xs, "empty list"
    return min(xs)


smallest_item([1])


# Deal with classes
class CountingClicker:
    """A class can/should have a docstring, just like a function"""

    def __init__(self, count=0):
        self.count = count

    def __repr__(self):
        return f"CountingClicker(count={self.count})"

    def click(self, num_times=1):
        """Click the clicker some number of times"""
        self.count += num_times

    def read(self):
        return self.count

    def reset(self):
        self.count = 0


clicker1 = CountingClicker()
clicker2 = CountingClicker(100)
clicker3 = CountingClicker(count=100)

assert clicker1.read() == 0

clicker1.click()
clicker1.click()

assert clicker1.read() == 2

clicker1.reset()
assert clicker1.read() == 0


class NoResetClicker(CountingClicker):
    def reset(self):
        pass


no_reset_clicker = NoResetClicker()
assert no_reset_clicker.read() == 0
no_reset_clicker.click()
no_reset_clicker.click()
assert no_reset_clicker.read() == 2
no_reset_clicker.reset()
assert no_reset_clicker.read() == 2


def generate_range(n):
    i = 0
    while i < n:
        yield i
        i += 1


for i in generate_range(10):
    print(f"i: {i}")


def natural_numbers():
    """returns 1, 2, 3, ..."""
    n = 1
    while n < 100:
        yield n
        n += 1


evens_below_20 = (i for i in generate_range(20) if i % 2 == 0)
print([x for x in evens_below_20])

data = natural_numbers()
evens = (x for x in data if x % 2 == 0)
even_squares = (x**2 for x in evens)
even_squares_ending_in_six = (x for x in even_squares if x % 10 == 6)

print([x for x in even_squares_ending_in_six])

names = ["alice", "bob", "charlie", "debbie"]

for i, name in enumerate(names):
    print(f"({i}) - {name}")

import random

random.seed(10)

four_uniform_randoms = [random.random() for _ in range(4)]
[print(x) for x in four_uniform_randoms]

random.randrange()

from typing import Callable


def twice(repeater: Callable[[str, int], str], s: str) -> str:
    return repeater(s, 2)


def comma_repeater(s: str, n: int) -> str:
    n_copies = [s for _ in range(n)]
    return ", ".join(n_copies)
