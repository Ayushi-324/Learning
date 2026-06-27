class Codec:
    def serialize(self, root):
        res = []
        def dfs(node):
            if not node:
                res.append("X")  # none mila toh X likh 
                return
            res.append(str(node.val)) # pehle root value daal
            dfs(node.left)  # fir left ghum
            dfs(node.right)  
        dfs(root)
        return ",".join(res)  #sare elements ko comma se jod kr string bana di

    def deserialize(self, data):
        vals = data.split(",")   # comma hatake list banayi
        self.i = 0  #list ka index track krne ke liye global pointer

        def dfs():
            if vals[self.i] == "X":
                self.i += 1
                return None  #X mila toh none return 

            node = TreeNode(int(vals[self.i]))   #naya node bnaya
            self.i += 1
            node.left = dfs()  #left child jodo
            node.right = dfs()  # right child jod
            return node

        return dfs()

  # PRE -ORDER DFS  time - 0(n) har node visited once     , space - O(n) o/p string aur split list store krneko
# jaise tree ko ghumaoge(BFS/DFS) waise hi string banegi , aur waise hi string se wapas tree bnega
#LOGIC - Serialize (tree to string) -> pre order dfs (root -left- right) chala , agr node mile toh uski value aur comma jodte jao agar none mile toh string me X daldoDeserialize(string to tree) -> string ko comma se split krke list banao, wapas vhi same pre order dfs chala - phla element root banega , baki se left aur right subtrees banenge . agr x mile return None
