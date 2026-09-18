# Day 44 — Buddy Strings

## LeetCode #859

### Problem

Given two strings `s` and `goal`, determine whether we can make `s` equal to `goal` by swapping exactly two characters in `s`.

### Approach

There are two major cases.

### Case 1: Different Lengths

If the lengths are different, return `False`.

### Case 2: Strings Are Already Equal

If `s == goal`, we need at least one duplicate character.

Why?

Swapping two identical characters keeps the string unchanged.

This is checked using:

```python
len(set(s)) < len(s)
