class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:  #edge case khali string already sub
            return True

        if len(s) > len(t):
            return False 

        i = 0  # it's a two pointer strategy 
        j = 0
        len_s = len(s) #len of s string ka variable so shuru me hi len nikl gyi
        len_t = len(t)

        while i < len_s and j < len_t: #tb tk chlo until dono me se ek string puri khtm
            if s[i] == t[j]: #agar s letter and t lett match 
                i += 1  # s ke agle char pe chalo 

            j += 1 # t ka pointer toh aage bdhta hi hai 

        return i == len_s #agr i poori len tk pahuncha means we got all char 


# TWO POINTER APPROACH: s choti hi hogi toh usko direct t se match krte hai and while matching s ke char pr wait until u find it in t and t me aage bdhte rho until match na mile....jaise hi match s agle char pe jump agar s ke sare char khatam so t kitni bhi bdi ho still true if t puri khatam aur sare s nhi mile FALSE

# TIME COMP- O(N) as in worst case puri t string ko end tak scan krna hai
# SPACE COMP - O(1) i have not used any extra arr only two pointers 
