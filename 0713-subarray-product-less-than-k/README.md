# 🚀 LeetCode #713 - Subarray Product Less Than K

## 🧩 Problem Statement

Given an array of positive integers `nums` and an integer `k`, return the number of contiguous subarrays where the product of all the elements in each subarray is **strictly less than** `k`.

🔗 **Problem Link:** https://leetcode.com/problems/subarray-product-less-than-k/

---

## 💡 Approach

A brute-force approach would generate every possible subarray and calculate its product, resulting in a time complexity of **O(n²)**.

To optimize this, I used the **Sliding Window** technique.

### Algorithm

1. Initialize two pointers (`left` and `right`) to represent the current window.
2. Maintain the product of all elements inside the window.
3. Expand the window by moving the `right` pointer.
4. If the product becomes greater than or equal to `k`, shrink the window from the left until the product is less than `k`.
5. At every position, count all valid subarrays ending at the current `right` index.

This allows the array to be traversed only once.

---

## 🧠 Python Solution

```python
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        left = 0
        product = 1
        count = 0

        for right in range(len(nums)):
            product *= nums[right]

            while product >= k:
                product //= nums[left]
                left += 1

            count += right - left + 1

        return count
```

---

## ⏱️ Complexity Analysis

| Complexity | Value |
|------------|-------|
| Time Complexity | **O(n)** |
| Space Complexity | **O(1)** |

---

## 📚 Key Learnings

- Sliding Window is an efficient technique for solving many contiguous subarray problems.
- Maintaining a running product eliminates the need to recalculate products repeatedly.
- Whenever a window violates the condition (`product >= k`), shrink it until it becomes valid again.
- The number of valid subarrays ending at each index can be calculated using:

```
right - left + 1
```

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

Part of my **Daily Coding Log** and **#45DaysOfGrowth** challenge.
