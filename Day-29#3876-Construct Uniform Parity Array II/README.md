# LeetCode #3876 - Uniform Array

## 🧩 Problem

Given an integer array, determine whether it can satisfy the required
uniformity condition using the allowed operations.

## 💡 Approach

I solved this problem using an observation based on the smallest odd
number.

### Step 1

Find the smallest odd number in the array.

### Step 2

If there is no odd number, return `True`.

### Step 3

If an odd number exists, check every even number.

Every even number must be strictly greater than the smallest odd number.

If any even number is less than or equal to the smallest odd number,
return `False`.

Otherwise, return `True`.

## 🧠 Python Solution

```python
class Solution:
    def uniformArray(self, nums: list[int]) -> bool:
        minodd = float('inf')

        for num in nums:
            if num % 2 != 0:
                minodd = min(minodd, num)

        if minodd == float('inf'):
            return True

        for num in nums:
            if num % 2 == 0 and num <= minodd:
                return False

        return True
