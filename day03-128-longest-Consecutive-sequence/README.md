# 🚀 LeetCode #128 - Longest Consecutive Sequence

## 🧩 Problem Statement

Given an unsorted array of integers `nums`, return the length of the longest consecutive sequence.

Your algorithm should run in **O(n)** time.

🔗 **Problem Link:** https://leetcode.com/problems/longest-consecutive-sequence/

---

## 💡 Approach

A straightforward solution would sort the array first, but sorting requires **O(n log n)** time.

Instead, I used a **HashSet** to achieve **O(n)** time complexity.

### Algorithm

1. Store all numbers in a HashSet for constant-time lookups.
2. Identify the start of a sequence by checking if `num - 1` is **not** present.
3. Count the sequence length by checking consecutive numbers.
4. Track the maximum sequence length found.

This ensures every sequence is counted only once.

---

## 🧠 Python Solution

```python
from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_s = set(nums)
        max1 = 0

        for num in num_s:
            if num - 1 not in num_s:
                length = 1
                while num + length in num_s:
                    length += 1
                max1 = max(max1, length)

        return max1
```

---

## ⏱️ Complexity Analysis

| Complexity | Value |
|------------|-------|
| Time Complexity | **O(n)** |
| Space Complexity | **O(n)** |

---

## 📚 Key Learnings

- HashSet provides **O(1)** average lookup time.
- Instead of sorting, identify the beginning of each sequence.
- Processing only sequence starters avoids unnecessary work.
- Choosing the right data structure can significantly improve performance.

---

## 🏷️ Topics

- HashSet
- Arrays
- Data Structures
- Python
- LeetCode

---

## ⭐ Status

✅ Accepted

Part of my **Daily Coding Log** and **#45DaysOfGrowth** challenge.
