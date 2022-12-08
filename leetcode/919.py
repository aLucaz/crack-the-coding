"""


At most 104 calls will be made to insert and get_root.

"""

from typing import Optional

from data_structures.tree import TreeNode


class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root

    def is_lvl_complete(self, root: TreeNode, curr_lvl, lvl) -> bool:
        if curr_lvl == lvl:
            return root is not None

        return self.is_lvl_complete(root.left, curr_lvl + 1, lvl) and self.is_lvl_complete(root.right, curr_lvl + 1, lvl)

    def insert_complete(self, parent: TreeNode, val, next_lvl) -> TreeNode | None:
        child = TreeNode(val)

        if self.is_lvl_complete(self.root, 1, next_lvl):
            left_child = self.insert_complete(parent.left, val, next_lvl + 1)
            if left_child is not None:
                return left_child
            right_child = self.insert_complete(parent.right, val, next_lvl + 1)
            if right_child is not None:
                return right_child

        if parent.left is None:
            parent.left = child
            return parent
        elif parent.right is None:
            parent.right = child
            return parent

        return None

    def insert(self, val: int) -> int:
        parent = self.insert_complete(self.root, val, 2)
        return parent.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()

if __name__ == '__main__':
    node3 = TreeNode(3, None, None)
    node2 = TreeNode(2, None, None)
    node1 = TreeNode(1, node2, node3)
    s = CBTInserter(node1)
    print(s.insert(4))
    print(s.insert(5))
    print(s.insert(6))
    print(s.insert(7))
    print(s.insert(8))
