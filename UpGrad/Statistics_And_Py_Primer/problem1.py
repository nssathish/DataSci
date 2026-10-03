from functools import reduce

number = int(input())


def factorial(n: int) -> int:
    if n < 0:
        return -1
    if n < 2:
        return 1
    else:
        return reduce(lambda x, y: x * y, list(range(n, 0, -1)))


print(factorial(number))
