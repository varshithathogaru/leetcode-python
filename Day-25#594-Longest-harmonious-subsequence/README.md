# LeetCode #594 - Longest Harmonious Subsequence

## 🧩 Problem Statement

A harmonious subsequence is a subsequence where the difference between
its maximum value and minimum value is exactly 1.

Given an integer array `nums`, return the length of the longest
harmonious subsequence.

## 💡 Approach

I solved this problem using a **Hash Map / Frequency Counting**
approach.

First, I count the frequency of every number.

Then, for each number `x`, I check whether `x + 1` exists.

If it exists, the values `x` and `x + 1` can form a harmonious
subsequence.

The length is:

freq[x] + freq[x + 1]

I keep track of the maximum length found.

## 🧠 Python Solution

```python
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        longest = 0

        for x in freq:
            if x + 1 in freq:
                longest = max(longest, freq[x] + freq[x + 1])

        return longest
