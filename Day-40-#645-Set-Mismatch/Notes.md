# Day 40 Notes — Set Mismatch

## LeetCode
#645

## Pattern
Frequency Map / Hash Map

## Problem

One number appears twice and one number from `1` to `n` is missing.

Return:

```text
[duplicate, missing]
Approach
Create a frequency dictionary.
Count every number.
Iterate from 1 to n.
Frequency 2 → duplicate.
Frequency 0 → missing.
Important Code
freq[i] = freq.get(i, 0) + 1

get(i, 0) means:

Return the frequency of i, otherwise return 0.

Example
nums = [1, 2, 2, 4]

1 → frequency 1
2 → frequency 2 → duplicate
3 → frequency 0 → missing
4 → frequency 1

Answer:

[2, 3]
Memory Trick

COUNT → CHECK → IDENTIFY

Complexity

Time: O(n)

Space: O(n)
