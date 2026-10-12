class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums) #array total len saved in n variable

        output = [1] * n #o/p name khali array jisme sb jagah 1 h abhi

        prefix = 1   #left side product calculate 
        for i in range(n):  #loop from 0 to n-1
            output[i] = prefix   #abhi tk ka left ks prefix in output array
            prefix *= nums[i]   # for next element abhi wale no ko prefix me * krke update

        suffix = 1 
        for i in range(n-1, -1, -1):  #ulta loop last element(n-1) se 0 tk
            output[i] *= suffix #purane left product ko right se * 
            suffix *= nums[i]  #pichle index ke liye update 

        return output

# right side ke product live multiply kiya peeche se ....taki right side ka ready made product mile hme br br aage loop krke multiply nhi krna hota ex - 4 ke liye 10-5 tk ka * already h alag se loop chala ke 5*6*.....dobara nhi krna variable ne reuse de diya so mem save\

#output = [1] * n -> initialize op array with 1s taki mem me contigous block allocate ho
