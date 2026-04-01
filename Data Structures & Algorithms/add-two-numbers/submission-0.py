# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def add(n1 , n2 , carry):
            if not n1 and  not n2:
                if carry :
                    return ListNode(carry)
                return None
            res = 0
            if n1:
                res += n1.val
            if n2:
                res += n2.val
            res += carry

            val = res % 10
            carry = res // 10
            nextnode = add(n1.next if n1 else None , n2.next if n2 else None , carry)
            node = ListNode(val ,nextnode )
            return node
        return add(l1 , l2 , 0)