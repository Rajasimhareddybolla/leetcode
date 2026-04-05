class Solution:
    def countBits(self, n: int) -> List[int]:
        def cont(a):
            count = 0 
            for i in range(32):
                if a & (1 << i)!=0:
                    count +=1
            return count
        res = [0] * (n + 1)
        
        for i in range(1, n + 1):
            res[i] = res[i >> 1] + (i & 1)
        
        return res