class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, index):
            if index == len(word):  #BASE CASE sare char mil gye (index is count of word letter) 
                return True  

            if (r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[index]):
                return False  #boundary check(index matrix se bhar na jaye) + char mismatch check + visited check

            temp = board[r][c]
            board[r][c] = '#'   #cell ko temporary viisted mark kr do so no extra SPACE

            found = (dfs(r + 1, c, index + 1) or  #RECURSE -> chasro taraf dhundhna (up, down, left, right)
                     dfs(r - 1, c, index + 1) or  #index + 1 is curr letter found ab recursion go for next 
                     dfs(r, c + 1, index + 1) or  #same as directional arr bs yaha loop ki jgh manual recusrion call likhi 
                     dfs(r, c-1, index + 1))

            board[r][c] = temp #BACKTRACK -> wapas aate waqt char theek kro

            return found  #save t or f and vo jawab upr bhejo

        for r in range(rows):  #har ek cell se DFS shuru krke dekhna 
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r, c, 0): #agr board ka letter woed ke pehle lett se match tabhi vha se DFS start
                    return True 
        return False


# PATTERN -> MATRIX BACKTRACKING jab bhi grid pr rasta dhundhna ho and same cell dobara use krni ho use it 
# SPACE COMP-> O(M*N*4power l) m n board ka size and l word len as har cell se char direction explore (3l h vese as parent cell blocked hota)
#SDPACE - O(L) for recusrion stack else extra visited matrix me O(M*N) lgta
# 2D matrix can be treated like a graph .....DFS ek raste pe gehrai tak jata h and BFS sare padosi ek saath check krta hai..
# DFS use as mere ko deep me jana h pata nhi end me ho vo word agr (linear path) and backtrack so galat raste wale cell ko univisited(false) kr diya ..
#IN-PLACE VISITED - space bachane ko cell ko temp # kra and backtrack krte waqt pehle jesa bana diya else visited map use krna tha
