class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        m = len(s)
        left , right = 0 , 0
        res = 0
        while left < m:
            block = {}
            big_c = s[left]
            rep = 0
            while right < m :
                c = s[right]
                if c not in block:
                    block[c] = 0
                block[c] +=1
                big_no = block[big_c]
                if block[c] > big_no:
                    big_no = block[c]
                    big_c = c
                rep = right - left + 1 - big_no
                if rep > k:
                    break
                right +=1
            res = max(right - left , res)
            left +=1
            right = left 
        return res