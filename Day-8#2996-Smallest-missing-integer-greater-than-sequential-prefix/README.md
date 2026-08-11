# 🚀 LeetCode #2996 - Smallest Missing Integer Greater Than Sequential Prefix

## 🧩 Problem Statement

You are given a 0-indexed array of positive integers `nums`.

The sequential prefix is the longest prefix of `nums` such that:

`nums[i] = nums[i - 1] + 1`

for every `1 <= i < prefix length`.

Let the sum of the elements in the sequential prefix be `sum`.

Starting from `sum`, find the smallest integer that is not present in `nums`.

🔗 Problem Link:
https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix/

---

## 💡 Approach

I used a **Sequential Prefix + HashSet** approach.

### Algorithm

1. Start with the first element as the initial sequential prefix sum.
2. Traverse the array while consecutive elements increase by exactly `1`.
3. Add every element belonging to this sequential prefix to `total`.
4. Convert the array into a `set` for efficient membership checking.
5. Start the answer from the sequential prefix sum.
6. If the answer already exists in the set, increment it.
7. Return the first value that is not present in the array.

---

## 🧠 Python Solution

```python
from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        total = nums[0]
        i = 1

        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            total += nums[i]
            i += 1

        seen = set(nums)

        ans = total

        while ans in seen:
            ans += 1

        return ans
