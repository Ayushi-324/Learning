class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_p = min_p = ans = nums[0] #ex - [2,3,-1,4] nums me 0 index pr h 2 so shuru me initialize all as 2

        for i in range(1, len(nums)):  #loop index 1 se last element tk jayegi
            curr = nums[i]
            temp_max = max_p #python line by line interpret krta h if i update max_prod first uski purani value delete hojayegi so save it 

            max_p = max(curr, curr*max_p, curr*min_p)
            min_p = min(curr, curr*temp_max, curr*min_p)

            ans = max(ans, max_p)

        return ans

# PATTERN -> Kadane Variant normal kadane is max sum but here max product as negative * n = positive (aaj ka min kal ka max ban skta h)
# TIME COMP-> O(n) bs ek bar loop chala , SPACE -> O(1) no extra space
# so we need both curr max and curr min so keep both curr min jruri hai negative se khel palat skta h 
# simple h tere pas teen choices h ya toh vo num(curr) khud ya phir naya no*max_p, nayano*min_p) 
# temp max_p save krke chalna kyunki computer aandha hai ex - vo 2*3 = 6 max hai but if can't save vo -2 me max _2 lelega )
# SLIDING WINDOW Ka khayal aaya tha but -ve no h fix nhi ho payega subarray 
