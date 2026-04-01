from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        # Each string is encoded as: <length>#<string>
        return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # Find the separator
            j = s.find('#', i)
            if j == -1:
                break
            length = int(s[i:j])
            # Extract the string
            str_val = s[j+1:j+1+length]
            res.append(str_val)
            i = j+1+length
        return res
