from functools import lru_cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def isvalid(i , j ):
            if 0<=i<m and 0<=j<n: return True
            return False
        poss = [[0,-1] , [-1,0] ]
        mat = [[0]*n for _ in range(m)]
        mat[m-1][n-1] = 1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                res= 0
                for dx, dy in poss:
                    ix , jy = i+dx , j+dy
                    res += mat[ix][jy]
                mat[i][j] = res
        print(mat)
        return mat[0][0]
        @lru_cache()
        def count(i , j):
            print(i,j)
            if not isvalid(i , j):return 0
            if i == m-1 and j==n-1: return 1
            res = 0
            for dx , dy in poss:
                ix , iy = i+dx , j+dy
                res += count(ix , iy)
            return res
        
        return count(0,0)