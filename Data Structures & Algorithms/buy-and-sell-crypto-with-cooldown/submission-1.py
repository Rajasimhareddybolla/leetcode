from typing import List
from functools import lru_cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        @lru_cache(None)
        def stock(i, coin):
            if i >= len(prices):
                return 0
            
            if coin is not None:
                sell = prices[i] - coin + stock(i + 2, None)  # cooldown
                
                hold = stock(i + 1, coin)
                
                return max(sell, hold)
            
            else:

                buy = stock(i + 1, prices[i])
                
                skip = stock(i + 1, None)
                
                return max(buy, skip)
        
        return stock(0, None)