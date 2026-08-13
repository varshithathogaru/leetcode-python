
---

# 📝 `notes.md`

```markdown
# Personal Notes

## Problem

LeetCode #42 - Trapping Rain Water

## Pattern

Two Pointers

## Core Idea

Water trapped at a position depends on the smaller of the
maximum height from the left and right.

Instead of storing left and right maximum arrays, maintain:

leftmax
rightmax

and two pointers:

l
r

## Decision

If:

leftmax < rightmax

process the left side.

Otherwise:

process the right side.

## Formula

Left side:

water = leftmax - height[l]

Right side:

water = rightmax - height[r]

## Complexity

Time: O(n)

Space: O(1)

## Important Learning

The key optimization is avoiding additional arrays.

By maintaining the maximum boundaries while moving two pointers,
we can calculate the trapped water in a single traversal.
