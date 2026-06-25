class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} #map for letters count
        max_freq = 0  # longest repeating letter count in a window (hero)
        left = 0
        max_len = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1  #naya char aaya count bdhao and update hero
            max_freq = max(max_freq, count[s[right]])  

            if (right -left + 1) - max_freq > k: #(window size -hero) = villains . agr ye k se bada h toh window choti kr 
                count[s[left]] -= 1
                left += 1  

            max_len = max(max_len, right - left + 1) # hr step pe sbse badi valid window save krtegye

        return max_len

# SLIDING WINDOW (variable size)   time - O(n) pura arr scan once , space - O(1) max 26 uppercase english letter count track 

# LOGIC - window me sbse jyada aane wala letter apna hero h , baki sare letters villain h jinhe badalna hai ....agr villains ka count (window_size - hero_count) < k hojaye toh left pointer aage bdha ke window choti 

# so we're tracking the max frequency of any single char . if the count of the other char exceeds k we shrink the window from left 
