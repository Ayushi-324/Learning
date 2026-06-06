def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()  #ek single hash set sb try krne ko
        
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':   #agar cell khali ignore
                    continue

                row_key = (r, val)  #unique descriptive string for rows, columns, and 3x3 boxes
                col_key = (val, c)
                box_key = (r // 3, c // 3, val)
                
                if row_key in seen or col_key in seen or box_key in seen: #agar inme se ek bhi string phle se dikhi boom 
                    return False
                
                seen.add(row_key)  #agar sb shi h toh set me daal do and aage chlo
                seen.add(col_key)
                seen.add(box_key)
                
        return True

# SINGLE PASS HASH SET PATTERN- jb bhi grid me multiple constraints (row, col, region) ek sath check use this unique key generation hashing pattern 
# TIME COMP - O(1) constant time as board hamesha 9*9 size ka h so total 81 loops if board n*n so O(n2)
# SPACE COMP - O(1) const space as set ke andr max strings limited as grid fixed 

