 def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:  # pointers cross tk loop and = check that last element too when both l and h there
            mid = (low+high) // 2

            if nums[mid] == target:    #direct match check 
                return mid

            if nums[low] <= nums[mid]:  # agr left side perfectly sorted hai

                if nums[low] <= target < nums[mid]:  # check if target there
                    high = mid - 1  #left me search
                else:
                    low = mid + 1   # right me jump 

            else:  #right side perfectly sorted 
                if nums[mid] < target <= nums[high]:  #check if right range me target
                    low = mid + 1
                else:
                    high = mid - 1

        return -1 #element nhi mila array me

#PATTERN -> Modified binary search .......logic is any rotated array divided by  mid has always one side normal sorted ....RULE -> agr pehla element aakhiri element se chota ya equal then that range sorted
# MID nikalo -> sorted side find-> check if target in that range else other side -> apply binary search there me pura search space aadha krna
# time complexity - O(logn) as hr br search space aadha...SC- 0(1) no extra space 
