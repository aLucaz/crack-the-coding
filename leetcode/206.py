from data_structures.linked_list import ListNode

"""


Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

"""


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        loop = 1
        new_head = None
        while head.next is not None:
            # go tail
            tail = head
            prev = None
            while tail.next is not None:
                prev = tail
                tail = tail.next
            if loop == 1:
                new_head = tail
            # change
            prev.next = None
            tail.next = prev
            loop += 1

        return new_head


if __name__ == '__main__':
    node4 = ListNode(4)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(1, node2)

    head = Solution().reverseList(node1)
    head.print_list()
