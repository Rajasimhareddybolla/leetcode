class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(n):
            if nums[i] != i:
                return i
        