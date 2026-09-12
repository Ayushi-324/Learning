class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()  # Sort array to use two-pointer technique
        n = len(nums)
        res = []
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:  # Skip duplicate for 'i'
                continue
                
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:  # Skip duplicate for 'j'
                    continue
                
                left, right = j + 1, n - 1 #TWO POINTER SETUP
                
                while left < right:
                    curr_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if curr_sum == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        while left < right and nums[left] == nums[left + 1]: #move pointers nd skip dup
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                            
                        left += 1
                        right -= 1
                    elif curr_sum < target:
                        left += 1  #need bda sum
                    else:
                        right -= 1  #chota sum
                        
        return res
