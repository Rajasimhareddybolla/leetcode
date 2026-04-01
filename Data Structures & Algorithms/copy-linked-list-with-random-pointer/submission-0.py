"""
# Definition for a Node.
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        memo = {}
        def create(node):
            if node == None:
                return None
            if node in memo :
                return memo[node]
            curr = Node(node.val , None , None)
            memo[node] = curr

            if node.next:
                nnode = create(node.next)
            else:
                nnode = None
            if node.random:
                rnode = create(node.random)
            else:
                rnode = None
            curr.next = nnode
            curr.random = rnode
            return curr
        return create(head)