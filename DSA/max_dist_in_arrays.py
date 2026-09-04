class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        min_val = arrays[0][0] #phle arr se min & max start kr
        max_val = arrays[0][-1]
        max_dist = 0

        for i in range(1, len(arrays)):  #loop on other arrays
            current_min = arrays[i][0]
            current_max = arrays[i][-1]
            
            max_dist = max(max_dist,   #cross-diff check krke max dist update
                           abs(current_max - min_val), 
                           abs(max_val - current_min))
    
            min_val = min(min_val, current_min) #global min nd max upda for next iteration
            max_val = max(max_val, current_max)
            
        return max_dist
#greedy/pre compute    t-O(m) 1pass  s-O(1)

comp curr arr boundaries with prev global min/max to ensure elem come from diff arrays
