class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        x= init
        for i in range(iterations):
            f = x**2
            df= 2*x
            x = x - learning_rate * df
        return round(x , 5)