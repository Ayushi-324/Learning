class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0   #n and n-1 ka bitwise AND kr

# BIT MANIPULATION  time -O(1) space -O(1) 

# hr power of 2 no 1 bit hota h ex - 4 bnega 8421 se 0010 but ek minus power of two me ex 3 toh vo akela 1 0 bnjayega nd aage ke sare 0 1 bnte ex 3 = 0011
so koi bhi 1 aamne samne nhi bachta toh AND unka 0 aata
