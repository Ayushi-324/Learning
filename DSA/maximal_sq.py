class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
            
        cols = len(matrix[0])
        heights = [0] * (cols + 1) # Extra cell edge logic - simple close krne ko
        max_area = 0
        
        for row in matrix:
            for i in range(cols): #upward geugh arr build kr r metrics use krke
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
        
            stack = [] # Indicies track storage system  , largest rect in histogram calcul lga
            for i in range(len(heights)):
                while stack and heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)
                
        return max_area
