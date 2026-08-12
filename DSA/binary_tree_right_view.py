from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            
            for i in range(level_size):
                current_node = queue.popleft()
                
                # Agar ye level ka aakhri node hai, toh right side se dikhega
                if i == level_size - 1:
                    result.append(current_node.val)
                
                # Next level ke liye queue mein bachhe daal do
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
                    
        return result
