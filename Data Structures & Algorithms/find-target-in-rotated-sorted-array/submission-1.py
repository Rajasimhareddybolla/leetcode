class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , h = 0 , len(nums)-1
        while l<=h:
            mid = (l+h)//2
            ll , hl , ml = nums[l] , nums[h] , nums[mid]
            if ml == target :
                 return mid
            if ml>ll:
                if ll<=target<ml:
                    h = mid - 1
                else:
                    l = mid +1
            else:
                if ml<target<=hl:
                    l = mid +1
                else:
                    h = mid -1

        return -1
