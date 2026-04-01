class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        fast = head
        slow = head

        # move fast n steps
        for _ in range(n):
            fast = fast.next

        # if fast is None -> remove head
        if not fast:
            return head.next

        # move both pointers
        while fast.next:
            fast = fast.next
            slow = slow.next

        # remove node
        slow.next = slow.next.next

        return head