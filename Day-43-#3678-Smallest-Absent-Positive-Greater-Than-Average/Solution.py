from typing import List

class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        avg = sum(nums) // len(nums)

        candidate = max(1, avg + 1)
        seen = set(nums)

        while candidate in seen:
            candidate += 1

        return candidate
