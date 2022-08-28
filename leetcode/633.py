"""
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

O(logn)
"""

import math


class Solution(object):

    def search_a(self, s_list, c, start, end):
        if start == end:
            return s_list[start]

        center = int((end + start + 1) / 2)
        if s_list[center] ** 2 <= c:
            if s_list[center + 1] ** 2 > c:
                return s_list[center]
            else:
                start = center + 1
        else:
            end = center - 1
        return self.search_a(s_list, c, start, end)

    def judge_square_sum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        n = 10 ** (len(str(c)) - 1)
        s_list = [i for i in range(0, n + 1)]
        start = 0
        end = len(s_list) - 1

        a = self.search_a(s_list, c, start, end)
        if a == c or math.sqrt(c - a ** 2) % 1 == 0:
            return True
        return False


if __name__ == "__main__":
    print(Solution().judge_square_sum(25))
