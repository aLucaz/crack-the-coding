"""
Euclidean approach to solve greatest common divisor
"""


class EuclideanGDC:
    @staticmethod
    def execute(a: int, b: int) -> int:
        print(a, b)
        if b == 0:
            return a
        else:
            return EuclideanGDC.execute(b, a % b)


if __name__ == '__main__':
    print(EuclideanGDC.execute(2, 18))
