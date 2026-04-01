# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.i = 0
        def ino(root):
            if root is None:
                return None
            l = ino(root.left)
            self.i +=1
            if self.i == k:return  root.val
            if l is not None:
                return l 
            r = ino(root.right)
            if r is not None: return r
            return None
        return ino(root)