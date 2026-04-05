class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = 0
        carry = 0

        for i in range(32):
            abit = (a >> i) & 1
            bbit = (b >> i) & 1

            s = abit ^ bbit ^ carry
            if s:
                res |= (1 << i)

            carry = (abit & bbit) | (bbit & carry) | (abit & carry)

        return res