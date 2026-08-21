class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        total_sum = sum(nums)
        
        # Impossible conditions check karo
        if (total_sum + target) % 2 != 0 or total_sum < abs(target):
            return 0
        
        # Target subset sum nikalo: (P - N = target) formula se
        subset_target = (total_sum + target) // 2
        
        # DP array: dp[i] matlab 'i' sum banane ke tareeqe
        dp = [0] * (subset_target + 1)
        dp[0] = 1 # 0 sum banane ka 1 tareeqa (empty set)
        
        # 0/1 Knapsack logic
        for num in nums:
            # Reverse loop taaki ek element baar-baar use na ho
            for j in range(subset_target, num - 1, -1):
                dp[j] += dp[j - num] # Purane combinations add karo
                
        return dp[subset_target]
