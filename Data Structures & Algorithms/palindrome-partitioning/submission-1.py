class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def groups(i , sofar , ss ,rr ):
            if i == len(s):
                if ss == "":
                    res.append(sofar)
                return 
            if i > len(s): return 
            
            ss = ss+s[i]
            rr = s[i]+ rr
            if ss ==rr :
                groups(i+1 , sofar+[ss] , '' , '')
            
            groups(i+1 , sofar , ss , rr)

        groups(0 , [] , '' , '')
        return res