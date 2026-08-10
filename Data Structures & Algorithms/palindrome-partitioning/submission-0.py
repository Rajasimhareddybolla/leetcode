class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def groups(i , sofar , ss ):
            if i == len(s):
                if ss == "":
                    res.append(sofar)
                return 
            if i > len(s): return 
            
            ss = ss+s[i]
            
            if ss == ss[::-1]:
                groups(i+1 , sofar+[ss] , '')
            
            groups(i+1 , sofar , ss)

        groups(0 , [] , '')
        return res