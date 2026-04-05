class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        directions = [[0,1] , [1,0] , [0,-1] , [-1,0]]
        visited = set()
        res = []
        m , n = len( matrix) , len(matrix[0])
        i = 0 

        def valid(i , j ):
            if 0<=i<m and 0<=j<n and matrix[i][j] not in visited: 
                return True
            return False
        x , y =  0 , -1
        while  len(visited) < m*n:
            dx , dy = directions[i]
            x1 , y1 = x+dx , y+dy
            print(visited)
            if valid(x1,y1):
                res.append(matrix[x1][y1])
                visited.add(matrix[x1][y1])
                x, y = x1, y1
            else:
                i+=1
                i = i%4
        return  res