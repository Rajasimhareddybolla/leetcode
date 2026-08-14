from functools import lru_cache
class Solution:
    def rob(self, nums: List[int]) -> int:        
        n = len(nums)
        @lru_cache(None)
        def r(i):
            if i >= n:
                return 0
            
            a , b = r(i+2)+nums[i] , r(i+1)
            return max(a , b)
        
        return r(0)