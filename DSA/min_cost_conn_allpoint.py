class Solution:

    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        edges = []

        # 1. Calculate Manhattan distance between every pair of points
        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(
                    points[i][1] - points[j][1]
                )
                edges.append((dist, i, j))

        # 2. Sort edges by distance (Greedy approach for MST)
        edges.sort()

        # 3. Standard Union-Find (DSU) Implementation
        parent = list(range(n))

        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])  # Path compression
            return parent[i]

        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                return True  # Successfully connected two components
            return False  # Already connected, skip to avoid cycle

        # 4. Process sorted edges to build the tree
        mst_cost = 0
        edges_used = 0

        for dist, u, v in edges:
            if union(u, v):
                mst_cost += dist
                edges_used += 1
                if edges_used == n - 1:  # MST is complete when N-1 edges are added
                    break

        return mst_cost
