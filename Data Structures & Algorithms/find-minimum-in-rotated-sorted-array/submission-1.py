class Solution:
    def findMin(self, nums: List[int]) -> int:
        l , h = 0 , len(nums)-1
        while l<h:
            mid = (l+h)//2
            ll , hl , ml = nums[l] , nums[h] , nums[mid]
            if ml > hl:
                l = mid +1
            else:
                h = mid
        return nums[l]


# ll = 3 , hl = 2 , mid = 6