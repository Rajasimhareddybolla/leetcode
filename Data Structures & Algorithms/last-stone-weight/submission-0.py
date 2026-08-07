class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        

        import heapq
        stones = [-s for s in stones]
        heapq.heapify(stones )

        while len(stones) >= 2:
            x,  y = -heapq.heappop(stones),-heapq.heappop(stones)
            print(x , y )
            if x == y :
                continue
            else:
                heapq.heappush(stones , -abs(x - y ))
        
        return 0 if not stones else -stones[0]