class Solution:
    def calculateMinimumHP(self, dungeon: list[list[int]]) -> int:
        rows, cols = len(dungeon), len(dungeon[0])
    
        for r in range(rows - 1, -1, -1): #bottom up traver kro matrix me
            for c in range(cols - 1, -1, -1):
    
                if r == rows - 1 and c == cols - 1: #bottom right corner(princess spot)
                    dungeon[r][c] = max(1, 1 - dungeon[r][c])
                    
                elif r == rows - 1: #last row(bs r ja skte)
                    dungeon[r][c] = max(1, dungeon[r][c+1] - dungeon[r][c])
                    
                elif c == cols - 1: #last c (bs down)
                    dungeon[r][c] = max(1, dungeon[r+1][c] - dungeon[r][c])
                    
                else:  #beech ke cells (r down ka min)
                    min_health_needed = min(dungeon[r+1][c], dungeon[r][c+1])
                    dungeon[r][c] = max(1, min_health_needed - dungeon[r][c])
                    
        return dungeon[0][0] # Starting gate par zaroori min health
