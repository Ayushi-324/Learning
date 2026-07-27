class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1) 
        n2 = len(s2)

        if n1 > n2: #edge case agr s1 s2 se bda no permu
            return False

        s1_counts = [0] * 26 #26 letters arr- index 0 a 
        s2_counts = [0] * 26

        for i in range(n1): #s1 ke sare char and s2 phli window arr me save 
            s1_counts[ord(s1[i]) - ord('a')] += 1 #s1 char index me convert and freq bdhayi
            s2_counts[ord(s2[i])- ord('a')] += 1   #s2 ke phke n1 char in window 

        if s1_counts == s2_counts: #phli window me exact match found 
            return True

        for i in range(n1,n2):  #slide window across s2
             s2_counts[ord(s2[i]) - ord('a')] += 1   #naya char window me(right pointer)
             s2_counts[ord(s2[i - n1]) - ord('a')] -= 1  #purana char window se out, i-n1 left pointer

             if s1_counts == s2_counts:#cur_window match s1 char
                return True

        return False

        
# instead of hashmap use 26 char arr for quick memory access
# SLIDING WINDOW (FIX SIZE)   s1 ke sare char aur ginti map me -> s2 ke upr s1 jtni window bdha-> window aage jate hi naya char andr+ purana bhar - match hote hi true
# time - O(n2) N2 not square - n1+n2 as we scan at s1 s2 once         here m+n mtlb linear/sequential ek ke bad ek    BUT m*n nested/quadratic ek kam ke andr dusra kam bar bar 
#space - O(1) fixed size 26 int 
