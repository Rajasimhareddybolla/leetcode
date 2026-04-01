class Solution:
    def numDecodings(self, s: str) -> int:
        # Memoization dictionary to store results of subproblems
        memo = {}
        l = len(s)

        def decode(i):
            # Base Case: If we reached the end, we found 1 valid path
            if i == l:
                return 1
            
            # Base Case: Leading zeros are invalid
            if s[i] == '0':
                return 0
            
            # Check cache
            if i in memo:
                return memo[i]
            
            # 1. Take 1 digit
            res = decode(i + 1)
            
            # 2. Take 2 digits (if valid index and value <= 26)
            if i + 1 < l and int(s[i:i+2]) <= 26:
                res += decode(i + 2)
            
            # Store result in cache
            memo[i] = res
            return res

        return decode(0)