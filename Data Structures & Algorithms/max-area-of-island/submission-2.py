class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        m , n = len(grid) , len(grid[0])
        poss = [ [1,0],[0,1],[-1,0],[0,-1] ]
        res = 0

        def isvalid(i , j):
            if 0<= i < m and 0<=j<n:
                return True
            return False

        def bfs(i , j):
            quee = [[i , j]]
            grid[i][j] = -1
            area = 0
            while quee:
                x, y = quee.pop()
                area +=1
                
                for dx , dy in poss:
                    x1 , y1 = x+dx , y+dy
                    if isvalid(x1 , y1) and grid[x1][y1] == 1:
                        grid[x1][y1] = -1
                        quee.append([x1,y1])

            return area

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(bfs(i , j) , res)
        return res 