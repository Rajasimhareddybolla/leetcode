# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def search(node , ele):
            if node is None:
                return None
            val = node.val
            if ele == val:
                return [val]
            path = []
            if ele < val:
                path = search(node.left , ele)
            else:
                path = search(node.right , ele)
            
            path = [val]+path
            return path
        p , q = p.val ,q.val
        left = search(root , p)
        print(left)
        node , i = root , 0
        while node and i<len(left) and left[i] == node.val:
            val = node.val
            if q < val :
                node = node.left
            else:
                node = node.right
            i+=1
        print(left[i-1])
        return TreeNode(left[i-1])