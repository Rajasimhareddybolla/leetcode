class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq

        def dist(x , y):
            return (x**2+ y**2)**0.5

        ## you should use the maxheap 

        h = []
        for x, y in points[:k]:
            h.append( [-dist(x,  y) , [x , y ]])
        
        heapq.heapify(h)
        for x, y in points[k:]:
            d = dist(x,  y)
            if -d > h[0][0]:
                heapq.heapreplace(h , [-d , [x, y]])
        
        return [[x, y ] for d ,(x, y) in h]
