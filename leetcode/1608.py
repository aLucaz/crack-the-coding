"""
You are given an array nums of non-negative integers.
nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.

Notice that x does not have to be an element in nums.
Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.

Input: nums = [3,5]
Output: 2
Explanation: There are 2 values (3 and 5) that are greater than or equal to 2.

O(n)

it can be improved using binary search

"""


class Solution(object):
    @staticmethod
    def special_array(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        lnums = len(nums)

        if lnums == 1 and nums[i] < 1:
            return -1

        nums.sort(reverse=True)
        while i < lnums and nums[i] >= i:
            i += 1
        return -1 if lnums > i > nums[i - 1] else i


if __name__ == '__main__':
    res = Solution().special_array([3])
    print(res)
