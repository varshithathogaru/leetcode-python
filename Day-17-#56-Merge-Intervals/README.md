# LeetCode #56 - Merge Intervals

## 🧩 Problem Statement

Given an array of intervals, merge all overlapping intervals and return
an array of the non-overlapping intervals that cover all the intervals.

🔗 Problem:
https://leetcode.com/problems/merge-intervals/

## 💡 Approach

I solved this problem using the **Intervals + Sorting** pattern.

### Steps

1. Sort the intervals based on their starting values.
2. Add the first interval to the output.
3. Compare each interval with the last interval in the output.
4. If the current interval overlaps with the previous one, merge them.
5. Otherwise, add the current interval separately.

Two intervals overlap when:

```text
current_start <= previous_end
