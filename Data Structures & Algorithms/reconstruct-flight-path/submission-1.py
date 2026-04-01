import collections
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        
        for source, dest in sorted(tickets, reverse=True):
            graph[source].append(dest)
        
        route = []
        def visit(airport):
            while graph[airport]:
              
                next_dest = graph[airport].pop()
                visit(next_dest)

            route.append(airport)
        visit("JFK")
        
        return route[::-1]