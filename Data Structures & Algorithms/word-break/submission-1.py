class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        l = len(s)
        def br(soFar , i):
            if i>=l:
                if soFar in wordDict or not soFar: return True
                return False
            m = False
            if soFar in wordDict:
                m = br("",i)
            m = br(soFar+s[i] , i+1) or m
            return m
        return br("",0)