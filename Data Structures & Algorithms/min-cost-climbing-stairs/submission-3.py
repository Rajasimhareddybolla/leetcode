from functools import lru_cache

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:    
        @lru_cache(None)
        def climb(i):
            if i <= 1:
                return 0
            return min(climb(i - 1) + cost[i - 1],
                       climb(i - 2) + cost[i - 2])

        return climb(len(cost))