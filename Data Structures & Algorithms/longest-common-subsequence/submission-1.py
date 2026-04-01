class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        l1 , l2 = len(text1) , len(text2)
        memo = {}
        def search(i , j ):
            if i >= l1 or j>=l2: return 0
            if (i , j ) in memo: return memo[(i , j)]
            res = 0
            if text1[i] == text2[j]:
                res = max( res , search(i+1 , j+1)+1)
            l = search(i+1 , j)
            r = search(i , j+1)
            res = max(l , r , res)
            memo[(i , j)] = res
            return res 
        
        return search(0 , 0)