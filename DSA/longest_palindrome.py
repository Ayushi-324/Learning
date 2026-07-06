class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Count frequencies of each character
        counts = Counter(s)
        
        length = 0
        has_odd = False
        
        for count in counts.values():
            # Add the largest even part of the count
            length += (count // 2) * 2
            
            # Check if there is an odd frequency
            if count % 2 == 1:
                has_odd = True
        
        # If any character has an odd count, one can sit in the center
        return length + 1 if has_odd else length

#Logic:Take all pairs (count // 2 * 2).Add 1 at the end if any odd count exists (for the exact center).
#Time: O(N) — One pass to count.....
#Space: O(1) — Max 52 characters....
