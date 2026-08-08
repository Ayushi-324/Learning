class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                # Swap the 0 to the low section
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # 1 is already in its correct relative place (middle)
                mid += 1
            else:  # nums[mid] == 2
                # Swap the 2 to the high section
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

# DUTCH NATIONAL FLAG ALGO    time & space - O(1) 
3 pointer algo jo arr ko 3 hissso me bantegi  -> low p ke phle sare 0 ,    mid p arr ko check krte hue aage chlta       high ke bad sare 2 
