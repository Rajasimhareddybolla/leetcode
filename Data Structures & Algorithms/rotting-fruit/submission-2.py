class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m , n = len(grid) , len(grid[0])

        ff = 0 
        rotten = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ff+=1
                elif grid[i][j] == 2:
                    rotten.append((i , j))
        quee = [rotten]
        time = -1
        while quee:
            level = quee.pop(0)
            if not level: continue
            nlevel = []
            for i , j in level:
                for di , dj in [(-1,0) , (0,1) , (1 , 0) , (0,-1)]:
                    x , y = di+i , dj+j
                    if not (0<=x<m and 0<=y<n): continue
                    if grid[x][y] == 1:
                        nlevel.append([x,y])
                        ff -=1
                        grid[x][y] = 2
            quee.append(nlevel)
            time +=1
        return max(time , 0) if ff == 0 else -1