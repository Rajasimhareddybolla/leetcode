class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0 : return 0
        coins.sort()
        coins = coins[::-1]
        def coin_c(amnt):
            if amnt == 0 : return 0
            for coin in coins:
                n_coin= amnt // coin
                if n_coin == 0: continue
                rem_amnt = amnt % coin
                res = coin_c(rem_amnt)
                if res >= 0:
                    return res + n_coin
            return -1
        return coin_c(amount)