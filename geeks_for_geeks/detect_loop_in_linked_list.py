"""
Given a linked list of N nodes. The task is to check if the linked list has a loop. Linked list can contain self loop.

1 -> 2 -> 3 -> 4
     |         |
      ---------

Note
a. always the loop starts on the tail to one element before

O(n)

"""


class Solution:
    # Function to check if the linked list has a loop.
    def detect_loop(self, head):
        i = 1
        curr = head
        while True:
            prev_index = i
            curr.index = prev_index

            if curr.next == None:
                return False

            curr = curr.next

            atr_list = list(curr.__dict__.keys())
            if 'index' in atr_list and curr.index != None and curr.index < prev_index:
                return True

            i = i + 1


# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

    # connects last node to node at position pos from begining.
    def loop_here(self, pos):
        if pos == 0:
            return

        walk = self.head
        for i in range(1, pos):
            walk = walk.next

        self.tail.next = walk


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())

        LL = LinkedList()
        for i in input().split():
            LL.insert(int(i))

        LL.loop_here(int(input()))

        print(Solution().detect_loop(LL.head))
