class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m , n = len(matrix) , len(matrix[0])

        for i in range(m):
            for j in range(i+1 , n):
                matrix[i][j] , matrix[j][i] =  matrix[j][i]  ,  matrix[i][j] 

        for i in range(m):
            for j in range(n//2):
                matrix[i][j] , matrix[i][-j-1] = matrix[i][-j-1] ,  matrix[i][j] 

