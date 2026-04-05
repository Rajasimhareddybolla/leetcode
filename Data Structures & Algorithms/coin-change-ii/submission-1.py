from typing import List
from collections import Counter

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()

        def change(rem , index):
            if rem == 0:
                return 1
            if index >= len(coins) or rem<0 :
                return 0

            res = change(rem-coins[index] ,  index)
            res += change(rem , index+1)
            return res
            
        return change(amount, 0 )