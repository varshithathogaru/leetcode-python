# 🚀 LeetCode #209 - Minimum Size Subarray Sum

## 🧩 Problem Statement

Given an array of positive integers `nums` and a positive integer `target`, return the **minimum length** of a contiguous subarray whose sum is greater than or equal to `target`. If no such subarray exists, return `0`.

🔗 **Problem Link:** https://leetcode.com/problems/minimum-size-subarray-sum/

---

## 💡 Approach

I solved this problem using the **Sliding Window** technique.

### Algorithm

1. Initialize two pointers (`left` and `right`) to represent the current window.
2. Expand the window by moving the `right` pointer and keep track of the current sum.
3. Whenever the sum becomes greater than or equal to the target, update the minimum window length.
4. Shrink the window from the left while maintaining the condition.
5. If no valid subarray exists, return `0`.

This approach processes the array efficiently in a single traversal.

---

## 🧠 Python Solution

```python
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        sum1 = 0
        min1 = float("inf")

        for right in range(len(nums)):
            sum1 += nums[right]

            while sum1 >= target:
                min1 = min(min1, right - left + 1)
                sum1 -= nums[left]
                left += 1

        if min1 == float("inf"):
            return 0
        else:
            return min1
```

---

## ⏱️ Complexity Analysis

| Complexity | Value |
|------------|-------|
| Time Complexity | **O(n)** |
| Space Complexity | **O(1)** |

---

## 📚 Key Learnings

- Sliding Window is an efficient technique for contiguous subarray problems.
- Expanding and shrinking the window dynamically avoids checking every possible subarray.
- Keeping track of the minimum valid window helps solve the problem in linear time.

---

## 🏷️ Topics

- Sliding Window
- Two Pointers
- Arrays
- Python
- LeetCode

---

## ⭐ Status

✅ Accepted

Part of my **#45DaysOfGrowth** challenge.
