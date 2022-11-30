"""
Count ways to build good strings

Input: low = 2, high = 3, zero = 1, one = 2
Output: 5
Explanation: The good strings are "00" "11" "000" "110" "011"

Return the number of different good strings that can be constructed satisfying these properties.
Since the answer can be large, return it modulo 10^9 + 7

Constraints:

1 <= low <= high <= 10^5
1 <= zero, one <= low

Thought Dynamic Programming

custom examples

low = 1, high = 4, zero = 1, one = 1

key -> represents number of digits
value -> represents quantity of elements with 'key' number of digits

{
    1: 2
    2: 4
    3: 8
    4: 16
}

low = 1, high = 4, zero = 1, one = 2 NOT POSIBLE

low = 2, high = 3, zero = 1, one = 2

{
    1: 1
    2: 2
    3: 3
}

dp[i] = dp[i - zero] + dp[i - one]

dp[i < 0] = 0
dp[i >= 0 and i < low] = 1

using dynamic programming

complexity -> On where n is high
memory -> On where n is high
"""


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = {}
        for i in range(1, high + 1):
            i_zero = i - zero
            without_zero_elements = 0
            if dp.get(i_zero) is None:
                if 0 <= i_zero <= low:
                    without_zero_elements = 1
            else:
                without_zero_elements = dp.get(i_zero)

            i_one = i - one
            without_one_elements = 0
            if dp.get(i_one) is None:
                if 0 <= i_one <= low:
                    without_one_elements = 1
            else:
                without_one_elements = dp.get(i_one)

            dp[i] = without_zero_elements + without_one_elements
        module = 10 ** 9 + 7
        subdp = {k: dp[k] for k in range(low, high + 1)}
        return sum(subdp.values()) % module


if __name__ == '__main__':
    s = Solution()
    r = s.countGoodStrings(1, 4, 1, 1)
    print(r)
    r = s.countGoodStrings(3, 3, 1, 1)
    print(r)
    r = s.countGoodStrings(2, 3, 1, 2)
    print(r)
