"""

a = [1,3,8,48,10]
LNS(a) = 3

LNS(1) = 1
LNS(2) = LNS(1) + and(a{2}, a{1})
LNS(3) = LNS(2) + and(a{3}, a{2})
LNS(4) = LNS(3) + and(a{4}, a{3})
LNS(5) = LNS(4) + and(a{5}, a{4})

"""

from typing import List


class Solution:

    def andWise(self, a, b):
        return 1 if a & b == 0 else 0

    def longestNiceSubarray(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 1:
            return l
        lns = [0] * l
        for i, n in enumerate(nums):
            if i > 0:
                wise = self.andWise(nums[i], nums[i-1])
                lns[i] = lns[i-1] + wise
        return lns[l - 1] if lns[l - 1] != 0 else 1



if __name__ == '__main__':
    s = Solution()
    r = s.longestNiceSubarray([1,3,8,48,10])
    print(r)
    r = s.longestNiceSubarray([3,1,5,11,13])
    print(r)


