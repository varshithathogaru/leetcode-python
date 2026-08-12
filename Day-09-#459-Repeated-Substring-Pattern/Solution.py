
"""
LeetCode #459 - Repeated Substring Pattern

Approach:
- Knuth-Morris-Pratt (KMP)
- LPS Array

Time Complexity: O(n)
Space Complexity: O(n)

Author: Varshitha Thogaru
"""

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        lps = [0] * n

        length = 0
        i = 1

        while i < n:
            if s[i] == s[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    i += 1

        l = lps[-1]

        return l > 0 and n % (n - l) == 0
