class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.counter = 0  #counter to track nodes visited 
        self.result = None  #to store ans 

        def inorder(node):  #in-order traversal (left- root-r)
            if not node or self.result is not None:  #if already result found 
                return 

            inorder(node.left)  #go left 

            self.counter += 1   #process root 
            if self.counter == k:
                self.result = node.val
                return  #found it 

            inorder(node.right)

        inorder(root)  #go right 
        return self.result
