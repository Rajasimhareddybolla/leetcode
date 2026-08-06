# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        

        self.res = float("-inf")
        def fsum(node):
            if not node:
                return 0
            val = node.val
            left = fsum(node.left)
            right = fsum(node.right)
            self.res = max(self.res , val + max(left,0 )+max(right, 0))
            return val + max(max(left,0 ), max(right, 0))
        
        fsum(root)
        return self.res