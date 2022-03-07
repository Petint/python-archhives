import math


def solve(a: float, b: float, c: float) -> 'tuple[float, float]':
    x1 = (b + math.sqrt(b ** 2 - 4 * a * c)) / 2
    x2 = (b - math.sqrt(b ** 2 - 4 * a * c)) / 2
    return x1, x2


# print(solve(1, -1, 1))
print(math.sqrt(-1))
