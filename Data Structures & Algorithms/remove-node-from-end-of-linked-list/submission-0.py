# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        h = head
        m = n
        while m  :
            h=h.next

            m = m -1
        
        prev , curr = h , head
        while h:
            h = h.next
            prev = curr
            curr= curr.next
        if prev and prev.next:
            prev.next = prev.next.next
        else:
            return None
        return head
            