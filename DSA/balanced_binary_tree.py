class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Helper function returns the height if balanced, or -1 if unbalanced
        def check_height(node):
            if not node:
                return 0
            
            # Check left subtree
            left_height = check_height(node.left)
            if left_height == -1:
                return -1
                
            # Check right subtree
            right_height = check_height(node.right)
            if right_height == -1:
                return -1
            
            # Check current node balance
            if abs(left_height - right_height) > 1:
                return -1
                
            # Return actual height if balanced
            return 1 + max(left_height, right_height)
            
        return check_height(root) != -1

#bottom-up DFS / post order traversal 
time - O(n) each node visit once   space- O(h) recursion stack
