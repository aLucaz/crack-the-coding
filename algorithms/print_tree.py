"""

        1
    2       3
4      5 6     None

"""

from data_structures.tree import TreeNode


class TreePrinter(object):

    def in_order(self, root: TreeNode):
        if root is None:
            return
        self.in_order(root.left)
        print(root.val, end=' ')
        self.in_order(root.right)

    def pre_order(self, root: TreeNode):
        if root is None:
            return
        print(root.val, end=' ')
        self.pre_order(root.left)
        self.pre_order(root.right)

    def post_order(self, root: TreeNode):
        if root is None:
            return
        self.post_order(root.left)
        self.post_order(root.right)
        print(root.val, end=' ')


if __name__ == '__main__':
    node6 = TreeNode(6)
    node5 = TreeNode(5)
    node4 = TreeNode(4)
    node3 = TreeNode(3, node6, None)
    node2 = TreeNode(2, node4, node5)
    node1 = TreeNode(1, node2, node3)
    print(TreePrinter().in_order(node1))
    print(TreePrinter().pre_order(node1))
    print(TreePrinter().post_order(node1))
