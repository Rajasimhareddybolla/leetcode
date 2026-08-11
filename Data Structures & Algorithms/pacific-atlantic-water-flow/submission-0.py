from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []
            
        m, n = len(heights), len(heights[0])
        pacific_visited = set()
        atlantic_visited = set()
        
        def bfs(starts, visited):
            queue = deque(starts)
            for x, y in starts:
                visited.add((x, y))
                
            while queue:
                x, y = queue.popleft()
                for dx, dy in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited:
                        if heights[nx][ny] >= heights[x][y]:
                            visited.add((nx, ny))
                            queue.append((nx, ny))

        # Collect ocean borders
        pacific_starts = [[0, i] for i in range(n)] + [[i, 0] for i in range(m)]
        atlantic_starts = [[m - 1, i] for i in range(n)] + [[i, n - 1] for i in range(m)]
        
        # Run BFS for both oceans
        bfs(pacific_starts, pacific_visited)
        bfs(atlantic_starts, atlantic_visited)
        
        # Find intersection
        result = []
        for i in range(m):
            for j in range(n):
                if (i, j) in pacific_visited and (i, j) in atlantic_visited:
                    result.append([i, j])
                    
        return result
