class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        coln = len(matrix[0])

        first_row_zero = False   #STEP 1 -> border zero ko backup flags bana 
        first_coln_zero = False

        for r in range(rows):   #check sbse upr wali row 0 me phle se koi zero?
            if matrix[r][0] == 0:
                first_coln_zero = True

        for c in range(coln):   #check sbse left wale col 0 me phle se koi 0?
            if matrix[0][c] == 0:
                first_row_zero = True

        for r in range(1, rows):  #STEP 2-> andr wali matrix ko scan kr and border par flags lga 
            for c in range(1, coln): #starting from row 1 & coln 1 as border ka backup le chuke 
                if matrix[r][c] == 0:
                    matrix[0][c] = 0  #sbse upr wle header pr flag lga 
                    matrix[r][0] = 0  #sbse left wale header pr flag 

        for r in range(1, rows):    #STEP 3-> border flags dekh kr andr ka matrix zero ko 0 bna
            for c in range(1, coln):
                if matrix[0][c] == 0 or matrix[r][0] == 0: #agr uske upr wale header ya left header pr 0 
                    matrix[r][c] = 0

        if first_row_zero:   #STEP 4 -> last me backup flags dekh ke absolute borders ko zero kr 
            for c in range(coln):
                matrix[0][c] = 0   #left coln zero

        if first_coln_zero:
            for r in range(rows):
                matrix[r][0] = 0  #poori sbse upr wali roz zero 
              
# IN- PLACE ARR MANIPULATION,  time - O(m*n) linear scan, space - O(1) in-place tracking
#jha bhi 0 mile us puri row coln ko zero kr mgr comp bhul jata loop so we could have use set ki yha pe ye row col me 0 h but space so LOGIC - phle row 0 coln 0 ka backup liya , fir andr wale zeroes ka flag unhi ke seedhe upr ya left border(row0, col0) pr lga diya and last me un nishan ko dekhke sab saaf krdiya.



        
