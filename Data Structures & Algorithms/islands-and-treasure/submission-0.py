class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        m , n = len(grid) , len(grid[0])
        poss = [[0 ,1] , [1, 0] , [-1, 0] , [0, -1]]
        ## Its the same as rotting oranges so find the time and come backward towords the cell from the holes 

        INF = 2147483647
        ini = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    ini.append([i, j ])
        
        def isvalid(x , y):
            if 0<= x < m and 0<=y<n:
                return True
            return False

        nodes = [ini]
        time = 0
        while nodes:
            level = nodes.pop()
            time +=1
            l = [ ]
            for x , y in level:
                for dx , dy in poss:
                    x1 , y1 = x+dx , y+dy
                    if isvalid(x1,y1) and grid[x1][y1] == INF:
                        grid[x1][y1] = time
                        l.append([x1,y1])
            if l:
                nodes.append(l)
        
        return 