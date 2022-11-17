from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = dict()
        for num in arr:
            counter[num] = 1 if counter.get(num) is None else (counter[num] + 1)
        vmax = -1
        for k, v in counter.items():
            if int(k) == v:
                if v > vmax:
                    vmax = v
        return vmax


if __name__ == '__main__':
    res = Solution().findLucky([1, 2, 2, 3, 3, 3])
    print(res)
