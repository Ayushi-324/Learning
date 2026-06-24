class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0   #ghr khali pesa 0

        prev_house1 = prev_house2 = 0 # dono purane ghr ka pesa start me 0 

        for num in nums:
            money = max(prev_house1 , prev_house2 + num) #max( ghr chhoda, ya phir pichla chod kr curr loota)

            prev_house2 = prev_house1  #variables ek ek step aage khiskao 
            prev_house1 = money

        return prev_house1  #aakhiri ghr tk ka max money loota hua

# Linear dp(pick/ skip)  time - O(n) har ghr ek baar visit,  space - O(1) only two variables
# LOGIC - har kadam pe do raste - ya toh abhi wala loot aur pichla chhod , ya phir abhi wala chod  aur pichle se khush reh 
