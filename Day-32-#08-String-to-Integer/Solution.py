class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()

        if not s:
            return 0

        sign = 1
        i = 0

        if s[0] in ['-', '+']:
            sign = -1 if s[0] == '-' else 1
            i += 1

        result = 0
        maxi = 2**31 - 1
        mini = -2**31

        while i < len(s) and s[i].isdigit():
            digit = int(s[i])

            if result > maxi // 10 or (result == maxi // 10 and digit > 7):
                return maxi if sign == 1 else mini

            result = result * 10 + digit
            i += 1

        return sign * result
      
