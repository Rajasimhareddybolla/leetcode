from functools import lru_cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        le = len(nums)
        @lru_cache()
        def rob(no):
            if no >= le:
                return 0
            l , r = rob(no+1) , rob(no+2) +nums[no]
            return max(l ,r )

        return rob(0)
