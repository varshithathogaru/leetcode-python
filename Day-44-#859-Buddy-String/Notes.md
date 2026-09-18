# Day 44 Notes — Buddy Strings

## Core Idea

Two strings are buddy strings if exactly one swap of two characters in `s` can make it equal to `goal`.

## Four-Step Pattern

### 1. Length

```python
if len(s) != len(goal):
    return False
2. Same Strings

If:

s == goal

there must be a duplicate character.

len(set(s)) < len(s)
3. Find Differences
diffs = [(a, b) for a, b in zip(s, goal) if a != b]
4. Check Reverse

There must be exactly two mismatches:

len(diffs) == 2

And they must be reversed:

diffs[0] == diffs[1][::-1]
Memory Trick

L → S → D → R

Length
Same
Differences
Reverse

Complexity

Time: O(n)

Space: O(n)
