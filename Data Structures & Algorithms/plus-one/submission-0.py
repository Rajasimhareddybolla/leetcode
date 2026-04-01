class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = int(''.join([str(r) for r in digits]))+1
        return [r for r in str(res)]