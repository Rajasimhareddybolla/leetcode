from functools import lru_cache

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        @lru_cache()
        def divide(a , b , c):
            if not a and not b and not c:
                return True
            elif not a :
                if b == c : return True
                else: return False
            elif not b:
                if a == c: return True
                return False
            elif not c:
                return False

            res = False
            if c[0] == b[0] == a[0]:
                res = res or (divide(a[1:] , b , c[1:]) or divide(a , b[1:] , c[1:]))
                if res : return res
            elif c[0] == a[0]:
                res = res or divide(a[1:] ,b ,c[1:])
                if res : return res
            elif c[0] == b[0]:
                res = res or divide(a , b[1:] , c[1:])
                if res : return res
            else:
                return False
            return res

        return divide(s1 ,s2 , s3)