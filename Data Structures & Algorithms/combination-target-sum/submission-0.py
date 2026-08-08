from functools import lru_cache


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        self.res = []
        def comb(target , nums , i , sofar):
            if target == 0:
                self.res.append(sofar[:])
                return 
            if i >= len(nums) or target < 0 :
                return

            comb(target , nums , i + 1 , sofar)
            sofar.append(nums[i])
            comb(target-nums[i] , nums,  i , sofar)
            sofar.pop()
            return 
        comb(target , nums , 0 , [])
        return self.res