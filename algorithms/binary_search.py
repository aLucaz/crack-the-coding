"""
Recursive approach to solve classic binary search algorithm

O(logn)
"""


class BinarySearch:
    @staticmethod
    def execute(sorted_list, element, start, end):
        if start > end:
            return -1
        center = start + ((end - start + 1) // 2)
        if sorted_list[center] == element:
            return center
        else:
            if sorted_list[center] < element:
                start = center + 1
            if sorted_list[center] > element:
                end = center - 1
            return BinarySearch.execute(sorted_list, element, start, end)


if __name__ == '__main__':
    my_list = [1, 4, 7, 11, 13, 15]
    my_list_size = len(my_list)
    for i, v in enumerate(my_list):
        print(BinarySearch.execute(my_list, v, 0, my_list_size - 1))
