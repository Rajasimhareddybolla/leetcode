from functools import lru_cache
class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(None)
        def climb(n):
            if n < 0 :
                return 0
            if n == 0 :
                return 1
            
            return climb(n-1) + climb(n-2)
        
        return climb(n)