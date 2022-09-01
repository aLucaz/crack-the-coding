"""
Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
from typing import Optional

from data_structures.tree import TreeNode


class Solution:

    def get_in_order(self, root, in_order_list):
        if root is None:
            return
        self.get_in_order(root.left, in_order_list)
        in_order_list.append(root.val)
        self.get_in_order(root.right, in_order_list)

    def range_sum_bst(self, root: Optional[TreeNode], low: int, high: int) -> int:
        lista = []
        self.get_in_order(root, lista)
        summ = 0
        for val in lista:
            if val in range(low, high + 1):
                summ += val
        return summ


if __name__ == '__main__':
    node6 = TreeNode(18)
    node5 = TreeNode(7)
    node4 = TreeNode(3)
    node3 = TreeNode(5, node4, node5)
    node2 = TreeNode(15, None, node6)
    node1 = TreeNode(10, node3, node2)

    print(Solution().range_sum_bst(node1, 7, 15))
