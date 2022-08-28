"""
Given an array of positive integers nums, remove the smallest subarray (possibly empty) such that the sum of the remaining elements
is divisible by p. It is not allowed to remove the whole array.

Return the length of the smallest subarray that you need to remove, or -1 if it's impossible.

A subarray is defined as a contiguous block of elements in the array.


O(2^n) - very bad solution

TODO improve logic

"""


class Solution(object):
    @staticmethod
    def min_subarray(nums, p):
        """
        :type nums: List[int]
        :type p: int
        :rtype: int
        """

        ibin = bin(1)
        lnums = len(nums)

        minqzeroes = 100000
        minlist = []

        for i in range(pow(2, lnums) - 1):
            val = bin(int(ibin, 2) + i)
            valstr = str(val[2:]).zfill(lnums)
            valstrlist = [int(v) for v in valstr]

            prod = []
            tempminlist = []
            for num1, num2 in zip(nums, valstrlist):
                prod.append(num1 * num2)
                if num2 == 0:
                    tempminlist.append(num1)

            sumprod = sum(prod)
            qzeroes = valstrlist.count(0)

            if sumprod % p == 0 and qzeroes < minqzeroes:
                minqzeroes = qzeroes
                minlist = tempminlist

        if minqzeroes == 100000:
            return -1

        return len(minlist)


if __name__ == '__main__':
    Solution().min_subarray([1, 2, 3], 7)
