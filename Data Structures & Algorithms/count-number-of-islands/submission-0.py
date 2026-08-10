class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m , n = len(grid) , len(grid[0])
        poss = [ [1,0],[0,1],[-1,0],[0,-1] ]
        res = 0

        def isvalid(i , j):
            if 0<= i < m and 0<=j<n:
                return True
            return False

        def bfs(i , j):
            quee = [[i , j]]
            while quee:
                x, y = quee.pop()
                grid[x][y] = '-1'
                for dx , dy in poss:
                    x1 , y1 = x+dx , y+dy
                    if isvalid(x1 , y1) and grid[x1][y1] == '1':
                        quee.append([x1,y1])
            return 

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    bfs(i , j)
                    res +=1
        return res 