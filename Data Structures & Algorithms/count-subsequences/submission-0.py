class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        

        def find(s1 , s2):
            if not s1:
                if s2:
                    return 0
            
