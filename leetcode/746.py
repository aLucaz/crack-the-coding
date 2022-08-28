"""

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Constraints

2 <= cost.length <= 1000
0 <= cost[i] <= 999

Solution

C(0) = 0
C(1) = c1
C(2) = min(c2 + C(1), c2 + C(0))
...
C(n) = min(cn + C(n-1), cn + C(n-2))

response min(C(n), C(n-1))


O(n)

"""


class Solution(object):
    @staticmethod
    def min_cost_climbing_stairs(cost):
        """
        :type cost: List[int]
        :rtype: int
        """

        lcost = len(cost)

        cList = [-1] * (lcost + 1)
        cList[0] = 0
        cList[1] = cost[0]

        for n in range(2, lcost + 1):
            cList[n] = min(cost[n-1] + cList[n-1], cost[n-1] + cList[n-2])

        return min(cList[lcost], cList[lcost-1])


if __name__ == '__main__':
    res = Solution().min_cost_climbing_stairs([10, 15, 20])
    print(res)


