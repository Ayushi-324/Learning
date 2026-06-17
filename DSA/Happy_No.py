class Solution:
    def isHappy(self, n: int) -> bool:
        def happy_hu(number: int)-> int:  #helper f'n to avoid calculating square sum again n again
            total_sum = 0
            while number > 0: #jb tk no 0 se bada uske digits alag krke square jod 
                number, digit = divmod(number, 10) #ex - 19 ko toda number =1 , digit = 9
                total_sum += digit ** 2 # digit ka square krke total sum me jod diya
            return total_sum

        slow = n
        fast = happy_hu(n)
        
        while fast != 1 and slow != fast:
            slow = happy_hu(slow)
            fast = happy_hu(happy_hu(fast))
            
        return fast == 1

# hash set () use krne me mem O(n) jayegi ..(har nikale no ko set me save agar koi no dobara aaye toh loop)
# TIME COMP -> 0(Logn) as hr bar no ke digits pr calculation and using log10 scale , SPACE -> 0(1) as no set only fast/slow
# divmoid(no, 10) python shotcut pc can"t see 1&9 seperately for that divide by 10 ----no//10 gives quotient nd remove last digit and no%10 remainder gives last digit ,,,,,,,,so number me bacha hua chota no jata digit me alag hua last digit 
        # COMP EK BAR ME EK (DIGIT) DEKHEGA LAST WALI -  divmod(19,10) = (digit - 9, no 1) sum = 9**2 81 so total_sum = 81 then SECOND LOOP me while 1 > 0 so divmoid(1,10)digit =1 and no = 0 (remainder) so sum = 1**1 = 1 and 81 + 1 = 82 ------loop stops as now no is 0
