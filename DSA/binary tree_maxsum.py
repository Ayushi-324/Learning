class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float("-inf")  #global variable overall maxsum tracker

        def dfs(node):
            if not node: #base case empty node 
                return 0

            left_gain = max(0, dfs(node.left))  #ask children their sum ignore -ve results
            right_gain = max(0, dfs(node.right))

            curr_path_sum = node.val + left_gain + right_gain #check curved v shape path at curr_node to update winner
            self.max_sum = max(self.max_sum, curr_path_sum)

            return node.val + max(left_gain , right_gain) #return single best branch to parent node 


        dfs(root)
        return self.max_sum
