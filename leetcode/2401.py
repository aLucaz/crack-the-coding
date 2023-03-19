"""

a = [1,3,8,48,10]
LNS(a) = 3


LNS(1) = 1 => c=1 m=1
LNS(2) = LNS(1) + and(a{2w1}) => c=2 m=2
LNS(3) = LNS(2) + and(a{3w1},a{3w2}) => c=1 m=2
LNS(4) = LNS(3) + and(a{4w3}) => c=2 m=2
LNS(5) = LNS(4) + and(a{5w4},a{5w3}) => c=3 m=2
LNS(6) = LNS(5) + and(a{5w4},a{5w3},a{5w2}) => c=3 m=3

     0 1 2 3  4
     1 3 8 48 10
0  1 1 1 1 1  1
1  3   1 2 3  3
2  8     1 3  3
3  48      1  3
4  10         1

LNS(i,j)

LNS(0,0) = 1
LNS(0,1) = MAX(LNS(0,0) + and(1:0), 0)
LNS(0,2) = MAX(LNS(0,1) + and(2:0), 0)
LNS(0,3) = MAX(LNS(0,2) + and(3:0), 0)
LNS(0,4) = MAX(LNS(0,3) + and(4:0), 0)

LNS(1,2) = MAX(LNS(1,1) + and(2:1), LNS(0,2))
LNS(1,3) = MAX(LNS(1,2) + and(3:1), LNS(0,3))
LNS(1,4) = MAX(LNS(1,3) + and(4:1), LNS(0,4))

LNS(2,3) = MAX(LNS(2,2) + and(3:2), LNS(1,3))
LNS(2,4) = MAX(LNS(2,3) + and(4:2), LNS(1,4))

LNS(3,4) = MAX(LNS(3,3) + and(4:3), LNS(2,4))


LNS(i,j) = MAX(LNS(i, j-1) + and(j:i), LNS(i-1, j))

"""

import numpy as np
from typing import List


class Solution:

    def andWise(self, arr, i, j):
        nice = True
        while i != j:
            nice = nice and arr[i] & arr[j] == 0
            i += 1
        return 1 if nice else 0

    def longestNiceSubarray(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return l
        lns = np.diag(np.ones(l), 0)
        for i in range(l):
            for j in range(l):
                if j > i:
                    if i - 1 >= 0:
                        lns[i][j] = max(lns[i][j - 1] + self.andWise(nums, i, j), lns[i - 1][j])
                    else:
                        lns[i][j] = max(lns[i][j - 1] + self.andWise(nums, i, j), 0)
        for r in lns:
            print(r)
        return lns[l - 2][l - 1]

    def calculate(self, arr):
        print('=' * 100)
        for i in range(len(arr) - 1):
            print('{0} & {1} => {2}'.format(arr[i], arr[i + 1], arr[i] & arr[i + 1]))
        print('=' * 100)


if __name__ == '__main__':
    s = Solution()
    r = s.longestNiceSubarray([1, 3, 8, 48, 10])
    print(r)
    s.calculate([1, 3, 8, 48, 10])
    r = s.longestNiceSubarray([3,1,5,11,13])
    print(r)
    r = s.longestNiceSubarray([744437702,379056602,145555074,392756761,560864007,934981918,113312475,1090,16384,33,217313281,117883195,978927664])
    print(r)
