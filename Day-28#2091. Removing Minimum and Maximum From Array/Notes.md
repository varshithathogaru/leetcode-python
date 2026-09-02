
# Personal Notes

## Problem

LeetCode #2091 - Removing Minimum and Maximum From Array

## Core Idea

Find the indices of minimum and maximum.

Let:

left = smaller index
right = larger index

There are only 3 possibilities.

### Case 1: Both from front

front = right + 1

### Case 2: Both from back

back = n - left

### Case 3: One from each side

both = (left + 1) + (n - right)

Answer:

min(front, back, both)

## Important Formula

If:

left = earlier index
right = later index

Then:

Front = right + 1

Back = n - left

Both = left + 1 + n - right

## Complexity

Time: O(n)

Space: O(1)

## Interview Insight

When deletion is allowed only from the two ends, first locate the
important elements and compare the possible ways of reaching them
from the ends.

Instead of simulating deletions, calculate the cost of each possible
strategy.
