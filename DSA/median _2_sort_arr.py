class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):  #choti arr pe binary search for speed 
            nums1, nums2 = nums2, nums1  # for swap write in single line

        m = len(nums1)
        n = len(nums2)
        total_left = (m + n + 1) // 2  #left side kitne elem chahiye +1 for odd

        left = 0   #binary search pointers for shorter arr
        right  = m

        while left <= right:
            i = (left + right) // 2   #arr 1 cut point 
            j = total_left - i    #arr 2 automatic cut point 

            left1 = nums1[i - 1] if i > 0 else float('-inf')  #Deewar ke paas waale 4 numbers nikalo (Edge cases handle karte hue)
            right1 = nums1[i] if i < m else float('inf')
            
            left2 = nums2[j - 1] if j > 0 else float('-inf')
            right2 = nums2[j] if j < n else float('inf')

            if left1 <= right2 and left2 <= right1:   #Tircha (Cross) Check
                 if (m + n) % 2 == 1:  # Agar Perfect Cut mil gaya
                    return float(max(left1, left2))   # Odd total: Left ka sabse bada number
                 return (max(left1, left2) + min(right1, right2)) / 2.0 # Even total: Average

            elif left1 > right2:   #Agar cut galat hai, toh pointers ko khiskao
                right = i - 1   # Array 1 ka cut peeche khiskao
            else:
                left = i + 1  

# median is bich ki line where left elem right ke = ya ek jyada for odd 
        
