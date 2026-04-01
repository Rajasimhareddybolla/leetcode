class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0 : return 0
        memo = {}
        def coin_c(amnt):
            if amnt in memo : return memo[amnt]
            if amnt == 0 : return 0
            m = float("inf")
            for coin in coins:
                rem_amnt = amnt - coin
                if coin > amnt:continue
                res = coin_c(rem_amnt)
                m = min(res + 1, m)
            memo[amnt] = m
            return m
        res= coin_c(amount)
        return -1 if res == float("inf") else res