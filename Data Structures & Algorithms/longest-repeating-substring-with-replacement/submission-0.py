class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        m = len(s)
        res = 0
        for i in range(m):
            nos = k
            ch = s[i]
            j = i +1
            while j<m and (s[j] == ch or nos>0 ):
                if not s[j] == ch:
                    nos -=1
                j+=1
            res = max(res , j - i )
        return res
