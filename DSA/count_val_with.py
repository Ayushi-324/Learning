class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        d = {}    #dict me indixes store 
        for i in range(len(nums)):
            val = nums[i]
            if val not in d:
                d[val] = []
            d[val].append(i)

        ans = 0
        for k in d:
            arr = d[k]
            if len(arr) >= 3:
                diff = arr[1] - arr[0] #phle do indices ka gap 
                valid = True

                for j in range(2, len(arr)):
                    if arr[j]- arr[j-1] != diff:
                        valid = False
                        break

                if valid:
                    ans += 1
