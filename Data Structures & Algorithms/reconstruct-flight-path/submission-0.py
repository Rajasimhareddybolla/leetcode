
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        departed = "JFK"
        import heapq

        t = {}
        for source , dest in tickets:
            if source in t:
                t[source].append(dest)
            else:
                t[source] = [dest]
        res = {}

        def triverse(node , tickets , path):
            if not tickets: return path            
            if node in res:
                return res
            t[node].sort()
            print(t)
            for n in t[node]:
                tickets -=1
                path.append(n)
                t[node].remove(n)
                if triverse(n , tickets , path):
                    path = [node]+path
                    return path
                t[node].append(n)
                path = path[:-1]
                tickets +=1
            return None
        return triverse(departed ,len(tickets) , [] )
