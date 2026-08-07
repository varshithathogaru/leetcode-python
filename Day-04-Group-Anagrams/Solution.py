"""
LeetCode #209 - Minimum Size Subarray Sum

Approach:
- Sliding Window
- Two Pointers

Time Complexity: O(n)
Space Complexity: O(1)

Author: Varshitha Thogaru
GitHub: https://github.com/varshithathogaru
"""

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

        return min1
