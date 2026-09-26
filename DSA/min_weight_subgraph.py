import heapq
from collections import defaultdict

class Solution:
    def minimumWeight(self, n: int, edges: list[list[int]], src1: int, src2: int, dest: int) -> int:
        g = defaultdict(list)
        rg = defaultdict(list) # Reverse graph for destination tracking
        
        for u, v, w in edges:
            g[u].append((v, w))
            rg[v].append((u, w))
            
        def dijkstra(graph, start):
            dist = {i: float('inf') for i in range(n)}
            dist[start] = 0
            pq = [(0, start)]
            
            while pq:
                d, u = heapq.heappop(pq)
                if d > dist[u]: continue
                for neighbor, weight in graph[u]:
                    if dist[neighbor] > d + weight:
                        dist[neighbor] = d + weight
                        heapq.heappush(pq, (dist[neighbor], neighbor))
            return dist

        # 3 times Dijkstra runs
        d1 = dijkstra(g, src1)
        d2 = dijkstra(g, src2)
        d3 = dijkstra(rg, dest) # Reverse graph gives dist from all nodes to dest
        
        ans = float('inf')
        for i in range(n):
            ans = min(ans, d1[i] + d2[i] + d3[i])
            
        return ans if ans != float('inf') else -1
