class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:  # 1 ya 2 seedhe me utne hi raste 
            return n

        prev2, prev1 =1, 2  # prev 2 means 2 step piche (1st seedhi) & prev 1- one step piche (2nd seedhi) as hr step pe pichli do seedhi ya ghr ka rasta yaad rkhna 

        for i in range(3, n+1):  #loop 3rd seedhi as 1 2 way already known 
            current = prev1 + prev2  # 2 + 1 = 3
            prev2 = prev1  #Purani 1st step waali ab 2 step peeche ho gayi
            prev1 = current #curr ab 1 step piche 

        return prev 1
