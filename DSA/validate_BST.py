# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, low=float('-inf'), high=float('inf')):
            if not node: #base case - empty tree always valid BST
                return True

            if not (low < node.val < high):  #curr node ki value within boundaries
                return False

            return(dfs(node.left, low, node.val) and #recursively check subtrees with updated bounds
                   dfs(node.right, node.val, high))

        return dfs(root)  #start dfs


# Recursive DFS with valid ranges      time - O(n) every node visitied once  space - O(H) tree h (recursion stack depth) 
