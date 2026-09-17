# Day 43 — Smallest Absent Positive Integer

## LeetCode #3678

### Problem

Given an integer array, find the smallest positive integer that is absent from the array and is strictly greater than the average of the array.

### Approach

1. Calculate the integer average of the array.
2. Start checking from `max(1, average + 1)`.
3. Convert the array into a set for fast membership checking.
4. Keep increasing the candidate while it exists in the set.
5. Return the first absent positive integer.

### Example

Input:

`[3, 4, 5, 6]`

Sum = 18

Length = 4

Average:

`18 // 4 = 4`

Start candidate:

`5`

5 exists.

6 exists.

7 does not exist.

Therefore:

`Answer = 7`

### Important Idea

Instead of repeatedly searching the list, use a set:

```python
seen = set(nums)
