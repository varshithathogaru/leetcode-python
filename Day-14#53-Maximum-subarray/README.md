# 🚀 LeetCode #53 - Maximum Subarray

## 🧩 Problem Statement

Given an integer array `nums`, find the subarray with the largest sum
and return its sum.

A subarray is a contiguous part of an array.

🔗 Problem:
https://leetcode.com/problems/maximum-subarray/

---

## 💡 Approach

I solved this problem using **Kadane's Algorithm**.

The main idea is to maintain the maximum subarray sum ending at the
current position.

For every element, I have two choices:

1. Start a new subarray from the current element.
2. Extend the previous subarray by adding the current element.

This is represented by:

```python
curr_sum = max(nums[i], nums[i] + curr_sum)
