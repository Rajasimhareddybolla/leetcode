class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l= len(nums)
        m = float("-inf")
        for i in range(l):
            csum , msum =  1 , float("-inf")
            for j in range(i , l):
                csum = csum*nums[j]
                msum = max(msum , csum)
            m = max(m , msum)
        return m