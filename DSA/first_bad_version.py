class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        
        while left < right:
            # Middle point
            mid = left + (right - left) // 2
            
            if isBadVersion(mid):
                # Answer left side hai
                right = mid
            else:
                # Answer right side hai
                left = mid + 1
                
        # First bad version
        return left

# BINARY SEARCH - data is sorted & have to find specific switching point (first bad version)
#TIME COMP - O(logn) hr step pe search aadhi
#SPACE - O(1) only three pointers l , r mid used
