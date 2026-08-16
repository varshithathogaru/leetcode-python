# 🚀 LeetCode #367 - Valid Perfect Square

## 🧩 Problem Statement

Given a positive integer `num`, determine whether it is a perfect
square without using built-in square root functions.

🔗 Problem:
https://leetcode.com/problems/valid-perfect-square/

---

## 💡 Approach

I solved this problem using **Binary Search**.

Instead of checking every number from `1` to `num`, I search for the
possible square root within a specific range.

I maintain two pointers:

- `low` → lower boundary
- `high` → upper boundary

For every iteration, I calculate:

```text
mid = (low + high) // 2
