class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1) # amount = 2, 2+1=3    dp = [inf,inf,inf] (infinite cost)
        dp[0]  = 0 #base case 0 amount bnane ko 0 coins

        for a in range(1, amount + 1): # 1- amount tk har amount ke liye check 
            for c in coins:
                if a - c >= 0:   #agr coin amount se chota ya equal 
                    dp[a] = min(dp[a], 1 + dp[a - c]) #FORMULA -> ek coin le + bache hue amount ka min coin jod 
        
        return dp[amount] if dp[amount] != float('inf') else -1 #agr dp[amo] abhi bhi inf means amount nhi ban skta


#pattern - bottom up DP, time - O(amount*n) n total amount loop and andar n type coins loop, space - O(a) dp arr
# like in combination sum ques sare raste dhundne so backtracking use here sirf ek rasta jisme min coins use ........so dp use ki calculation yd rkhne ko 

        
