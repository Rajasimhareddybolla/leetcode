class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def find(x , y):
            if not x and y == '*':
                return True
            if not x and not y : return True
            if not x or not y:
                return False
            res = 0 
            if y[0] == '.':
                res = find(x[1:] , y[1:])
                if res : return True
            elif y[0] == '*':
                res = find(x[1:] , y)
                if res : return True
                res = find(x , y[1:])
                if res : return True

            elif x[0] == y[0]:
                res = find(x[1:] , y[1:])
                if res : return True
            else:
                res = find(x , y[1:])
                if res : return True
            return False
        return find(s , p)