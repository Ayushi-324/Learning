class Solution:
    def reverse(self, x: int) -> int:
        # BOUNDARIES: 32-bit signed limits
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # SIGN MANAGEMENT: Minus alag karo, positive pe loop chalao
        sign = -1 if x < 0 else 1
        x = abs(x)
        
        res = 0
        while x > 0:
            pop = x % 10  #  Aakhri digit nikaali
            x //= 10      # Number chota kiya
            
            # OVERFLOW GUARD: Kya agla step karne pe boundary cross hogi?
            if res > (INT_MAX - pop) // 10: 
                return 0
                
            res = res * 10 + pop # Safe hai toh pichle result me jod do
            
        return sign * res



#Digit Extraction (Math)     Time- O(log niche 10 N) hr step pe no 10 guna chota,  digits equal loops    space-O(1)
