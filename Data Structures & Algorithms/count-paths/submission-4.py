

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def isvalid(i , j):
            if 0<=i<m and 0<=j<n: return True
            return False
        def gen(i , j):
            if (i , j ) in memo:
                return memo[(i , j)]

            if not isvalid(i,j): return 0
            if i == m - 1 and j == n - 1:
                return 1
            
            right = gen(i , j+1 )
            left = gen(i + 1 , j)
            memo[(i , j)] = right + left
            return left + right
        
        return gen(0 , 0)