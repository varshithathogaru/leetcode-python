# Day 32 - String to Integer (atoi)

## LeetCode #8

### Problem

Convert a string into a 32-bit signed integer according to the rules of the `atoi` function.

---

## Approach

The solution follows these steps:

1. Remove leading whitespace.
2. Check for a positive or negative sign.
3. Read consecutive digits.
4. Build the integer using:

result = result * 10 + digit
