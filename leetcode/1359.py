"""
Given n orders, each order consist in pickup and delivery services.

Count all valid pickup/delivery possible sequences such that delivery(i) is always after of pickup(i).

Since the answer may be too large, return it modulo 10^9 + 7.

1 <= n <= 500

O(n)
"""


class Solution:
    def count_orders(self, n: int) -> int:
        m = 1000000007
        if n == 1:
            return 1
        response = self.count_orders(n - 1) * (((n - 1) * 2) + 1) * n
        return response if n < 8 else response % m


if __name__ == '__main__':
    print(Solution().count_orders(8))
