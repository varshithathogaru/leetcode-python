class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff

        a = a & mask
        b = b & mask

        while b:
            carry = ((a & b) << 1) & mask
            a = (a ^ b) & mask
            b = carry

        return a if a < 0x80000000 else ~(a ^ mask)
