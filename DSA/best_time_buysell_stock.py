class Solution:
    def maxProfit(self, prices):
        left_idx = 0
        max_profit = 0

        for right_idx, price in enumerate(prices):
            if price > prices[left_idx]:
                max_profit = max(max_profit, price - prices[left_idx])
            else:
                left_idx = right_idx

        return max_profit
        
