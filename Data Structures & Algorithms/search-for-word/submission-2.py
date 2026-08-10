class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m , n = len(board) , len(board[0])

        seen = [ [False for _ in range(n)] for _ in range(m)]

        poss = [[-1, 0] , [1, 0] , [0,-1] , [0, 1]]

        def isvalid(x, y ):
            if 0<=x<m and 0<=y<n:
                return True
            return False
            
        def word_s(x , y , curr):
            print(curr)
            if curr == "":
                return True

            for dx , dy in poss:
                x1 , y1 = x+dx , y+dy
                if not isvalid(x1, y1):
                    continue 
                
                c = board[x1][y1]
                if  not seen[x1][y1] and c == curr[0] :                  
                    seen[x1][y1] = True
                    if word_s(x1, y1 , curr[1:]):
                        return True
                    seen[x1][y1] = False

            return False
        for i in range(m):
            for j in range(n):
                if word[0] == board[i][j]:
                    seen[i][j] = True
                    if word_s(i , j , word[1:]):
                        return True
                    seen[i][j] = False
        return False