# 🚀 LeetCode #3345 - Smallest Divisible Digit Product I

## 🧩 Problem Statement

Given two positive integers `n` and `t`, return the smallest integer greater than or equal to `n` such that the product of its digits is divisible by `t`.

🔗 Problem Link:
https://leetcode.com/problems/smallest-divisible-digit-product-i/

---

## 💡 Approach

I used a simple **Brute Force + Digit Extraction** approach.

### Algorithm

1. Start checking numbers from `n`.
2. For each number, extract its digits using:
   - `temp % 10` to get the last digit.
   - `temp //= 10` to remove the last digit.
3. Multiply all the digits together.
4. Check whether the digit product is divisible by `t`.
5. Return the first number satisfying the condition.

Since the answer is guaranteed to be found within a small range, checking consecutive numbers is efficient.

---

## 🧠 Python Solution

```python
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
