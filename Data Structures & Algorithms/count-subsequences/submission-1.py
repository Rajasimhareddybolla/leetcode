class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        

        def find(s1 , s2):
            if not s2:
                return 1
            
            if not s1:
                return 0
            res = 0 
            if s1[0] == s2[0]:
                res += find(s1[1:] , s2[1:])
            res += find(s1[1:] , s2)
            return res
        return find(s , t)