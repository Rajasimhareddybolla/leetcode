
from functools import lru_cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        le = len(cost)
        @lru_cache
        def search(i ):
            if i >= le:
                return 0
            l , r = search(i+1) , search(i+2)
            res= min(l , r)
            return res+cost[i]
        
        return min(search(0) , search(1))