from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Magazine chars ka count lo
        magazine_counts = Counter(magazine)
        
        # RansomNote chars ka count lo
        ransom_counts = Counter(ransomNote)
        
        # Dono counts ko compare karo
        for char, count in ransom_counts.items():
            # Agar magazine me char kam hai toh False
            if count > magazine_counts[char]:
                return False 
                
        # Agar saare mil gaye toh True       
        return True 

#Time Complexity: O(m + n) (Dono strings ko ek baar scan kiya)
#Space Complexity: O(1) (Maximum 26 unique characters hash map mein)
