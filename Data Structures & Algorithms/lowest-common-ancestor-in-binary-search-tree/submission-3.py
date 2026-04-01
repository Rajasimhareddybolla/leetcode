class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # We traverse down from the root
        current = root
        
        while current:
            # If both p and q are greater than current, go right
            if p.val > current.val and q.val > current.val:
                current = current.right
            
            # If both p and q are smaller than current, go left
            elif p.val < current.val and q.val < current.val:
                current = current.left
            
            # If we find the split point (one is smaller, one is larger), 
            # or if current equals p or q, then current is the LCA.
            else:
                return current