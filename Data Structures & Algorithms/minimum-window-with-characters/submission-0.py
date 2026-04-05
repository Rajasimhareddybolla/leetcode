class Solution:
    def counter(self , t):
        count = {}
        for c in t:
            if c not in count:
                count[c] = 0 
            count[c] +=1
        return count
    def minWindow(self, s: str, t: str) -> str:
        l  = 0 
        m = float("inf")
        if len(t) > len(s):
            return ""
        res = ""
        counter = self.counter(t)
        while l < len(s):
            lc  = s[l] 
            if lc in counter:
                dcounter = counter.copy()
                r = l 
                while len(dcounter)>0 and r < len(s):
                    rc = s[r]
                    if rc in dcounter :
                        if dcounter[rc] > 0 :
                            dcounter[rc] -=1
                            if dcounter[rc] == 0 :
                                del dcounter[rc]
                    r +=1

                if not dcounter:
                    if m > r - l +1:
                        m = r - l +1 
                        res = s[l:r+1]
            l +=1
        return res