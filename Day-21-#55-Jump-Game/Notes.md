
# Personal Notes

## Problem

LeetCode #55 - Jump Game

## Pattern

Greedy - Backward Approach

## Core Idea

Start from the last index and treat it as the target.

Move from right to left.

If:

i + nums[i] >= target

then the current index can reach the target.

Therefore:

target = i

At the end:

target == 0

means the last index is reachable.

## Example

nums = [2,3,1,1,4]

Initial:

target = 4

Index 3:

3 + 1 >= 4
target = 3

Index 2:

2 + 1 >= 3
target = 2

Index 1:

1 + 3 >= 2
target = 1

Index 0:

0 + 2 >= 1
target = 0

Answer:

True

## Important Insight

Instead of trying every possible jump, find the earliest position
that can reach the current target.

Then that position becomes the new target.

## Complexity

Time: O(n)

Space: O(1)

## Key Learning

When a problem asks whether the final position is reachable, consider
working backwards and maintaining a reachable target.
