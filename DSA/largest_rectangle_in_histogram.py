class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0) #sentinal 0 add
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:  # jb tk curr h choti h stack top se 
                pop_index = stack.pop()
                height = heights[pop_index]  #pop hone wale ki height

                width = i if not stack else i - stack[-1] - 1  #width

                max_area = max(max_area, height * width)

            stack.append(i)  #push

        return max_area
