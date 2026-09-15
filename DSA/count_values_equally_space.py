class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        d = {}
        for i in range(len(nums)):
            val = nums[i]
            if val not in d:
                d[val] = []
            d[val].append(i)

        ans = 0
        for k in d:
            arr = d[k]
            if len(arr) == 3:
                if arr[1] - arr[0] == arr[2]-arr[1]:
                    ans += 1

        return ans
