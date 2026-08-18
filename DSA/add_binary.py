class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        i = len(a) - 1  # a ka piche se pointer
        j = len(b) - 1  # b ka piche se pointer
        carry = 0       # haasil (carry) zero se suru
        
        # jab tak digit bachi hai ya carry bacha hai
        while i >= 0 or j >= 0 or carry:
            total = carry  # pehle pichla carry add karo
            
            if i >= 0:
                total += int(a[i])  # a ka bit jodo
                i -= 1
            if j >= 0:
                total += int(b[j])  # b ka bit jodo
                j -= 1
                
            carry = total // 2      # naya carry nikalo
            res.append(str(total % 2))  # bacha hua bit list me daalo
            
        return "".join(res[::-1])  # list ko ulta karke string banao

#Two-Pointers (Right-to-Left) + Math Simulation  time- O(max(n,m)) dono str ke hr char pe traverse once   space - O(max(n,m)) o/p str store

