class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1  #goal ko last indep pr set

        for i in range(len(nums) - 2, -1, -1):  #piche se shuru krke index 0 tk 
            if i + nums[i] >= goal:  #agr is jgh se jump mar ke purane goal tk poch skte h
                goal = i #naya goal curr index bangya

        return goal == 0  #agr goal index 0 tk pochgya mtlb rasta c
