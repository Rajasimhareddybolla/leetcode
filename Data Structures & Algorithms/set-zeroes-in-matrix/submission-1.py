class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m , n = len(matrix) , len(matrix[0])
        row = [-1]*m
        col = [-1]*n
        for i in range( m):
            for j in range( n):
                if matrix[i][j] == 0:
                    row[i] = 0
                    col[j] = 0 
        for i in range(m):
            if row[i] == 0 :
                for j in range(n):
                    matrix[i][j] = 0
        print(matrix)
        for j in range(n):
            if col[j] == 0 :
                for i in range(m):
                    matrix[i][j]= 0

      