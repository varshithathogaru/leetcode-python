
"""# Day 23/45 — LeetCode 3663

## Find The Least Frequent Digit

### Problem
Given a positive integer `n`, return the digit that occurs the least number of times in `n`.

If multiple digits have the same minimum frequency, return the smallest digit.

### Python Solution

```python
class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        s = str(n)
        return int(min(set(s), key=lambda d: (s.count(d), int(d))))
