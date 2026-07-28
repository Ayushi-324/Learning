from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []

        queue = deque()  #to store indices
        res = [] #ans list store

        for i in range(len(nums)):
            while queue and nums[queue[-1]] <= nums[i]: #vo indices hta piche se jo smaller than curr element
                queue.pop()

            queue.append(i) #add curr elem index to the back

            if queue[0] == i-k: # front index hta agr boundary se bhar h 
                queue.popleft()

            if i >= k - 1: #phli window puri ho max q[0] out me dal 
                res.append(nums[queue[0]])

        return res
      
# bade ke aate hi chote ko laat maro -> naya elem piche se aaya agar bada h toh chote ko piche se hu nikal dega -> agr purana elem h sbse aage se jayega -> for ans sbse aage wala h 
#monotonic deque    time -O(n) hr elem add/rem at most once   space- O(k) 
