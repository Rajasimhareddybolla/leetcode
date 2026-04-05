class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(len(n)):
            if nums[i] != i:
                return i
        