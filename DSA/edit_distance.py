class Solution:

    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        # 2D DP Table (Size: (m+1) x (n+1))
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1): #base case- agr ek str khali- puri len operation  
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1): #dp loop
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][
                        j - 1
                    ]  # Same char- Koi oper nhi
                else:
                    # Alg char- Min of(ins, del, rep) +1
                    dp[i][j] = (
                        min(
                            dp[i][j - 1],  # In
                            dp[i - 1][j],  # Del
                            dp[i - 1][j - 1],  # Rep
                        )
                        + 1
                    )

        return dp[m][n]
