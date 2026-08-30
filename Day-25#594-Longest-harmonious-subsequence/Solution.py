from typing import List

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
