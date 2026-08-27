class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix [0]:
            return False

        rows = len(matrix)
        coln = len(matrix[0])

        r = 0
        c = coln - 1 #top right corner elem se start as (iske l sare elem chote niche ke sb bde)

        while r < rows and c >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                c -= 1      #left move for smaller no 
            else:
                r += 1            #down bde no 
           

#target chota left ja (col-= 1), bda neeche ja (row += 1) 
# 2 pointer as matr not sorted linearly(row 1 start row 0 end se chota)
#STAIRCASE SEARCH (2d pointer search)           t - O(r+c) wc me either go all left or down    s- O(1) 2pointers r c 
