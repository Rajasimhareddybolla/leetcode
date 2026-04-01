class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrom(s):
            return s[::-1] == s
        l = len(s)
        m = 0
        res = ''
        for i in range(l):
            for j in range(i+1,l+1):
                if isPalindrom(s[i:j]):
                    if j-i > m : 
                        m = j -i
                        res = s[i:j]
        return res