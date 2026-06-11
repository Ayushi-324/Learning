class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0

        def expand(l,r):    # Helper function to expand from center and count palindromes
            nonlocal ans #bahar wale ans variable ko andar change krne ko 

            while l >= 0 and r < len(s) and s[l] == s[r]:  #jb tk string ke andr and letter match 
                ans += 1  #ek pal mila
                l -=1   #l ek step piche 
                r += 1

        for i in range(len(s)): #string kr har char ko bari bari center maana 
            expand(i,i)   #odd single center 
            expand(i, i+1) #even 

        return ans 

# TWO POINTER APPROACH 
# har char ko center maan lo then expand and check palindrome hai ? ex - aba center b(l,r=b) check b==b yes then a==a yes pal if even length ex - abba toh center bb(l=b,r=b) a == a yes pali 
# Palindrome + Substring + Count -> EXPAND AROUND CENTER 
# expand(i, i) means starts from the same char (ODD PAL).....expand(i, i+1) start from gap bw two char (EVEN PAL)
# TIME COMP- O(N2) as there are 2n -1 possible center har center ke expand me o(n) time .....SPACE - O(1) used pointers only
