# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        if not root.left and not root.right:
            return root.val
        def sum( node):
            if not node :
                return 0
            left_sum  = max(sum(node.left) , 0)
            right_sum = max(sum(node.right) , 0)
            r =  left_sum + right_sum + node.val
            self.res =max( r, self.res)
            return r
        sum(root)
        return self.res
        