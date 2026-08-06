class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Hash map for O(1) root lookup in inorder list
        in_map = {val: idx for idx, val in enumerate(inorder)}

        # p_i, p_j : bounds [start, end] for preorder
        # in_i, in_j : bounds [start, end] for inorder
        def construct(p_i: int, p_j: int, in_i: int, in_j: int) -> Optional[TreeNode]:
            if p_i > p_j or in_i > in_j:
                return None

            # First element in preorder window is the root
            root_val = preorder[p_i]
            root = TreeNode(root_val)

            # Find root position in inorder array
            in_root = in_map[root_val]
            
            # Number of elements in the left subtree
            left_size = in_root - in_i

            # Construct Left Subtree:
            # Preorder range: [p_i + 1  to  p_i + left_size]
            # Inorder range:  [in_i     to  in_root - 1]
            root.left = construct(p_i + 1, p_i + left_size, in_i, in_root - 1)

            # Construct Right Subtree:
            # Preorder range: [p_i + left_size + 1  to  p_j]
            # Inorder range:  [in_root + 1          to  in_j]
            root.right = construct(p_i + left_size + 1, p_j, in_root + 1, in_j)

            return root

        n = len(preorder)
        return construct(0, n - 1, 0, n - 1)