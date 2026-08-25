# LeetCode #13 - Roman to Integer

## 🧩 Problem Statement

Given a Roman numeral string, convert it into an integer.

## 💡 Approach

I used a Hash Map to store the integer value of each Roman symbol.

The main idea is to compare the current symbol with the next symbol.

If the current value is smaller than the next value, subtract it.

Otherwise, add it.

For example:

IV = -1 + 5 = 4

IX = -1 + 10 = 9

## 🧠 Python Solution

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0

        for i in range(len(s)):
            if i < len(s) - 1 and roman[s[i]] < roman[s[i + 1]]:
                result -= roman[s[i]]
            else:
                result += roman[s[i]]

        return result
