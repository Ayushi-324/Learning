class Solution:
    def maxDepth(self, root):
        if not root:
            return 0 

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# TREE ek  graph hi h bs usme gol nhi ghum skte  DFS (POST ORDER TRAVERSAL) 
 time O(n) tree ke hr node pr ek bar , space - O(h) h is tree height ye internal call stack ka space
