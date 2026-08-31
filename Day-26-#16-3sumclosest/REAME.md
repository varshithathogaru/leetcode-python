# LeetCode #16 - 3Sum Closest

## 🧩 Problem Statement

Given an integer array `nums` and an integer `target`, find three
integers in `nums` such that their sum is closest to `target`.

Return the sum of the three integers.

## 💡 Approach

I solved this problem using **Sorting + Two Pointers**.

First, I sort the array.

Then I fix one element using a loop and use two pointers for the
remaining two elements.

For every combination:

```text
current = nums[i] + nums[left] + nums[right]
