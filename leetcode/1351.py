"""
Count Negative Numbers in a Sorted Matrix

Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise.
Return the number of negative numbers in grid.

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 100
    -100 <= grid[i][j] <= 100

O(m + m*n) Solution
"""


class Solution:

    @staticmethod
    def count_negatives(grid) -> int:
        big_list = []
        negative_counter = 0
        for row in grid:
            big_list = big_list + row
        for element in big_list:
            if element < 0:
                negative_counter = negative_counter + 1
        return negative_counter


if __name__ == '__main__':
    Solution().count_negatives(grid=[[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]])
