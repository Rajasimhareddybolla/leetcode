class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh  = 0
                
        m , n = len(grid) , len(grid[0])
        poss = [[0 ,1] , [1, 0] , [-1, 0] , [0, -1]]

        ini = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    ini.append([i, j ])
                if grid[i][j] == 1:
                    fresh +=1
        
        
        def isvalid(x , y):
            if 0<= x < m and 0<=y<n:
                return True
            return False

        quee = [ini]
        mins = 0 
        while quee:
            level = quee.pop()
            mins +=1
            l = []
            for x, y in level:
                for dx , dy in poss:
                    x1 , y1 = x+dx , y+dy
                    if isvalid(x1, y1) and grid[x1][y1] == 1:
                        grid[x1][y1] = 2
                        l.append([x1, y1])
                        fresh -=1
            if l: quee.append(l)


        return mins-1 if fresh == 0 else -1