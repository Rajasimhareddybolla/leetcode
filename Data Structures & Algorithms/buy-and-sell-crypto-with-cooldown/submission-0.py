class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        

        def stock(i , coin ):
            if i >= len(prices):
                return 0
            
            profit = 0
            if coin is not None:
                if prices[i]-coin>0:
                    profit+=prices[i]-coin
                    profit += max(stock(i+2, prices[i]) , stock(i+1 , None)) ## repeated logic
                else:
                    profit = stock(i+1 , coin)

            else:
                profit= max(stock(i+1 , coin) , stock(i , prices[i]))
            
            return profit
        return stock(0 , None)