from typing import List
from collections import Counter

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        re = set()
        
        def change(n, sofar, index):
            if n < 0:
                return 0
            if n == 0:
                re.add(tuple(sorted(sofar)))  # store unique combination
                return 1
            
            res = 0
            for i in range(index, len(coins)):   # 🔥 only forward
                coin = coins[i]
                res += change(n - coin, sofar + [coin], i)  # 🔥 stay at i (reuse allowed)
            
            return res
        
        change(amount, [], 0)
        return len(re)