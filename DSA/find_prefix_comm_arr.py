class Solution:
    def findThePrefixCommonArray(self, A: list[int], B: list[int]) -> list[int]:
        n = len(A)
        ans = []
        
        # Numbers 1 se N tak hain, isliye size N + 1 liya
        freq = [0] * (n + 1)
        common = 0
        
        for i in range(n):
            # Element from A
            freq[A[i]] += 1
            if freq[A[i]] == 2:
                common += 1
                
            # Element from B
            freq[B[i]] += 1
            if freq[B[i]] == 2:
                common += 1
                
            ans.append(common) # Har index pe answer store karo
            
        return ans
