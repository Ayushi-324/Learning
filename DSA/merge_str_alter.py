class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        i, j = 0, 0
        m, n = len(word1), len(word2)
        
        # Ek-ek karke dono strings se characters uthao
        while i < m and j < n:
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1
            
        # Jo bhi string badi thi, uska bacha hua part end me jodo
        if i < m:
            res.append(word1[i:])
        if j < n:
            res.append(word2[j:])
            
        # List ko string me convert karke return karo
        return "".join(res)
