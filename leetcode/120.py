"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

Planning:

This is an Dinamyc Programming Problem so:

M : set of minimum path sum solutions starting from bottom to top

recurrence:

    M[0..s-1] = triangle[s-1] -> first set of solutions
    M[i] = min(M[i], M[i+1]) + triangle[n][i] -> refreshing set of solutions

    given
    s: number of rows
    n: s-2..0 -> current row from bottom to top
    i: 0..n+1 -> element of row

O((n-1)^2)
"""


class Solution:
    @staticmethod
    def minimum_total(triangle) -> int:
        s = len(triangle)
        M = triangle[s - 1]
        for n in range(s - 2, -1, -1):
            for i in range(0, n + 1):
                M[i] = min(M[i], M[i + 1]) + triangle[n][i]
        return M[0]


if __name__ == '__main__':
    print(Solution.minimum_total(
        [
            [-1],
            [2, 4],
            [1, -1, -5]
        ]
    ))