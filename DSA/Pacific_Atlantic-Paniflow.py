class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows = len(heights)
        cols = len(heights[0])

        #BOUNDARY SETUP(queue ready krna)
        pacific_queue = deque()
        atlantic_queue = deque() #do lines(queue) banaye coordinates dalne ko

        pacific_visited = set() #checking (r,c) in visited 
        atlantic_visited = set() #do registers(hashmap for graph) to remember kis-kis pr flag lg chuka

        for r in range(rows): #kinaro ko queue me dalna
            pacific_queue.append((r,0))   #bilkul left wali line(col 0)    LEFT EDGE-> PACIFIC
            pacific_visited.add((r, 0))   #turant pacific ka flag laga diya 

            atlantic_queue.append((r, cols-1))  #bilkul right wali line   RIGHT EDGE -> ATLANTIC
            atlantic_visited.add((r, cols-1))

        for c in range((cols)):
            pacific_queue.append((0, c))  #TOP EDGE-> PACIFIC
            pacific_visited.add((0, c))  

            atlantic_queue.append((rows-1, c))   #BOTTOM EDGE-> ATLANTIC
            atlantic_visited.add((rows-1, c))

        def bfs(queue, visited):  #helper f'n to run bfs climbing up to the mountain
            while queue:
                r, c = queue.popleft() #line me se sbse aage khade cell ko bahar

                for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]: #to check in all four directions 
                    nr, nc = r + dr, c + dc  #naya padosi (new row, new col)

                    if 0 <= nr < rows and 0 <=nc < cols and (nr, nc) not in visited: #BOUNDARY CHECK matrix ke bahar nhi and visited check kya is padosi pr pehle se flag h 
                        if heights[nr][nc] >= heights[r][c]:  #LAW OF PHYSICS- agar padosi ki height badi ya barabar tabhi samandar se upar pahad(island) jana
                            visited.add((nr, nc))   #padosi pr flag 
                            queue.append((nr, nc))   #padosi in line so uske aage check ho 

        bfs(pacific_queue, pacific_visited)  #running bfs for bothy oceans independently 
        bfs(atlantic_queue, atlantic_visited)

        return list(pacific_visited.intersection(atlantic_visited))  #find common coordinates jaha both flag are true (intersection)


# pani hamesha niche ki taraf behta hai like chat se pahad se , yaha pe ek block se dusre block(e,w,n,s) tabhi jayenge jb samne wale block ki height equal ya choti ho  hume bs pure island pe vo khas spots(cells) dhundne jaha agr barish ho toh pani waha se behke pacific ocean and atlantic dono me jaye 

# agar har cell se niche ki taraf raste dhundna bhot time lgega so ulta krte h oceans ke kinare khade hoke aur pahad(island) ki taraf chadna shuru krte us case me height barbar ya jyada honi chahiye to dono side se chalte h pacific ke sare kinaro se bhi and atlantic se bhi and visited krte jayenge toh jha dono rang ke flags honge yani dono true vo ans 

# DFS is fine but bfs better h kinare se shuru krke unchi heights pe flags lgate hue chalenge so traversal ke liye samandar ke sare kinaro ko ek saath queue me dal ke level by level upar chado 

# TIME COMP -> O(m*n) kyunki hr cell processed ek constant no of times in bfs, SPACE -> O(m*n) to store visited states and bfs queue
# this is a multi source BFS Pattern ek point se start na krke entire boundary se start krte h ek sath 
