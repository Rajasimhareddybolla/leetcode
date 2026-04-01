# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def construct(preorder , inorder):
            if not preorder:
                return None
            root_ele = preorder[0]
            i= inorder.index(root_ele)
            tree = TreeNode(val = root_ele , 
            left= construct(preorder[1:i+1] ,inorder[:i] ),
            right = construct(preorder[i+1:] , inorder[i+1:])
            )
            return tree
        
        return construct(preorder , inorder)