# Day 39 - Longest Continuous Increasing Subsequence

## 🚀 LeetCode #674

### Problem

Given an integer array `nums`, return the length of the longest continuous increasing subsequence.

A continuous increasing subsequence means that every element is strictly greater than the previous element and the elements must be adjacent.

---

## 💡 Approach

I used two variables:

- `curr_len` → length of the current increasing sequence
- `max_len` → longest increasing sequence found so far

For every element, compare it with the previous element.

If:

```text
nums[i] > nums[i - 1]
