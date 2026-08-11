class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m , n = len(board ) , len(board[0])
        
        poss = [[ 0, 1] , [1, 0 ] , [ 0 ,-1] , [-1 , 0]]
        def isvalid( x,  y ):
            if 0<=x<m and 0<= y <n: return True
            return False
        def isboard(x1 , y1):
            return (x1 == 0 or x1 == m-1) or (y1 == 0 or y1==n-1)

        isvisited = [[ False for j in range(n)] for i in range(m)]
        def bfs(i , j):
            quee = [[i , j ]]
            isCapture = True if not isboard(i , j) else False
            history = [[i , j ]]
            while quee:
                x , y =  quee.pop()
                for dx , dy in poss:
                    x1 , y1 = x + dx, y+dy
                    if isvalid(x1 , y1) and board[x1][y1] == 'O' and isvisited[x1][y1] == False:
                        quee.append([x1, y1])
                        history.append([x1,y1])
                        isvisited[x1][y1] = True
                        
                        if isboard(x1, y1):
                            isCapture = False
            if isCapture:
                for x, y in history:
                    board[x][y] = 'X'
            
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and isvisited[i][j] == False:
                    bfs(i , j)
        
