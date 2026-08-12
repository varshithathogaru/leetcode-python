# Personal Notes

## Pattern

KMP (Knuth-Morris-Pratt)

## Main Concept

KMP uses an LPS array to avoid unnecessary comparisons.

LPS means:

Longest Prefix which is also Suffix.

## Important Part

If:

l = lps[-1]

then:

pattern_length = n - l

If:

n % pattern_length == 0

the string can be constructed by repeating the same substring.

## Example

s = "abab"

LPS:

[0, 0, 1, 2]

l = 2

n = 4

pattern_length = 4 - 2 = 2

4 % 2 == 0

Therefore:

"ab" + "ab"

Answer = True

## Important KMP Rule

When characters don't match and:

length != 0

we do:

length = lps[length - 1]

We do NOT immediately increment `i`.

This allows KMP to reuse previously calculated prefix information.

## Complexity

Time: O(n)

Space: O(n)

## Personal Learning

I initially knew this problem could be solved using simpler string techniques, but I intentionally used KMP to understand the algorithm and practiced the LPS construction through a dry run.
