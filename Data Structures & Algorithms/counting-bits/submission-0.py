class Solution:
    def countBits(self, n: int) -> List[int]:
        def cont(a):
            count = 0 
            for i in range(32):
                if a & (1 << i)!=0:
                    count +=1
            return count
        
        res = [0]*(n+1)
        for a in range(n+1):
            res[a] = cont(a)
        return res
