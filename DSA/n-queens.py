class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        # Conflict sets: column, positive diagonal (r+c), negative diagonal (r-c)
        cols = set()
        pos_diag = set()  # (row + col) is constant for anti-diagonals (/)
        neg_diag = set()  # (row - col) is constant for main diagonals (\)
        
        res = []
        board = [["."] * n for _ in range(n)] # Khali board create kiya '.' se

        def backtrack(r):
            # Base Case: Agar saare rows me queen place ho gayi, solution mil gaya
            if r == n:
                copy = ["".join(row) for row in board] # Rows ko string me convert kiya
                res.append(copy)
                return
            
            # Current row 'r' ke har column 'c' par queen place karne ki koshish karo
            for c in range(n):
                # Agar column ya diagonals me pehle se koi queen hai, toh skip karo (Conflict check)
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue
                
                # 1. Choose: Queen ko board par place karo aur track karne ke liye sets me dalo
                board[r][c] = "Q"
                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                
                # 2. Explore: Agli row (r + 1) par jao
                backtrack(r + 1)
                
                # 3. Unchoose (Backtrack): Queen hatao taaki doosre paths try kar sakein
                board[r][c] = "."
                cols.remove(c)
                pos_diag.remove(r + c)
                
                neg_diag.remove(r - c)

        # Row 0 se shuru karo
        backtrack(0)
        return res
