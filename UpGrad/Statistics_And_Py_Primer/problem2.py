number = int(input())


def _py_reverse(n: int):
    numbers = []
    while n != 0:
        numbers.append(n % 10)
        n //= 10

    result = 0
    for exp, n in enumerate(reversed(numbers)):
        result += n * (10**exp)

    return result


def py_reverse(n: int) -> int:
    return -1 * _py_reverse(abs(n)) if n < 0 else _py_reverse(n)


print(py_reverse(number))
