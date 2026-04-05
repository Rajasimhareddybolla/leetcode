class Solution:
    def encode(self, strs: List[str]) -> str:
        r = '#'
        for s in strs:
            r += str(len(s))
            r+=s
            r+='+'
        r+='#'
        return r
    def decode(self, s: str) -> List[str]:
        res = []
        i = 1
        while i < len(s)-1:
            l = int(s[i])
            i +=1
            res.append(s[i:l+i])
            i = i+ l
            i+=1
        return res