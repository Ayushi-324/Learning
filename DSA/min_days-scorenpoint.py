class Solution:
    def minDays(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[0] = 0

        for i in range(1, n+1):
            L = 1
            while True:
                pts = L* (L+1) // 2
                if pts>i:
                    break
                if dp[i-pts] + L + 1 < dp[i]:
                    dp[i] = dp[i-pts] + L + 1
                L += 1

        return dp[n] - 1
