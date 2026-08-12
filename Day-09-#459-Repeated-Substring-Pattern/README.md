# 🚀 LeetCode #459 - Repeated Substring Pattern

## 🧩 Problem Statement

Given a string `s`, check whether it can be constructed by taking a substring of it and appending multiple copies of the substring together.

🔗 Problem Link:
https://leetcode.com/problems/repeated-substring-pattern/

---

## 💡 Approach

Instead of using Python slicing or string manipulation directly, I solved this problem using the **Knuth-Morris-Pratt (KMP)** algorithm.

The key part of KMP is the **LPS (Longest Prefix which is also Suffix)** array.

### Algorithm

1. Build the LPS array for the given string.
2. `lps[-1]` gives the length of the longest proper prefix that is also a suffix.
3. Let:

```text
l = lps[-1]
