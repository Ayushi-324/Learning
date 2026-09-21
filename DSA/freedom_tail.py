class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        R, K = len(ring), len(key)
        memo = {}

        char_indices = {} #ring ke hr char ke sare indices store kr liye- fast lookup
        for i, c in enumerate(ring):
            if c not in char_indices: char_indices[c] = []
            char_indices[c].append(i)

        def dp(r_idx, k_idx):
            if k_idx == K: return 0 #base case- sb char spell hogye
            if (r_idx, k_idx) in memo: return memo[(r_idx, k_idx)]

            target_char = key[k_idx]
            min_steps = float('inf')

            for next_r_idx in char_indices[target_char]: #target char ke sb poss pos check
                dist = abs(r_idx - next_r_idx) #clockwise and anticl dono turn dist nikal
                steps_to_align = min(dist, R - dist) # Circular array wrap check
                
                total_steps = steps_to_align + 1 + dp(next_r_idx, k_idx + 1) #1 step button press krne ka jod kr aage recursion chlaya
                min_steps = min(min_steps, total_steps)

            memo[(r_idx, k_idx)] = min_steps
            return min_steps

        return dp(0, 0) # Shuruwat: 12:00 alignment index 0 par

        
