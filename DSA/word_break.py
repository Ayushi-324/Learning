class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        hash_set = set(wordDict) #fast 0(1) search 
        n = len(s)  #string length
        
        dp = [False] * (n+1)  #checklist array

        dp[0] = True #base case khali string true 

        for i in range(1, n+1):  
            for j in range(i):   #j is for cut 0-i tak khi bhi lg skta
                if dp[j] and s[j:i] in hash_set: 
                    dp[i] = True #current part valid
                    break  #next i pr jana
        
        return dp[n] 
