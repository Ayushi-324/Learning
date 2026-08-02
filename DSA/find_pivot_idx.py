class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)  # Total sum nikaal lo
        left = 0           # Left side ka sum starting me 0
        
        for i, num in enumerate(nums):
            # Right sum = Total - Left - Current number
            if left == (total - left - num):
                return i   # Pivot mil gaya!
                
            left += num    # Left sum update karo
            
        return -1          # No pivot found


# PREFIX SUM      time- O(n) arr traverse twice once initial total sum then locate pivot index              space - O(1) total_sum, left_sum var used
