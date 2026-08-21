# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        self.temp = head
        self.stop = False

        def recurse(node):
            if not node:
                return

            recurse(node.next)

            # 1. Stop processing if pointers have already crossed
            if self.stop:
                return

            # 2. Check if pointers met in the middle
            # Odd length: self.temp == node
            # Even length: self.temp.next == node
            if self.temp == node or self.temp.next == node:
                node.next = None
                self.stop = True
                return

            # 3. Interleave pointers
            nxt = self.temp.next
            self.temp.next = node
            node.next = nxt
            self.temp = nxt

        recurse(head)