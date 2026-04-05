class Dsu:
    def __init__(self , n):
        self.rank = [1 for i in range(n)]
        self.parent = [i for i in range(n)]

    def find(self , n ):
        if n != self.parent[n]:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]

    def union(self , a , b):
        x , y = self.find(a) , self.find(b)
        if x == y : return False
        if self.rank[x] > self.rank[y]: 
            self.parent[x] = self.parent[y]
        elif self.rank[x] < self.rank[y]:
            self.parent[y] = self.parent[x]
        else:
            self.parent[x] = self.parent[y]
            self.rank[x] +=1
        return True
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        dsu =Dsu(n)
        for a , b in edges:
            if not union(a ,b):
                return [a ,b]
        return 
