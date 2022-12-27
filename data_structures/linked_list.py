class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print_list(self):
        curr = self
        while True:
            print(curr.val, end=' ')
            curr = curr.next
            if curr is None:
                break
            print(" => ", end=' ')
        print("\r")
