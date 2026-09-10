# Day 36 - Longest Common Prefix

LeetCode #14

## Pattern
String / Prefix Matching

## Approach
1. Take the first string as the initial prefix.
2. Compare it with every other string.
3. If a string does not start with the prefix, remove the last character.
4. Continue until the string starts with the prefix.
5. If the prefix becomes empty, return "".
6. Return the final prefix.

## Key Function
startswith()

Example:
"flower".startswith("flow") -> True
"flower".startswith("flx") -> False

## Memory Trick
Assume first -> Compare -> Shrink -> Return

## Complexity
Time: O(N * M^2) worst case
Space: O(M)
