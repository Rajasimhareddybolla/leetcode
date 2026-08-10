class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        

        res = []
        def generate(topens, opens , sofar):
            if topens == n :
                res.append(sofar+')'*opens)
                return 
            
            if topens > n :
                return 
            if topens < n :
                generate(topens+1 , opens+1 , sofar+'(')
            if opens > 0 :
                generate(topens , opens-1 , sofar+')')

        generate(0 , 0 , '')
        return res