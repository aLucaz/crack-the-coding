"""
Euclidean approach to solve least common multiple
"""

from classic.algorithms.gcd import EuclideanGDC as gdc


class EuclideanLCM:
    @staticmethod
    def execute(a: int, b: int) -> int:
        return int((a * b) / gdc.execute(a, b))


if __name__ == '__main__':
    print(EuclideanLCM.execute(20, 9))
