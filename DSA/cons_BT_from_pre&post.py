class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        # Fast index lookup for inorder values
        in_map = {val: idx for idx, val in enumerate(inorder)}
        pre_iter = iter(preorder)
        
        def helper(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            
            # Root is always next in preorder
            root_val = next(pre_iter)
            root = TreeNode(root_val)
            mid = in_map[root_val]
            
            # Left subtree must be built first
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            
            return root
            
        return helper(0, len(inorder) - 1)
