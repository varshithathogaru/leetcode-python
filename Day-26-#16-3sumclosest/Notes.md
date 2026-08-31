
# Personal Notes

## Problem

LeetCode #16 - 3Sum Closest

## Pattern

Sorting + Two Pointers

## Core Idea

Sort the array.

Fix one element.

Use two pointers for the remaining elements:

left = i + 1
right = n - 1

Calculate:

current = nums[i] + nums[left] + nums[right]

Compare the current sum with the target.

## Pointer Movement

If:

current < target

Move:

left += 1

Because the array is sorted, this can increase the sum.

If:

current > target

Move:

right -= 1

This can decrease the sum.

If:

current == target

Return target immediately.

## Tracking the Closest Sum

Calculate:

abs(current - target)

If this difference is smaller than the previous difference,
update the closest sum.

## Example

nums = [-1,2,1,-4]

target = 1

Sorted:

[-4,-1,1,2]

Closest sum:

2

## Complexity

Time: O(n²)

Space: O(1) extra space

## Key Learning

Sorting can make Two Pointer decisions possible.

For a sum that is too small → move left forward.

For a sum that is too large → move right backward.
