from typing import List


class Solution:

    def combinationSum2(
        self, candidates: List[int], target: int
    ) -> List[List[int]]:
        candidates.sort()  
        res = []

        def comb(i , target , sofar):
            if target == 0:
                res.append(sofar[:])
                return
            if i >= len(candidates) or target < 0 :
                return 
            
            sofar.append(candidates[i])
            comb(i+1 , target- candidates[i] , sofar)
            sofar.pop()
            
            i +=1
            ## leave all the subsequent duplicates 
            while i < len(candidates) and candidates[i] == candidates[i-1]:
                i+=1
            comb(i , target , sofar)
            

        comb(0, target, [])
        return res
