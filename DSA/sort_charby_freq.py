from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        # Sort characters by their frequency in descending order
        sorted_chars = sorted(count.keys(), key=lambda x: count[x], reverse=True)
        
        # Build the final string
        return "".join([char * count[char] for char in sorted_chars])

   
