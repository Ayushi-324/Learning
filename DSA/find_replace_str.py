class Solution:
    def findReplaceString(self, s: str, indices: list[int], sources: list[str], targets: list[str]) -> str:
        # Indices ko bade se chote order me sort karo data mapping ke sath
        for idx, src, tgt in sorted(zip(indices, sources, targets), reverse=True):
            
            # Agar original substring exact spot par match ho gayi
            if s[idx : idx + len(src)] == src:
                # Direct string chunk patch replacement
                s = s[:idx] + tgt + s[idx + len(src):]
                
        return s
#reverse sorted simulate (desc idx slicing)   t-O(n+klogk) s-O(n+k)
