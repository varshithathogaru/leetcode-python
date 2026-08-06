"""
LeetCode #49 - Group Anagrams

Problem:
Given an array of strings, group the anagrams together.

Approach:
- Use a Python dictionary (HashMap).
- Sort each string to create a unique key.
- Store all words with the same sorted key in the same list.
- Return all grouped anagrams.

Time Complexity: O(n × k log k)
Space Complexity: O(n × k)

where:
n = Number of strings
k = Maximum length of a string

Author: Varshitha Thogaru
GitHub: https://github.com/varshithathogaru
"""

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for i in strs:
            key = "".join(sorted(i))

            if key not in d:
                d[key] = []

            d[key].append(i)

        return list(d.values())
