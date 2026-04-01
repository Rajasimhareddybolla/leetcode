
from functools import lru_cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        le = len(nums)
        @lru_cache()
        def mob(no , isStart):
            if isStart:
                if no>= len(nums)-1: return 0
            else:
                if no >= len(nums): return 0
            l , r = mob(no+1 ,isStart) , mob(no+2,isStart )+ nums[no]
            return max(l ,r )
        
        return max(mob(0 , True) , mob(1 , False))
