# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ## inorder triveral -- you will get in sorted order 
        self.k = k
        self.res = root.val
        def ino(node ):
            if not node: return 
            left = ino(node.left )
            self.k -= 1
            if self.k == 0 :
                self.res = node.val
                return node.val
            right = ino(node.right)
        ino(root)
        return self.res