import math
from typing import List

Vector = List[float]


class linear_algebra:
    def vector_sum(self, vectors: List[Vector]) -> Vector:
        assert vectors, "no vectors provided!"

        num_elements = len(vectors[0])
        assert all(len(v) == num_elements for v in vectors), "different sizes!"

        return [sum(vector[i] for vector in vectors) for i in range(num_elements)]

    def scalar_multiply(self, c: float, vector: Vector) -> Vector:
        assert vector, "vector cannot be empty"

        return [c * v_i for v_i in vector]

    def vector_mean(self, vectors: List[Vector]) -> Vector:
        n = len(vectors)

        return self.scalar_multiply(1 / n, self.vector_sum(vectors))

    def dot(self, v: Vector, w: Vector) -> float:
        return sum([v[i] * w[i] for i in range(len(v))])

    def sum_of_squares(self, v: Vector) -> float:
        return self.dot(v, v)

    def magnitude(self, v: Vector) -> float:
        """Returns magnitude or length of v"""
        return math.sqrt(self.sum_of_squares(v))

    def subtract(self, v: Vector, w: Vector) -> Vector:
        return [v_i - w_i for v_i, w_i in zip(v, w)]

    def squared_distance(self, v: Vector, w: Vector) -> float:
        return self.magnitude(self.subtract(v, w))


la = linear_algebra()
assert la.vector_sum([[1, 2], [3, 4], [5, 6], [7, 8]]) == [16, 20]
assert la.scalar_multiply(2, [1, 2, 3, 4]) == [2, 4, 6, 8]
assert la.vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]
assert la.dot([1, 2, 3], [4, 5, 6]) == 32
assert la.sum_of_squares([1, 2, 3]) == 14
assert la.magnitude([3, 4]) == 5
assert la.squared_distance([1, 1], [4, 5]) == 5
