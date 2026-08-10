class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # Agar slope up ja rha hai, to peak right side mein hoga
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            # Agar slope down ja rha hai, to peak left side ya mid par hoga
            else:
                right = mid
                
        return left
