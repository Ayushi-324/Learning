class Solution:
    def solve(self, board: list[list[str]]) -> None:
        if not board or not board[0]:
            return
        
        ROWS, COLS = len(board), len(board[0])
        
        # 1. Border wale 'O' aur unse jude andar wale 'O' ko safe karne ka function
        def dfs(r: int, c: int):
            # Agar grid se bahar gaye ya cell 'O' nahi hai, toh ruk jao
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != "O":
                return
            
            # Jo 'O' border se touch hai, use temporary 'T' (Safe) mark kar do
            board[r][c] = "T"
            
            # Ab uske upar, neeche, left, right padosi check karo
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        # 2. Top aur Bottom border check karo
        for c in range(COLS):
            if board[0][c] == "O": dfs(0, c)
            if board[ROWS - 1][c] == "O": dfs(ROWS - 1, c)
                
        # 3. Left aur Right border check karo
        for r in range(ROWS):
            if board[r][0] == "O": dfs(r, 0)
            if board[r][COLS - 1] == "O": dfs(r, COLS - 1)
                
        # 4. Final step: Pure board par ghumo
        for r in range(ROWS):
            for c in range(COLS):
                # Jo 'O' bach gaye (border se nahi jude the), unhe 'X' kar do (Capture)
                if board[r][c] == "O":
                    board[r][c] = "X"
                # Jo safe wale 'T' the, unhe wapas asli 'O' bana do
                elif board[r][c] == "T":
                    board[r][c] = "O"
