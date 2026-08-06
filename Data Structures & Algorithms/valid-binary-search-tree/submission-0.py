# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isvalid(node , l , h):
            if not node:
                return True

            val = node.val
            if l <  val < h :
                left = isvalid(node.left , l , val)
                right = isvalid(node.right , val , h)
                return left & right

            return False

        return isvalid(root , float("-inf"), float("inf"))