class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.cameras = 0
        
        def dfs(node):
            if not node:
                return 2  # Null nodes consider covered
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if left == 0 or right == 0: #rule1- any child need help- put camera
                self.cameras += 1
                return 1
        
            if left == 1 or right == 1:#rule2- any child has camera- this node is covered
                return 2
            return 0  #rule3- both children covered- this node needs help

        if dfs(root) == 0: #special case- if root itself is not covered- put a camera
            self.cameras += 1
            
        return self.cameras
