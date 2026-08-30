
# Personal Notes

## Problem

LeetCode #594 - Longest Harmonious Subsequence

## Pattern

Hash Map + Frequency Counting

## Core Idea

A harmonious subsequence must have:

max - min = 1

Therefore, for every number x, check whether:

x + 1

exists.

If it exists:

length = freq[x] + freq[x + 1]

Keep the maximum length.

## Example

nums = [1,3,2,2,5,2,3,7]

Frequency:

1 → 1
2 → 3
3 → 2
5 → 1
7 → 1

Check:

1 and 2 → 1 + 3 = 4

2 and 3 → 3 + 2 = 5

Therefore:

Answer = 5

## Why Not Sort?

Sorting would take:

O(n log n)

Using a frequency map gives:

O(n) average time.

## Complexity

Time: O(n) average

Space: O(n)

## Key Learning

When a problem involves frequencies and a fixed numerical
difference, a Hash Map can avoid sorting and make the solution
more efficient.
