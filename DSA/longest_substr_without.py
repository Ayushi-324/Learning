class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mem = {}
        left = 0 
        max_len = 0

        for right in range(len(s)):
            char = s[right]  #abhi loop is char pr h 

            if char in mem and mem[char] >= left: #kya char mem me h and kya rep char curr window me h
                left = mem[char] + 1

            mem[char] = right  #char ka naya index mem me save 

            max_len = max(max_len, right - left + 1) # e - l +1 is curr window len 

        return max_len     

