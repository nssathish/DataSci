from typing import List

Vector = List[float]


def vector_sum(vectors: List[Vector]) -> Vector:
    assert vectors, "no vectors provided!"

    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "different sizes!"

    return [sum(vector[i] for vector in vectors) for i in range(num_elements)]


assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]


def scalar_multiply(c: float, vector: Vector) -> Vector:
    assert vector, "vector cannot be empty"

    return [c * v_i for v_i in vector]


assert scalar_multiply(2, [1, 2, 3, 4]) == [2, 4, 6, 8]


def vector_mean(vectors: List[Vector]) -> Vector:
    n = len(vectors)

    return scalar_multiply(1 / n, vector_sum(vectors))


assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]


def dot(v: Vector, w: Vector) -> float:
    return sum([v[i] * w[i] for i in range(len(v))])


assert dot([1, 2, 3], [4, 5, 6]) == 32


def sum_of_squares(v: Vector) -> float:
    return dot(v, v)


assert sum_of_squares([1, 2, 3]) == 14

import math


def magnitude(v: Vector) -> float:
    """Returns magnitude or length of v"""
    return math.sqrt(sum_of_squares(v))


assert magnitude([3, 4]) == 5
