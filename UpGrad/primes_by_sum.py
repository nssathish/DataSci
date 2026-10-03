from math import sqrt

arr = [
    1,
    2,
    5,
    8,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    29,
    30,
    31,
    33,
    37,
    39,
    41,
    42,
    43,
    45,
    46,
    47,
    49,
    53,
    59,
    61,
    66,
    67,
    71,
    79,
    80,
    82,
    88,
    89,
    92,
    99,
    109,
    120,
    121,
    125,
    130,
    131,
    133,
    136,
    140,
    145,
    148,
    157,
    169,
    178,
    182,
    193,
    199,
    200,
]


def find_primes(array):
    primes = []
    composites = []
    for num in array:
        if is_prime(num):
            primes.append(num)
        else:
            composites.append(num)
    return [primes, composites]


def is_prime(num):
    if num < 2:
        return False

    for factor in range(2, int(sqrt(num)) + 1):
        if num % factor == 0:
            return False

    return True


numbers_hashed = {}

for num in find_primes(arr)[1]:
    numbers_hashed[num] = 0

print(find_primes(arr))
print(numbers_hashed)

result = []
for num in find_primes(arr)[0]:
    for key in numbers_hashed.keys():
        if abs(num - key) in numbers_hashed:
            result.append(num)
            break

print(result)
