class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Edge Cases: Negative numbers and multiples of 10 (except 0) are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
            
        reversed_half = 0
        # Loop until we reach the middle of the number
        while x > reversed_half:
            # Pop the last digit from x and push it into reversed_half
            reversed_half = (reversed_half * 10) + (x % 10)
            x //= 10
            
        # For even lengths: x should equal reversed_half (e.g., 1221 -> x=12, reversed_half=12)
        # For odd lengths: discard the middle digit via reversed_half // 10 (e.g., 121 -> x=1, reversed_half=12)
        return x == reversed_half or x == reversed_half // 10
