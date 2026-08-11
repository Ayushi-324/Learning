class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        
        #SWAP TRICK: Har number x ko uske sahi ghar (index x-1) par bhej
        for i in range(n):
            # Agar number 1 se n ke beech hai, aur apne sahi ghar par nahi hai -> SWAP!
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
                
        # CHECK TRICK: Pehla konsa ghar hai jisme galat banda baitha hai
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1 # Wahi index + 1 missing hai
                
        #EDGE CASE: Agar 1 se n tak sab line se hain, toh agla number missing hai
        return n + 1
