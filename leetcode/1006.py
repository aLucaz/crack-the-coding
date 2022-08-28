"""Normally, the factorial of a positive integer n is the product of all positive integers less than or equal to n.
For example, factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1.

We instead make a clumsy factorial: using the integers in decreasing order, we swap out the multiply operations for a
fixed rotation of operations: multiply (*), divide (/), add (+) and subtract (-) in this order.


For example, clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1.  However, these operations are still applied using
the usual order of operations of arithmetic: we do all multiplication and division steps before any addition or
subtraction steps, and multiplication and division steps are processed left to right.

Additionally, the division that we use is floor division such that 10 * 9 / 8 equals 11.  This guarantees the result
is an integer.

Implement the clumsy function as defined above: given an integer N, it returns the clumsy factorial of N.

1 <= N <= 10000
-2^31 <= answer <= 2^31 - 1  (The answer is guaranteed to fit within a 32-bit integer.)

O(n^2/4)

TODO: improve this approach (brute force)
"""

m = lambda x, y: x * y
d = lambda x, y: int(x / y)
s = lambda x, y: x + y


class Solution:
    def __init__(self):
        self.operations = [m, d, s]

    def clumsy(self, N: int) -> int:
        first = True
        result = self.calculate_sub_clusmy(N, first)
        if N > 4:
            first = False
            for elem in range(N - 4, -1, -4):
                result = result + self.calculate_sub_clusmy(elem, first)
        return result

    def calculate_sub_clusmy(self, n, first):
        res = n if first else -n
        for elem in range(n - 1, n - 4, -1):
            if elem > 0:
                oper = self.operations.pop(0)
                self.operations.append(oper)
                res = oper(res, elem)
        return res


if __name__ == '__main__':
    print(Solution().clumsy(3))
