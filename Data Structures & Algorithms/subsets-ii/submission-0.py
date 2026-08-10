class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        self.res = []
        nums.sort()
        def sgen(sofar , i):
            
            self.res.append(sofar[:])
            

            for j in range(i , len(nums)):
                if j != i and nums[j-1] == nums[j]:
                    continue
                sofar.append(nums[j])
                sgen(sofar , j+1)
                sofar.pop()
            return 

        sgen([] , 0 )
        return self.res