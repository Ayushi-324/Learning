class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        low, high = max(nums), sum(nums) ## Range: Max element se Total sum tak

        while low < high:
            mid = (low + high) // 2

            chunks, curr_sum = 1, 0 #arr split checklist inline 
            for num in nums:
                if curr_sum + num > mid:
                    chunks += 1   #naya grp
                    curr_sum = num
                else:
                    curr_sum += num  #same grp me add

            # Range adjustment chunk count base pe 
            if chunks <= k:
                high = mid  # mid valid - check chota sum
            else:
                low = mid + 1  # Bada sum dhund

        return low
