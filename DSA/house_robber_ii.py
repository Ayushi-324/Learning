class Solution:
    def rob(self, nums: list[int]) -> int:
        # Agar sirf ek ghar hai, toh bas wahi loot lo
        if len(nums) == 1:
            return nums[0]
        
        # Helper function linear House Robber solve karega
        def helper(arr):
            prev1, prev2 = 0, 0
            for num in arr:
                # Max loot ya toh current ghar chhod kar milegi ya le kar
                temp = prev1
                prev1 = max(prev2 + num, prev1)
                prev2 = temp
            return prev1
        
        # 2 cases: pehla ghar chhod do OR aakhiri ghar chhod do
        return max(helper(nums[:-1]), helper(nums[1:]))
