class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []
        nums.sort() #sort array so duplicates can be skipped 

        for i in range (len(nums)):
            if i > 0 and nums[i] == nums[i-1]:  #agar i ki value pehle wali i jesi h skip it
                continue  # for skip in python

            l = i + 1  # l i se aage wala
            r = len(nums) - 1
            
            while l < r:
                total = nums[i] + nums[l] + nums[r] #two sum logic 

                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])  #jackpot triplet mila save it baki dhundenge 

                    while l < r and nums[l] == nums[l +1]: #to skip duplicates l r dono side se 0 milne pe ye cond check
                        l += 1
                    while l < r and nums[r] == nums[r -1]: # l and r jab tk aage piche aate h jb tk naya no na mile pehle se 
                        r -= 1

                    l += 1 #ek step aur aage chlo to find new combination
                    r -= 1

        return result


# CONFUSING BUT INTERESTING Question :-) arr sort kro rk no fix kro(i) and baki do ke liye 2 pointer and duplicate trap i ke liye and pointer shifting ke liye while  
# TIME COMP - > O(N2) as ek loop andr two pointer linear scan but sorting time o(nlogn)
# SPACE COMP -> O(1) but python uses timesort which takes o(n) auxiliary space
#PATTERN -> unique/triplet/quadruplet and sum/target puche think of SORTING + TWO POINTERS
