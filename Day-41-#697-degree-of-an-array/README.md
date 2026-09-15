# Day 41 — Degree of an Array

## LeetCode #697

### Problem

Given a non-empty array of non-negative integers, find the smallest possible length of a contiguous subarray that has the same degree as the entire array.

The degree of an array is the maximum frequency of any one of its elements.

### Approach

Use three hash maps:

- `count` → frequency of each number
- `first` → first occurrence of each number
- `last` → last occurrence of each number

### Steps

1. Traverse the array.
2. Store the first index of every number.
3. Update the last index of every number.
4. Count the frequency of every number.
5. Find the maximum frequency (degree).
6. For every number having the degree, calculate:

`last[x] - first[x] + 1`

7. Return the minimum length.

### Example

Input:

`[1, 2, 2, 3, 1]`

Frequencies:

- 1 → 2
- 2 → 2
- 3 → 1

Degree = 2

For 1:

`4 - 0 + 1 = 5`

For 2:

`2 - 1 + 1 = 2`

Answer = `2`

### Complexity

Time: O(n)

Space: O(n)

### Pattern

Hash Map + Frequency Counting + First/Last Index Tracking

### Key Learning

For frequency-based subarray problems, tracking:

`Count + First Index + Last Index`

can convert the problem into a simple range-length calculation.
