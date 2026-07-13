class TrieNode:
    def __init__(self):
        self.children = {}   
        self.is_word = False  #tell yha word khatam or not 
        self.word = ""  #to remember word empty str
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]: #words ko map me dalna (build trie) 
        root = TrieNode()   
        for w in words:   #ex - oath word 
            node = root   #har naye word ke liye wapas top pr aa 
            for char in w:  #phle o then a - t - h 
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_word = True
            node.word = w #h ke box me likha oath 

        rows = len(board)
        coln = len(board[0])
        res = set()

        def dfs(r,c, node):  #backtracking dfs f'n 
            if r < 0 or c < 0  or r >= rows or c >=coln:  #boundary cond
                return 

            char = board[r][c]  #board se char utha 

            if char == "#" or char not in node.children:  #agar char not valid and trie not in path 
                return 

            next_node = node.children[char]  #trie me ek setup niche aa

            if next_node.is_word:  #agr word miljaye set me add
                res.add(next_node.word)

            board[r][c] = "#"  # visited marked

            dfs(r + 1, c, next_node)  #4 directions check 
            dfs(r - 1, c, next_node) 
            dfs(r, c + 1, next_node)  
            dfs(r, c-1, next_node)

            board[r][c] = char  #original char wapas rkh 

        for r in range(rows):  #pure board pr dfs chala
            for c in range(coln):
                dfs(r, c, root)

        return list(res)

# Trie + DFS backtracking     time - O(m*n*4 power l) m*n board size l is max word len  space - O(k*L) k total words l max word len to store in trie

#LOGIC - sirf ek nhi multiple words to find so word serach 1 logic will exceed time so store words in trie and map from there .....build trie from words -> dfs  will check trie tree 






        
