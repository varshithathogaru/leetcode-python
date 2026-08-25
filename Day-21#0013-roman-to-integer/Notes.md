
# Personal Notes

## Problem

LeetCode #13 - Roman to Integer

## Pattern

Hash Map + Current/Next Comparison

## Roman Values

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

## Core Idea

Compare the current Roman symbol with the next symbol.

If:

current < next

subtract current.

Otherwise:

add current.

## Examples

IV:

1 < 5

-1 + 5 = 4

IX:

1 < 10

-1 + 10 = 9

VI:

5 < 1 → False

5 + 1 = 6

## Important Insight

A smaller value before a larger value represents subtraction.

Examples:

IV = 4
IX = 9
XL = 40
XC = 90
CD = 400
CM = 900

## Complexity

Time: O(n)

Space: O(1)

## Key Learning

When processing a sequence, sometimes comparing the current element
with the next element can simplify the logic.
