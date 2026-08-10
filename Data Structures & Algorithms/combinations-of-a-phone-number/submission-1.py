class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        keypad = {
            
            "2": ["2", "a", "b", "c"],
            "3": ["3", "d", "e", "f"],
            "4": ["4", "g", "h", "i"],
            "5": ["5", "j", "k", "l"],
            "6": ["6", "m", "n", "o"],
            "7": ["7", "p", "q", "r", "s"],
            "8": ["8", "t", "u", "v"],
            "9": ["9", "w", "x", "y", "z"],

        }
        def comb(l1 , l2):
            res = []
            for s1 in l1:
                for s2 in l2:
                    res.append(s1+s2)
            
            return res
        

        if len(digits) == 1: return keypad[digits[0]][1:]
        if len(digits) == 0: return []

        l1 , l2 = keypad[digits[0]][1:] , keypad[digits[1]][1:]
        res = comb(l1 , l2)
        for i in range(2,len(digits)):
            res = comb( res , keypad[digits[i]][1:])
        
        return res

            
