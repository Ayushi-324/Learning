class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        # Helper function to find the bound of the target
        def findBound(isFirst: bool) -> int:
            left, right = 0, len(nums) - 1
            bound = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] == target:
                    bound = mid
                    if isFirst:
                        right = mid - 1  # Look left for first position
                    else:
                        left = mid + 1   # Look right for last position
                elif nums[mid] > target:
                    right = mid - 1       # Target is in the left half
                else:
                    left = mid + 1        # Target is in the right half
                    
            return bound

        # Execute binary search for both boundaries
        return [findBound(isFirst=True), findBound(isFirst=False)]

