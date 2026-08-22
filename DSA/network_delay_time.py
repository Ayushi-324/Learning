import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # 1. Graph banao: {source_node: (neighbor, weight)}
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
            
        # 2. Min-Heap me daalo starting state: (time, source_node)
        pq = [(0, k)]
        
        # 3. Har node tak pahunchne ka minimum time store karne ke liye
        visited = {}
        
        while pq:
            # Hamesha sabse kam time wala node pehle niklega
            time, node = heapq.heappop(pq)
            
            # Agar is node ka better/shorter rasta pehle hi mil chuka hai toh skip karo
            if node in visited:
                continue
            visited[node] = time
            
            # Ab iske saare padosi (neighbors) ko check karo
            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    # Naya total time = abhi tak ka time + edge ka weight
                    heapq.heappush(pq, (time + weight, neighbor))
                    
        # 4. Agar saare nodes tak signal pahunch gaya toh max time return karo, nahi toh -1
        return max(visited.values()) if len(visited) == n else -1
