class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []    #list store all final valid combinations
 
        def dfs(left, right, s):  
            if len(s) == 2 * n:  #BASE CASE - if string is full save it and stop
                ans.append(s) # add string s to ans  
                return
            
            if left < n:  #choice 1 -> add ( and move to the next step 
                dfs(left + 1, right, s + "(") # s + ( creates new string with ( added to the end left + 1 updates open counter
                
            if right < left: # if curr have more ( than close in string - choice 2 
                dfs(left, right + 1, s + ")")

        dfs(0, 0, "")  #stat fn with 0 open, 0 close, and empty string 
        return ans
