# LeetCode #3622 - Check Divisibility by Digit Sum and Product

## 🧩 Problem Statement

Given an integer `n`, calculate the sum and product of its digits.
Return `True` if `n` is divisible by the sum of its digits plus the
product of its digits. Otherwise, return `False.

## 💡 Approach

I solved this problem using digit manipulation.

### Steps

1. Store the original number because the number will be reduced
   while extracting its digits.
2. Extract each digit using `% 10`.
3. Calculate the digit sum.
4. Calculate the digit product.
5. Divide the original number by:

   digit_sum + digit_product

6. Return whether the remainder is zero.

## 🧠 Python Solution

```python
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        temp = n
        tot = 0
        product = 1

        while n != 0:
            dig = n % 10
            tot += dig
            product *= dig
            n //= 10

        return temp % (tot + product) == 0
