class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)

        tot = 0

        while x > 0:
            rem = x % 10
            tot = tot * 10 + rem
            x = x // 10

        tot = sign * tot

        if tot < -2**31 or tot > 2**31 - 1:
            return 0

        return tot
