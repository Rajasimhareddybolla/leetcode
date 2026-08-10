class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        self.res = [ ]
        def per(sofar , rem):
            if not rem:
                self.res.append(sofar)
                return

            for i in range(len(rem)):
                per(sofar + [rem[i]] , rem[:i]+rem[i+1:])

            return 
        per([] , nums)
        return self.res
