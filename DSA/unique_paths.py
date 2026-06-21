class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n  #top aur left edges hmesha ek rasta deta h- > shuru ki row jisme sb 1  

        for i in range(m-1):  #har row ke liye values nikalni h (phle row ko chhod kr)
            new_row = [1] * n
            for c in range(1, n):  # upar + left 
                new_row[c] = row[c] + new_row[c -1]
            row = new_row 

        return row[-1]

# DP ( GRID DP) ,  time - O(m*n) pura grid fill krne ko    space - O(N) ek row track krke space optimize
#LOGIC - kisi bhi cell pr pahuchne ke total raste = uske upar wale cell ka rasta + uske left wale cell ka rasta  dp[r][c] = dp[r-1][c] + dp[r][c-1]      curr_cell = top neighbor + left neig
