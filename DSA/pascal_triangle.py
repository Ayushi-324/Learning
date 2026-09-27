class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = []

        for i in range(numRows):
            # 1. Pehle puri row ko 1 se bhar do
            row = [1] * (i + 1)
            
            # 2. Beech wale numbers = Upar wali row ke padosi numbers ka sum
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
                
            triangle.append(row)
            
        return triangle
