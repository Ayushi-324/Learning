class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1   #starting range 1 se num tk 
        right = num

        while left <= right: #loop until range valid 
            mid = (left + right) // 2
            square = mid * mid 

            if square == num:
                return True

            elif square < num:
                left = mid + 1  #range left boundary aage bdha 

            else:
                right = mid - 1

        return False
