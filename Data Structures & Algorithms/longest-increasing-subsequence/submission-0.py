class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = len(nums)
        def search(n , prev):
            if n >= l: return 0
            cur = nums[n]
            res = 0 
            if cur > prev: 
                res = search(n+1 , cur) +1
            res = max(search(n+1 , prev) , res )
            return res
        return  search(0 , float("-inf"))