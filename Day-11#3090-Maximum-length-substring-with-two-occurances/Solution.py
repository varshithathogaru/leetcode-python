from typing import List

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        m = {}
        l = 0
        ans = 0

        for r in range(len(s)):
            m[s[r]] = m.get(s[r], 0) + 1

            while m[s[r]] > 2:
                m[s[l]] -= 1
                l += 1

            ans = max(ans, r - l + 1)

        return ans
