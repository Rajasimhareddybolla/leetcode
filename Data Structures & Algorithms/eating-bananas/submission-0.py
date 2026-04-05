class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        m  = len(piles)
        l= max(piles)
        for k in range(1, l+1):
            hour = 0
            for i in range(m):
                hour += piles[i]//k
                if piles[i]%k !=0 :
                    hour +=1
            if hour < h :
                print(hour)
                return k
        return l