class Solution:
    def numTilings(n: int) -> int:
        if n <= 2: #base case
            return n

        MOD = 10**9 + 7

        prev3, prev2, prev1 = 1, 1, 2 #base val= dp[0], dp[1], dp[2]

        for _ in range(3, n + 1): #iterative to save space
             current = (2 * prev1 + prev3) % MOD  #optim- dp[i] = 2 * dp[i-1] + dp[i-3]
             prev3, prev2, prev1 = prev2, prev1, current   #state shift forward
        
        return prev1


#DP(state reduction opt)   t-O(n) 1 pass, s-O(1) 3 var 

how O(1) - phle O(n) arr used but we only need pichle 3 states                  if arr n bda time- matrix exponential use krke O(logn) kr 
