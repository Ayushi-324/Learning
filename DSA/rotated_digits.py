class Solution:
    def rotatedDigits(self, n: int) -> int:
        count = 0
        
        # Invalid aur changing digits define karein
        invalid_digits = {'3', '4', '7'}
        changing_digits = {'2', '5', '6', '9'}
        
        for i in range(1, n + 1):
            s = str(i)
            # 1. Agar ek bhi invalid digit hai -> skip karo
            if any(char in invalid_digits for char in s):
                continue
            # 2. Kam se kam ek changing digit hona chahiye -> count++
            if any(char in changing_digits for char in s):
                count += 1
                
        return count
