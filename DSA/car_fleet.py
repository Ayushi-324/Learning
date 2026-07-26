class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True) # # Pair position and speed, then sort by position descending
        stack = [] #store fleet leaders time

        for pos, spd in cars:
            time = (target-pos) / spd  #target tk jane ka time 
            if not stack or time > stack[-1]: #agr jyada time so car aage walo ko can't catch - naya fleet
                stack.append(time) #naye leader ka time in stack

        return len(stack) #fleet grp no

# monotonic stack/ sorting      time- O(nlogn) sort ki  space- O(n) to store car pairs and stack

# sort car closest to farthest calculate time for each agr aane wali car take more time than leader ahead it form new fleet and stack size ans
