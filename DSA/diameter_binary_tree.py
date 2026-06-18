class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0 #tsbse bada rasta store krne ko variable 

        def dfs(node):
            if not node:
                return 0  #base case -> khali jagah height 0

            left = dfs(node.left)  #left side ki height lao 
            right = dfs(node.right)

            self.max_diameter = max(self.max_diameter, left + right) #node pe khade hoke dono sides jodkar diameter nikalna & update max

            return 1 + max(left, right) #parent ko apni sbse lambi height (+1 khud ka bond) return (sirf bad wali chain)
        
        dfs(root)
        return self.max_diameter

# recursion h toh left right me comp niche se height mangwata h 
