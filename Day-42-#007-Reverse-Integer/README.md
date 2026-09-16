# Day 42 — Reverse Integer

## LeetCode #7

### Problem

Given a signed 32-bit integer `x`, return `x` with its digits reversed.

If reversing `x` causes the value to go outside the signed 32-bit integer range:

`[-2^31, 2^31 - 1]`

return `0`.

### Approach

1. Store the sign of the number.
2. Convert the number to its absolute value.
3. Extract the last digit using `% 10`.
4. Add the digit to the reversed number.
5. Remove the last digit using `// 10`.
6. Restore the original sign.
7. Check the 32-bit integer range.
8. Return the result or `0` if overflow occurs.

### Example

Input:

`123`

Process:

`123 → 12 → 1 → 0`

Reversed number:

`321`

Output:

`321`

### Negative Example

Input:

`-123`

Output:

`-321`

### Important Formula

```text
last digit = x % 10

remove last digit = x // 10

reverse = reverse * 10 + last digit
