class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        
        # 1. Generate all possible edges between unique pairs
        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                # Manhattan distance using built-in abs()
                dist = abs(x1 - x2) + abs(y1 - y2)
                edges.append((dist, i, j))
        
        # 2. Sort edges by distance (lowest cost first)
        edges.sort()
        
        # 3. Kruskal's Algorithm using Union-Find
        uf = UnionFind(n)
        min_cost = 0
        edges_count = 0
        
        for cost, u, v in edges:
            if uf.union(u, v):
                min_cost += cost
                edges_count += 1
                # Optimization: If we have n-1 edges, everything is connected
                if edges_count == n - 1:
                    break
                    
        return min_cost

# Helper DSU Class
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) # Path compression
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        
        if rootX != rootY:
            # Union by rank optimization
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            return True
        return False