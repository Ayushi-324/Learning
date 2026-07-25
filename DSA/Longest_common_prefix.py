class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        base = strs[0] #pehli str(word) ko base maan

        for i in range(len(base)):  #base word ke hr index pr loop
            for word in strs[1:]: #check other words except 1st
                if i == len(word) or word[i] != base[i]:  #agr word khatam or mismatch 
                    return base[:i] #vhi tk ka hissa slice

        return base  

# VERTICAL SCANNING   time - O(s)      space- O(1) 
