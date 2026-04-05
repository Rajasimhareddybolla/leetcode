class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        node = root
        while node:
            if p.val < node.val and q.val < node.val:
                node = node.left
            if p.val > node.val and q.val > node.val:
                node = node.right
            else:
                break
        
        return node