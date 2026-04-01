from functools import lru_cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def isvalid(i , j ):
            if 0<=i<m and 0<=j<n: return True
            return False
        poss = [[0,1] , [1,0] ]
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