from functools import lru_cache

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        @lru_cache(None)
        def burst( snums):
            if not snums:
                return 0
            if len(snums) == 1:
                return snums[0]
            n = len(snums)
            res = 0
            for i in range(n):
                curr = snums[i]
                if i == 0 :
                    prev = 1
                    last = snums[i+1]
                elif i == n-1:
                    last = 1
                    prev = snums[i-1]
                else:
                    prev = snums[i-1]
                    last = snums[i+1]
                nnums = snums[:i]+snums[i+1:]
                res =max(res , burst(nnums) + curr * prev * last) 
            return res
        return burst(nums)