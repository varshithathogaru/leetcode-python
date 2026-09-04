
# Personal Notes

## Problem

LeetCode #766 - Toeplitz Matrix

## Pattern

Matrix + Diagonal Comparison

## Key Rule

For every cell:

matrix[i][j] == matrix[i-1][j-1]

If this condition fails:

return False

Otherwise:

return True

## Why Start From 1?

We need:

i - 1
j - 1

Therefore, both `i` and `j` must start from 1.

## Visual Pattern

1  2  3  4
5  1  2  3
9  5  1  2

Compare:

matrix[i][j]

with:

matrix[i-1][j-1]

## Complexity

Time: O(m × n)

Space: O(1)

## Interview Insight

For matrix problems, look for a relationship between the current
cell and neighboring cells before attempting a complicated traversal.
