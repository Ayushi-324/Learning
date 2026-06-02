class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or root == p or root == q: #BASE CASE- agar rasta khatam ya p/q milgya
            return root

        left_jasoos = self.lowestCommonAncestor(root.left, p, q) #LEFT DFS left subtree me jasoos send wait for report
        right_jasoos = self.lowestCommonAncestor(root.right, p, q) #right dfs

        if left_jasoos and right_jasoos: # PATTERN MAPPING: Post order traversal checking both reports 
            return root #niche se upr aate waqt agar dno side se vaild so root is LCA

        return left_jasoos if left_jasoos else right_jasoos #agr ek side kuch nhi toh send other side upr

# POST-ORDER TRAVERSAL(left, right, node)- pehle left check kiya then right check kiya then root pe aakae decision liya ...i did this in max depth of binary ques too

# LCA is do nodes ka sbse pehla aur sbse lowest rishtedar ....my intuition here was dfs as in tree structure it is the deepest node jo dono nodes ka ancestor hai 

# time complexity- O(N) as visiting every node once and SPACE - 0(H) h is tree height for memory stack
