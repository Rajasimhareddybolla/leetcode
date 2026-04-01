class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n >= 0:
            res = 1
            for i in range(1 , n+1):
                res *= x
            return res
        else:
            res = 1.0
            for i in range(0, n , -1):
                res = res * (1.0/x)
            return res

