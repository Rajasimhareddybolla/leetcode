
from functools import lru_cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        le = len(nums)
        @lru_cache()
        def mob(no , num):
            if no >= len(num): return 0
            l , r = mob(no+1 , num) , mob(no+2 , num)+ num[no]
            return max(l ,r )
        
        return max(mob(0 , nums[:-1]) , mob(1 , nums))
