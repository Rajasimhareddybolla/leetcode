import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k 
        self.h= [n for n in nums[:k]]
        heapq.heapify(self.h)

        for num in nums[k:]:
            if self.h[0] < num:
                heapq.heapreplace(self.h , num)
        


    def add(self, val: int) -> int:
        if len(self.h) < self.k:
            heapq.heappush(self.h , val)
        
        elif self.h[0] < val :
            heapq.heapreplace(self.h , val)
        return self.h[0]