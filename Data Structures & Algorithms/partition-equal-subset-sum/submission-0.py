class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        le = len(nums)
        def search(i , l , r):
            if i >= le: return True if l==r else False
            cur= nums[i]
            l1 , l2 = search(i+1 ,l+cur , r) , search(i+1, l , r+cur)
            return l1 or l2
        return search(0 , 0 ,0 )