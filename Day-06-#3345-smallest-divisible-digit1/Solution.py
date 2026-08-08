
## `solution.py`

```python
"""
LeetCode #3345 - Smallest Divisible Digit Product I

Approach:
- Brute Force
- Digit Extraction

Time Complexity: O(d)
Space Complexity: O(1)

Author: Varshitha Thogaru
"""

class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n, n + 10):
            temp = i
            res = 1

            while temp > 0:
                res *= temp % 10
                temp //= 10

            if res % t == 0:
                return i
