from collections import Counter #python diary to count char fast

class Solution:
    def minWindow(self, s: str, t: str) -> str: 
        if not t or not s:  #if s and t empty
            return ""

        target_dict = Counter(t)  #{A: 1, 'B':1, C:1}    
        need = len(target_dict)  # kitne unique char need ex- t=ABC so 3 

        l, r = 0, 0 # two pointers l nd r set
        formed = 0 #counter to tell unique char of t in window later

        window_counts = {}  #to store letters char count during window

        ans = float("infinity"), None, None  # to track smallest ans shuru me inf so real ans would be small

        while r < len(s):    #jb tk r string s ke last letter tk
            character = s[r]   # r jis char pr use character variable name
            window_counts[character] = window_counts.get(character, 0) + 1  #uski ginti +1

            if character in target_dict and window_counts[character] == target_dict[character]:
                formed += 1 #if vo char in our target dict and in window its count is what req so formed move

            while l <= r and formed == need: #loop until sb need char in window
                character = s[l] # checking l kispe khada h 

                if r - l + 1 < ans[0]:  #if curr window len is small then old saved ans update in ans l,r coord
                    ans = (r - l + 1, l, r)
                    
                window_counts[character] -= 1 #char out of window as l moving for 
                if character in target_dict and window_counts[character] < target_dict[character]:
                    formed -= 1 #this window is not vaild now 

                l += 1 #window left se choti hogyi

            r += 1 #so next char include in window

        return "" if ans[0] == float("infinity") else s[ans[1] : ans[2] + 1]  #if ans len inf even after loop so return "" else slice krke ans us l pointer and r tk ka text  
                        
# r- l+1 is abhi ki window len
