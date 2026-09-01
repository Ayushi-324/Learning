class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        # Copy banakar sort kiya taaki exact halves milein
        arr = sorted(nums)
        n = len(nums)
        
        # Reverse se filling start ki taaki duplicates pass-pass na aayein
        mid = (n - 1) // 2  # Smaller half end pointer
        end = n - 1         # Larger half end pointer
        
        for i in range(n):
            if i % 2 == 0:
                nums[i] = arr[mid] # Even index par dips
                mid -= 1
            else:
                nums[i] = arr[end] # Odd index par peaks
                end -= 1
