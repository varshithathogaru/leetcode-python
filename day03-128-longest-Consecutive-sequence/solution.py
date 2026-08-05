"""
LeetCode #128 - Longest Consecutive Sequence

Approach:
- HashSet
- Sequence Detection

Time Complexity: O(n)
Space Complexity: O(n)

Author: Varshitha Thogaru
GitHub: https://github.com/varshithathogaru
"""

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
