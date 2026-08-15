# 🚀 LeetCode #3 - Longest Substring Without Repeating Characters

## 🧩 Problem Statement

Given a string `s`, find the length of the longest substring without
repeating characters.

🔗 Problem:
https://leetcode.com/problems/longest-substring-without-repeating-characters/

---

## 💡 Approach

I solved this problem using the **Sliding Window** technique with a
HashSet.

The set stores the unique characters currently present in the window.

I used two pointers:

- `left` → start of the current window
- `right` → end of the current window

### Algorithm

1. Move `right` through the string to expand the window.
2. If `s[right]` is already present in the set, the window contains
   a duplicate.
3. Remove characters from the left and move `left` forward until
   the duplicate is removed.
4. Add the current character to the set.
5. Calculate the current window length.
6. Keep track of the maximum length found.

### Window Length

```text
right - left + 1
