class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:  #khali matrix 0 area 
            return 0 

        rows = len(matrix)
        coln = len(matrix[0])
        dp = [0] * (coln + 1) #1d arr to store dp values for curr and prev row 
        max_side = 0

        for i in range(rows): 
            diagonal = 0 #stores top left value at start of each row is 0 
            for j in range(coln):
                next_diagonal = dp[j+1] #save top when loop further this top will become diagonal 
                
                if matrix[i][j] == "1":
                    dp[j+1] = min(dp[j], dp[j+1], diagonal) + 1 #left , top, d 
                    max_side = max(max_side, dp[j+1])
                else:
                    dp[j+1] = 0 # 0 makes no square

                diagonal = next_diagonal #saved top value main diag me to use in next coln calculation

        return max_side * max_side #area = side*side
