class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Convert to set for O(1) lookups
        wordSet = set(wordDict)
        # Memoization dictionary to store results of subproblems
        memo = {}
        n = len(s)

        def br(start_index):
            if start_index == n:
                return True
            
            if start_index in memo:
                return memo[start_index]
            
            for end_index in range(start_index + 1, n + 1):
                word = s[start_index:end_index]
                
                if word in wordSet and br(end_index):
                    memo[start_index] = True
                    return True
            memo[start_index] = False
            return False

        return br(0)