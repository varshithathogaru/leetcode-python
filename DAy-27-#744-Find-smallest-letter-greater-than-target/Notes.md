
# Personal Notes

## Problem

LeetCode #744 - Find Smallest Letter Greater Than Target

## Pattern

Binary Search - First Element Greater Than Target

## Core Idea

We need:

letters[i] > target

The condition is STRICTLY greater.

Therefore:

if letters[mid] <= target:
    low = mid + 1

else:
    high = mid - 1

When the loop ends:

low = first element greater than target

## Why <= ?

The problem asks for a character strictly greater than the target.

Example:

letters = ["c", "f", "j"]
target = "f"

We cannot return "f".

Therefore:

f <= f

is True, so we move to the right.

## Wrap Around

If no character is greater than the target:

low == len(letters)

Use:

letters[low % len(letters)]

Example:

low = 3
len = 3

3 % 3 = 0

So we return the first character.

## Example

letters = ["c","f","j"]
target = "d"

Answer:

"f"

## Complexity

Time: O(log n)

Space: O(1)

## Key Learning

This is a variation of Binary Search where we search for the first
element satisfying:

element > target
