# 🚀 LeetCode #3090 - Maximum Length Substring With Two Occurrences

## 🧩 Problem Statement

Given a string `s`, find the length of the longest substring in which
each character appears at most twice.

🔗 Problem:
https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/

---

## 💡 Approach

I solved this problem using the **Sliding Window** technique with a
frequency dictionary.

I maintained two pointers:

- `l` → left boundary of the window
- `r` → right boundary of the window

A dictionary `m` keeps track of the frequency of each character
inside the current window.

### Algorithm

1. Expand the window by moving `r`.
2. Add the current character to the frequency map.
3. If the current character occurs more than twice, shrink the window
   from the left.
4. Continue shrinking until the window becomes valid again.
5. Update the maximum window length.

The current window is always maintained so that every character occurs
at most twice.

---

## 🧠 Python Solution

```python
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
