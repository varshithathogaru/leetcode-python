
# Personal Notes

## Problem

LeetCode #3876 - Uniform Array

## Core Pattern

Observation + Minimum Odd Number

## Algorithm

1. Find the smallest odd number.
2. If there is no odd number, return True.
3. Check every even number.
4. If an even number is <= minimum odd, return False.
5. Otherwise return True.

## Important Condition

If an odd number exists:

even > minimum_odd

must be true for every even number.

## Example

nums = [5, 4, 9]

minimum odd = 5

4 <= 5

Therefore:

False

## Complexity

Time: O(n)

Space: O(1)

## Key Learning

Before trying to simulate operations, look for a mathematical
condition that determines whether the transformation is possible.
