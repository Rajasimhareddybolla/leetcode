class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        self.res = [ ]
        def per(sofar , status):
            if len(sofar) == len(nums):
                self.res.append(sofar)
                return

            for i in range(len(nums)):
                if not status[i]:
                    status[i] = True
                    per(sofar+[nums[i]] , status)
                    status[i] = False

            return 
        
        per([] , [False]*len(nums))
        return self.res
