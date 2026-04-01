class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        edges = {}

        for u , v , w in times:
            if u not in edges:
                edges[u] = []
            edges[u].append((v , w))
            
        dist = [float('inf')]*(n+1)
        dist[k] = 0 
        import heapq

        quee = [(0 ,k)]
        while quee:
            cost , node= heapq.heappop(quee)
            if cost > dist[node]:continue
            if node not in edges: continue
            for ne , we in edges[node]:
                c = cost + we
                if c < dist[ne]:
                    heapq.heappush(quee , (c , ne))
                    dist[ne] = c 
        max_wait = max(dist[1:])
        
        return max_wait if max_wait != float('inf') else -1
