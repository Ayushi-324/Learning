class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [0] * n  # Result array to store squares
        
        # Two pointers: largest absolute values are always at the boundaries
        left, right = 0, n - 1
        
        # Fill res from right to left (largest to smallest square)
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                res[i] = nums[left] ** 2
                left += 1  # Move left pointer inner
            else:
                res[i] = nums[right] ** 2
                right -= 1  # Move right pointer inner
                
        return res
# Two-Pointer (Collision / Boundary Type)    time- O(n) single pass loop      space- O(1) if o/p mem excluded
