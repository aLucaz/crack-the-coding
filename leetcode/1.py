from typing import List


class Solution:

    def _search(self, sorted_list, start, end, element) -> int:
        if start == end:
            return -1
        center = start + ((end - start + 1) // 2)
        if sorted_list[center] == element:
            return center
        else:
            if sorted_list[center] < element:
                start = center + 1
            elif sorted_list[center] > element:
                end = center - 1
            return self._search(sorted_list, start, end, element)

    def _partition(self, arr, arr_idx, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                arr_idx[i], arr_idx[j] = arr_idx[j], arr_idx[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        arr_idx[i + 1], arr_idx[high] = arr_idx[high], arr_idx[i + 1]
        return i + 1

    def _sort(self, arr, arr_idx, start, end):
        if start < end:
            pi = self._partition(arr, arr_idx, start, end)
            self._sort(arr, arr_idx, start, pi - 1)
            self._sort(arr, arr_idx, pi + 1, end)

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_len = len(nums)
        nums_idx = [i for i in range(nums_len)]
        self._sort(nums, nums_idx, 0, nums_len - 1)
        indexes = []
        for i, e in enumerate(nums):
            rest = target - e
            j = self._search(nums, i, len(nums), rest)
            if j != -1:
                indexes.append(nums_idx[i])
                indexes.append(nums_idx[j])
                break
        return indexes


if __name__ == '__main__':
    s = Solution()
    r1 = s.twoSum([2, 7, 11, 15], 9)
    print(r1)
    r2 = s.twoSum([3, 2, 4], 6)
    print(r2)
    r3 = s.twoSum([3, 3], 6)
    print(r3)
