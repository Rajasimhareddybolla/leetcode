class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m , n = len(matrix) , len(matrix[0])
        ways = [[-1, 0 ], [1,0] ,  [0 ,-1] , [0,1]]
        def find(i , j):
            if  not 0<=i<m and 0<=j<n:
                return 0