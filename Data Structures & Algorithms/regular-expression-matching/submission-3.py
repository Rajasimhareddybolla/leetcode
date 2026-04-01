class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s , p = s , p
        m , n = len(s) , len(p)
        def find(i , j ):
            if j == n :
                return i == m
            
            first_match = i<m and (s[i] == p[j] or p[j] == '.')

            if j+1<n and p[j+1] == '*':
                ans = (
                    find(i , j+2) or first_match and find(i+1, j)
                )
            else:
                ans = first_match and find(i+1,  j+1)
            return ans


        return find(0 ,0  )