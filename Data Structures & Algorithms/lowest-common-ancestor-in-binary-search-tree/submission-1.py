class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def search(node , ele):
            if node is None:
                return []
            val = node.val
            if ele == val:
                return [node]
            path = []
            if ele < val:
                path = search(node.left , ele)
            else:
                path = search(node.right , ele)
            
            path = [node]+path
            return path
        p_val , q_val = p.val , q.val
        path_p = search(root , p_val)
        
        lca = root
        for node in path_p:
            if q_val < node.val:
                if node.left:
                    lca = node
                    continue
            elif q_val > node.val:
                if node.right:
                    lca = node
                    continue
            else:
                lca = node
            break
        return lca