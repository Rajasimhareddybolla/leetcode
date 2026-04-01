class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        def find(i , target):
            if i == n  : 
                if target == 0 : return 1
                return 0

            return find(i+1 , target- nums[i]) + find(i+1 , target+nums[i])
        
        return find(0 , target)