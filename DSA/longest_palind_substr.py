class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""   #edge case

        start = 0  
        end = 0

        def find_ans(left: int, right:int)->int:   # helper fn L R dono indices pe hath failana so main loop me ise bar bar call
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1  #move left backward 
                right += 1

            return right - left - 1 #return len of pal &after expan lr pointer ek kdm bhr chale jate so -1  

        for i in range (len(s)):  #main loop code starts here & this find_ans would be called to just expand
            len1 = find_ans(i, i)  #SINGLE center - odd palindrome ex - aba me center b and LR at b nd expand 
            len2 = find_ans(i, i+1) #DOUBLE CENTER- Even pali ex - abba no mid letter so L on first b and R on second b (i+1)

            max_len = max(len1, len2) #jo bhi badi len as WE'RE CHECKING BOTH ODD EVEN SITUATION ek saath 

            if max_len > (end - start):  #update old record
                start = i - (max_len - 1) // 2  #pali start index find (center i se dono side barbar letters bantna)
                end = i + max_len // 2 #last index 

        return s[start : end + 1]  #slicing only that pali part +1 include last index 


