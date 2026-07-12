class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF  # 32-bit integer ki boundary
        
        while b & mask != 0:  # Jab tak carry bache hain tab tak chalega
            carry = (a & b) << 1
            a = (a ^ b) & mask  # Bina carry ka jod + mask binding
            b = carry & mask    # Naya carry + mask binding
            
        # Agar number negative boundary (0x7FFFFFFF) se bada hai toh convert karo, nahi toh a return karo
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)

# ^ (XOR) → Addition (bina carry ke)           & << 1 → Carry (aage bhejna)
# BITWISE MANIPULATION       time - O(1) bit len 32 fix     space - O(1) variables limited no extra arr
