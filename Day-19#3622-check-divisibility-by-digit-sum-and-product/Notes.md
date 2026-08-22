
---

# 📝 `notes.md`

```markdown
# Personal Notes

## Problem

LeetCode #3622 - Check Divisibility by Digit Sum and Product

## Pattern

Digit Manipulation + Math

## Core Idea

Extract each digit of the number and calculate:

1. Sum of digits
2. Product of digits

Then check:

n % (digit_sum + digit_product) == 0

## Digit Extraction

Last digit:

digit = n % 10

Remove last digit:

n //= 10

## Example

n = 123

Digits:

3 → 2 → 1

Digit Sum:

3 + 2 + 1 = 6

Digit Product:

3 × 2 × 1 = 6

Sum + Product:

6 + 6 = 12

Check:

123 % 12 != 0

Result:

False

## Important Point

Store the original number before modifying n:

temp = n

because n becomes 0 after repeatedly applying:

n //= 10

## Complexity

Time: O(d)

Space: O(1)

where d is the number of digits.

## Key Learning

A single loop can calculate multiple properties of a number while
extracting its digits.
