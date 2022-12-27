"""
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

2 -> 4 -> 3
5 -> 6 -> 4
-----------
7 -> 0 -> 8

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

"""
from typing import Optional

from data_structures.linked_list import ListNode


class Solution:

    def getValIfExists(self, node: ListNode):
        if node is not None:
            return node.val
        return 0

    def getNextIfExists(self, node: ListNode):
        if node is not None:
            return node.next
        return None

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        curr_node = result
        spare = 0
        while True:
            v1 = self.getValIfExists(l1)
            v2 = self.getValIfExists(l2)
            curr_v = v1 + v2 + spare
            if curr_v >= 10:
                spare = curr_v // 10
                curr_v = curr_v % 10
            else:
                spare = 0
            l1 = self.getNextIfExists(l1)
            l2 = self.getNextIfExists(l2)
            curr_node.val = curr_v
            if l1 is None and l2 is None:
                break
            curr_node.next = ListNode()
            curr_node = curr_node.next
        return result


if __name__ == '__main__':
    s = Solution()
    node3 = ListNode(3)
    node2 = ListNode(4, node3)
    node1 = ListNode(2, node2)

    node6 = ListNode(4)
    node5 = ListNode(6, node6)
    node4 = ListNode(5, node5)

    r = s.addTwoNumbers(node1, node4)
    node1.print_list()
    node4.print_list()
    r.print_list()
