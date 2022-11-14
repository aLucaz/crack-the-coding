"""
Euclidean approach to solve the least common multiple
"""

from algorithms.gcd import EuclideanGDC as Gdc


class EuclideanLCM:
    @staticmethod
    def execute(a: int, b: int) -> int:
        return int((a * b) / Gdc.execute(a, b))


if __name__ == '__main__':
    print(EuclideanLCM.execute(49, 21))
