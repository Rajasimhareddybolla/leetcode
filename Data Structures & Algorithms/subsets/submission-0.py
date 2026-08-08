class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        self.res = []
        def sets(nums , i , sofar):
            if i  >= len(nums):
                self.res.append(sofar[:])
                return 
            
            sets(nums, i+1 , sofar)
            sofar.append(nums[i])
            sets(nums , i+1 , sofar )
            sofar.pop()
            return 

        sets(nums , 0 , [])
        return self.res