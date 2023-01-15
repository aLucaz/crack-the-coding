"""
On a 2D plane, we place n stones at some integer coordinate points.
Each coordinate point may have at most one stone.
A stone can be removed if it shares either the same row or the same
column as another stone that has not been removed.
Given an array stones of length n where stones[i] = [xi, yi] represents the
location of the ith stone, return the largest possible number of stones that can be removed.

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Explanation: One way to remove 5 stones is as follows:
1. Remove stone [2,2] because it shares the same row as [2,1].
2. Remove stone [2,1] because it shares the same column as [0,1].
3. Remove stone [1,2] because it shares the same row as [1,0].
4. Remove stone [1,0] because it shares the same column as [0,0].
5. Remove stone [0,1] because it shares the same row as [0,0].
Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.

First Approach [INCORRECT]

Ci = [xi, yi]
L = [C0, C1, C2 ... Cn]

M(i,i) = 0

if i < 0 or j < 0then
    M(i,j) = 0
else
    M(i,j) = max(M(i-1:)) + coincide(Ci, Cj)

Example

   0     1     2     3     4     5
[[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]

   0  1  2  3  4  5
0  0, 1, 1, 0, 0, 0
1   , 0, 1, 1, 2, 1
2   ,  , 0, 3, 2, 2
3   ,  ,  , 0, 3, 4
4   ,  ,  ,  , 0, 5
5   ,  ,  ,  ,  , 0

[[0,1],[1,2],[1,3],[3,3],[2,3],[0,2]]

  0 1 2 3 4 5
0 0 0 0 0 0 1
1   0 2 1 1 2
2     0 3 3 2
3       0 4 3
4         0 4
5           0

Second Approach


"""

from typing import List


def print_matrix(m):
    if isinstance(m, list):
        print("=" * 50)
        for i in m:
            print(i)
        print("=" * 50)
    else:
        print(m)


class Solution:

    def get_neighbors(self, c, stones):
        n = []
        for i in range(len(stones)):
            if stones[i][0] == c[0] or stones[i][1] == c[1]:
                n.append(stones[i])
        return n

    def get_longest(self, c, m, stones):
        stones_c = stones[:]
        stones_c.remove(c)
        ns = self.get_neighbors(c, stones_c)
        nm = -1
        for n in ns:
            nm_aux = self.get_longest(n, m + 1, stones_c)
            nm = nm_aux if nm_aux > m else m
        return nm

    def removeStones(self, stones: List[List[int]]) -> int:
        if len(stones) == 1:
            return 0
        m = -1
        for c in stones:
            nm = self.get_longest(c, 0, stones)
            m = nm if nm > m else m
        return m + 1


if __name__ == "__main__":
    s = Solution()
    # r1 = s.removeStones([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]])  # 5
    # print_matrix(r1)
    # r2 = s.removeStones([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]])  # 3
    # print_matrix(r2)
    # r3 = s.removeStones([[0, 0]])  # 0
    # print_matrix(r3)
    # # custom
    # r4 = s.removeStones([[0, 0], [0, 1], [1, 0], [1, 2]])  # 3
    # print_matrix(r4)
    # # failed tests
    # r5 = s.removeStones([[0, 0], [0, 1], [1, 0], [1, 1], [2, 1], [2, 2], [3, 2], [3, 3], [3, 4], [4, 3], [4, 4]])  # 10
    # print_matrix(r5)
    # r6 = s.removeStones([[0, 1], [1, 2], [1, 3], [3, 3], [2, 3], [0, 2]])  # 5
    # print_matrix(r6)
    # r7 = s.removeStones([[0, 1], [1, 0]])  # 0
    # print_matrix(r7)
    # r8 = s.removeStones([[0, 1], [1, 1]])  # 1
    # print_matrix(r8)
    r9 = s.removeStones([[3, 2], [0, 0], [3, 3], [2, 1], [2, 3], [2, 2], [0, 2]])  # 6
    print_matrix(r9)
