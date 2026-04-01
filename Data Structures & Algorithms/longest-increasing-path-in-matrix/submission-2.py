from functools import lru_cache
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m , n = len(matrix) , len(matrix[0])
        ways = [[-1, 0 ], [1,0] ,  [0 ,-1] , [0,1]]
        def isvalid(i , j):
            return 0<=i<m and 0<=j<n
        @lru_cache(None)
        def find(i , j):
            
            res = 0 
            r = matrix[i][j]
            for dx , dy in ways:
                x , y = dx+i , dy+j
                if isvalid(x , y) and  matrix[x][y] > r:
                    res = max(res , find(x , y))
            return res+1
        res = 0
        for i in range(m):
            for j in range(n):
                res = max(find(i , j) , res)
        return res