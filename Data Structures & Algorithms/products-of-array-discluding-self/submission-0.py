class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [0]*len(nums)
        right = [0]*len(nums)
        left[0] = 1
        right[-1] = 1
        for i in range(1 , len(nums)):
            left[i] = left[i-1] * nums[i-1]
            right[-i-1] = right[-i] * nums[-i]
        print("Left :  ", left)
        print("Right :  " , right)
        res = [0]*len(nums)
        for i , (k ,v) in enumerate(zip(left , right)):
            res[i] = k*v
        return res