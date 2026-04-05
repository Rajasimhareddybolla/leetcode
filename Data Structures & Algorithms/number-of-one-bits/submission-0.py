class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0 
        s = str(n)
        for i in range(len(s)):
            if s[i] == 1:
                res +=1
        return res