class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        l  = len(nums)
        window = None
        res = [0]*(l-k+1)
        for i in range(l-k+1):
            window = nums[i:i+k]
            if window :
                res[i] = max(window)
        return res