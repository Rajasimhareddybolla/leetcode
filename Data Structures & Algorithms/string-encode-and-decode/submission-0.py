class Solution:
    def __init__(self):
        self.res = {}
    def encode(self, strs: List[str]) -> str:
        self.res[' '.join(strs)] = strs
        return ' '.join(strs)
    def decode(self, s: str) -> List[str]:
        return self.res[s]