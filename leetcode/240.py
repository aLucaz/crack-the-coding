"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

O(n log(n))
"""


class Solution:
    def search_matrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        for sorted_list in matrix:
            if sorted_list and self.binary_search(sorted_list, target, 0, len(sorted_list) - 1) != -1:
                return True
        return False

    @staticmethod
    def binary_search(sorted_list, element, start, end):
        if start == end:
            if sorted_list[start] == element:
                return start
            else:
                return -1
        center = int(end - start + 1 / 2)
        if sorted_list[center] == element:
            return center
        else:
            if sorted_list[center] < element:
                start = center + 1
            if sorted_list[center] > element:
                end = center - 1
            return Solution.binary_search(sorted_list, element, start, end)


if __name__ == '__main__':
    matrix = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    print(Solution().search_matrix(matrix, 5))
    print(Solution().search_matrix(matrix, 20))
