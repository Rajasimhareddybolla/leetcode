# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 1
        def find_g(node, m):
            if not node:
                return None
            val = node.val
            if  val >= m :
                self.res += 1
            val = max(m , val)
            find_g(node.left , val)
            find_g(node.right , val)
        
        find_g(root.left, root.val)
        find_g(root.right , root.val)
        return self.res
