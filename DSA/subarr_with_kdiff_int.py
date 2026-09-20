from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        def atMost(limit: int) -> int: #helper- count subarr atmost limit distinct no
            count = defaultdict(int)
            left = 0
            ans = 0
            
            for right, num in enumerate(nums):
                if count[num] == 0:
                    limit -= 1 # nya elem- capacity km
                count[num] += 1
            
                while limit < 0: #limit cross- l side se shrink
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        limit += 1 # elem pura hta - capaci bdhi
                    left += 1
                
                ans += right - left + 1 # Subarrays end hone wale elements count window me
            return ans
            
        return atMost(k) - atMost(k - 1) #formula apply

        
