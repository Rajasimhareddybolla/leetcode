class Solution:
    def findMin(self, nums: List[int]) -> int:
        l , h = 0 , len(nums)-1
        m = float("inf")
        while l<=h:
            mid = (l+h)//2
            ll , hl , ml = nums[l] , nums[h] , nums[mid]
            print(l , mid , h)
            print(ll , ml , hl)
            if hl<ll and hl<ml:
                l = mid+1
            else:
                h = mid-1
            m = min(m , ll , hl , ml)
        return m


# ll = 3 , hl = 2 , mid = 6