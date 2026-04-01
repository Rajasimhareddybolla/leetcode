from functools import lru_cache

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # @lru_cache()
        def cdist(w1 , w2):
            if not w1 and not w2:
                return 0
            elif not w1:
                return len(w2)
            elif not w2:
                return len(w1)
            
            md = float("inf")
            a , b = w1[0] , w2[0]
            if a == b:
                md = min(md , cdist(w1[1:] , w2[1:]))
            else:
                md = min(
                    md , 
                    cdist(w1[1:] , w2)+1, ## its for deletion
                    cdist(w1 , w2[1:]) +1 , ## for inserting
                    cdist(w1[1:] , w2[1:]) +1 , ## replacing
                )
            return md
        return cdist(word1 ,word2)