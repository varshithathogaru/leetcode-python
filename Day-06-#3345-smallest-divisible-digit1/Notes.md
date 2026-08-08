# Personal Notes

## Pattern

Brute Force + Digit Manipulation

## Key Idea

For every number starting from `n`, calculate the product of its digits.

If:

digit_product % t == 0

then that number is the answer.

## Digit Extraction

`temp % 10` → gets the last digit

`temp // 10` → removes the last digit

## Example

For `n = 15`:

15 → 1 × 5 = 5

16 → 1 × 6 = 6

17 → 1 × 7 = 7

18 → 1 × 8 = 8

...

The first number whose digit product is divisible by `t` is returned.

## Complexity

Time: O(d)

Space: O(1)
