class Solution:
    def countSubstrings(self, s: str) -> int:
        def isPalindrom(s):
            return s==s[::-1]
        n = 0
        l = len(s)
        for i in range(l):
            for j in range(i+1, l+1):
                if isPalindrom(s[i:j]):
                    n+=1
        return n