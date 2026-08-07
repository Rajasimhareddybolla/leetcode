class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        import heapq

        h = [ n for n in nums[:k]]
        heapq.heapify(h)

        for num in nums[k:]:
            if num > h[0]:
                heapq.heapreplace(h , num)


        return h[0]