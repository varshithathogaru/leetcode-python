# Day 41 Notes — Degree of an Array

## Core Pattern

VALUE → COUNT + FIRST + LAST

## Important Formula

Subarray length:

last_index - first_index + 1

## Degree

Degree = maximum frequency of any element.

## Algorithm

1. Count every element.
2. Store first occurrence.
3. Store last occurrence.
4. Find maximum frequency.
5. Check only elements having maximum frequency.
6. Find their range lengths.
7. Return the minimum.

## Memory Trick

C-F-L

C = Count
F = First
L = Last

Degree → Find maximum Count

Answer → Minimum(Last - First + 1)

## Complexity

Time: O(n)

Space: O(n)

## Interview Explanation

"I used three hash maps to track the frequency, first occurrence, and last occurrence of each element. After finding the degree of the array, I considered only the elements having that degree and calculated the length between their first and last occurrences. The minimum of these lengths is the answer."
