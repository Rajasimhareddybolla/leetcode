class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l , r = 0 , n -1
        while l<=r:
            mid = (l+r)//2
            no = nums[mid]
            if no == target:
                return mid
            if no < target:
                l = mid + 1
            else: r = mid - 1

        return -1