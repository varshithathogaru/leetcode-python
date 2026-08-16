
---

# 📝 notes.md

```markdown
# Personal Notes

## Problem

LeetCode #367 - Valid Perfect Square

## Pattern

Binary Search

## Core Idea

A perfect square has an integer `x` such that:

x * x = num

Instead of checking every possible `x`, use Binary Search.

## Decision

If:

mid * mid == num

return True.

If:

mid * mid < num

search right:

low = mid + 1

If:

mid * mid > num

search left:

high = mid - 1

## Edge Cases

0 → True
1 → True

That's why:

if num < 2:
    return True

## Complexity

Time: O(log n)

Space: O(1)
