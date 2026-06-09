class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        
# IN RECURSION code niche se start hota hai so phle issametree(1,1) root then issametree for left right if one fail then check p.val!= q.val
#har node pe check -> Dono null ?, ek null?, value same? then left right compare -> P AND Q ARE ROOTS OF BOTH TREES 
#Value mismatch  -> p.val != q.val
#Shape mismatch  -> not p or not q
# Pattern: DFS Tree Traversal (Recursive)
