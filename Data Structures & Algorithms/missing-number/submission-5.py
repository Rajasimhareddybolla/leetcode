class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        r = 0 
        n = len(nums)
        for i in range(n+1):
            r = r^i
        for num in nums:
            r = r^num
        return r