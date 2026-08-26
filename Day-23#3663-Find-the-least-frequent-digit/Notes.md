# Day 23 — LeetCode 3663
## Find The Least Frequent Digit

---

## 1. Problem Understanding

We are given an integer `n`.

We need to:

1. Find how many times each digit occurs.
2. Find the digit with the **minimum frequency**.
3. If multiple digits have the same minimum frequency, return the **smallest digit**.

### Example

n = 1122334

Frequency:

1 → 2 times
2 → 2 times
3 → 2 times
4 → 1 time

Therefore:

Answer = 4

---

# 2. My Solution

```python
class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:

        s = str(n)

        return int(
            min(
                set(s),
                key=lambda d: (s.count(d), int(d))
            )
        )
