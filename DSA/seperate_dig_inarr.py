class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        res = []  #har no ke digits temp list me nikal 
        for num in nums:
            temp = []
            while num > 0:
                temp.append(num % 10)  # Aakhri digit nikala (e.g., 13 % 10 = 3)
                num //= 10              # Number ko chhota kiya (e.g., 13 // 10 = 1)
            res.extend(temp[::-1])   #temp list ulta kr add in final res for correct order
        return res

#Digit Extraction / Pure Math    time O(n*k) total no*max dig in a no        space - O(k) ek no dig temp save
