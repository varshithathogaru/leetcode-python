
---

# 📝 `notes.md`

```markdown
# Personal Notes

## Problem

LeetCode #53 - Maximum Subarray

## Algorithm

Kadane's Algorithm

## Core Idea

At every position, decide whether to:

1. Start a new subarray.
2. Continue the previous subarray.

Formula:

curr_sum = max(nums[i], nums[i] + curr_sum)

Then update:

max_sum = max(max_sum, curr_sum)

## Important Insight

If the previous running sum is negative, carrying it forward can
decrease the sum of the next subarray.

Therefore, it can be better to start a new subarray.

## Example

nums = [-2,1,-3,4,-1,2,1,-5,4]

Maximum subarray:

[4,-1,2,1]

Maximum sum:

6

## Complexity

Time: O(n)

Space: O(1)
