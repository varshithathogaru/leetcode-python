# Day 39 Notes — Longest Continuous Increasing Subsequence

## LeetCode
#674

## Pattern
Streak / Consecutive Counting

## Core Idea

Maintain two variables:

python
curr_len = 1
max_len = 1

curr_len = current increasing streak

max_len = longest streak found so far

Condition
nums[i] > nums[i - 1]

If true:

curr_len += 1
max_len = max(max_len, curr_len)

Otherwise:

curr_len = 1
Why Reset to 1?

When the increasing sequence breaks, the current element itself starts a new sequence of length 1.

Important Difference

Continuous means we cannot skip elements.

Example:

[1, 3, 5, 4, 7]

[1, 3, 5] → continuous increasing
[4, 7]    → continuous increasing
Memory Trick

CURRENT = current streak

MAX = best streak
