"""
Recursive approach to solve classic binary search algorithm

O(logn)
"""


class BinarySearch:
    @staticmethod
    def execute(sorted_list, element, start, end):
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
            return BinarySearch.execute(sorted_list, element, start, end)


if __name__ == '__main__':
    my_list = [1, 4, 7, 11, 15]
    my_list_size = len(my_list)
    print(BinarySearch.execute(my_list, 15, 0, my_list_size - 1))
