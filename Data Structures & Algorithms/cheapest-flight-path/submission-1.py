class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {}
        for i in range(n): graph[i] = []
        for source , dest , price  in flights:
            graph[source].append([price , dest])
        
        for i in range(n) : graph[i].sort()

        def search(port , k , price):
            if port == dst:
                return price
            m_price = float("inf")
            if k < 0 : return m_price
            
            for n in graph[port]:
                pp , neigh = n
                p = search(neigh , k-1 , price + pp)
                m_price = min(m_price , p)
            return m_price
        res = search(src , k , 0) 
        
        return res if res != float("inf") else -1