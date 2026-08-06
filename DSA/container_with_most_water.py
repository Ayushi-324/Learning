class Solution:
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        total_water = 0

        while l < r:
            width = r - l
            h = min(height[l], height[r])
            total_water = max(total_water , width * h)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return total_water

# TWO POINTER (GREEDY APPROACH)   time -O(n) arr traverse once  space -O(1) l r used

# PANI ALWAYS CHOTI DIWAR JITNA BHAREGA -> har step pe area nikalne ke baad sirf us pointer ko hila jiski height choti (shorter wall andr move)
