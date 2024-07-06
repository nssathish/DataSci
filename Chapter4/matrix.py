from pprint import pprint
from typing import List, Tuple, Callable

Matrix = List[List[float]]
Vector = List[float]

A = [[1, 2, 3], [4, 5, 6]]
B = [[1, 2], [3, 4], [5, 6]]


def shape(A: Matrix) -> Tuple[int, int]:
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0

    return num_rows, num_cols


assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3)


def get_row(A: Matrix, i: int) -> Vector:
    return A[i]


def get_col(A: Matrix, j: int) -> Vector:
    return [A_i[j] for A_i in A]


def make_matrix(
    num_rows: int, num_cols: int, entry_fn: Callable[[int, int], float]
) -> Matrix:
    return [[entry_fn(a, b) for b in range(num_cols)] for a in range(num_rows)]


def identity_matrix(n: int) -> Matrix:
    return make_matrix(n, n, lambda a, b: 0 if a == b else 0)


assert identity_matrix(3) == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

friendships = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (5, 7),
    (6, 8),
    (7, 8),
    (8, 9),
]

friend_matrix = identity_matrix(10)
for i in range(len(A)):
    friend_matrix[i][i] = 0

pprint(friend_matrix)
for i, j in friendships:
    print(f"i: {i} j: {j}")
    friend_matrix[i][j] = 1
    friend_matrix[j][i] = 1

pprint(friend_matrix)

assert friend_matrix[0][2] == 1, "0 and 2 are friends"
assert friend_matrix[0][8] == 0, "0 and 8 are not friends"

friends_of_five = [i for i, is_friend in enumerate(friend_matrix[5]) if is_friend]
pprint(friends_of_five)
