class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_so_far):
            if not node:
                return 0  # Empty node

            is_good = 1 if node.val >= max_so_far else 0 #node val bdi toh good node(1) else 0

            max_so_far = max(max_so_far, node.val)   # Max update kr

            return is_good + dfs(node.left, max_so_far) + dfs(node.right, max_so_far)  #Left + Right children check
        
        return dfs(root, root.val) #root se start


# DFS Pre-order- jb upr se niche aate hue purana data agle level pe pass krna ho    t- O(n) hr node once   s-O(h) stack space equal tree h , wc me O(n ) if lmba linear tree
