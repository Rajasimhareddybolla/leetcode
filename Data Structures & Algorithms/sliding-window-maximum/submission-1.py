class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        nums2 = [ [nums[j] for j in range(len(nums)) ] for i in range(len(nums))]
        nums = nums2
        m , n = len(nums) , len(nums[0])
        res = [0]*(m-k+1)
        res[0] = max(nums[0][:k])
        for i in range(1 , m-k+1):
            res[i] = max(res[i-1] , nums[i][i+k-1])
        return res 