class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        l = len(s)
        def br(soFar , i):
            if i>=l:
                if soFar in s: return True
                return False
            m = False
            if soFar in wordDict:
                m = br("",i)
            if not m:
                m = br(soFar+s[i] , i+1)
            return m
        return br("",0)