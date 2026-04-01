class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        def op(no):
            no = str(no)
            res = sum(int(i)**2 for i in no)
            return int(res)
        
        while n not in visited:
            visited.add(n)
            n = op(n)
            if n == 1:
                return True
        return False