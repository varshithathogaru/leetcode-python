from typing import List

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        min_indx = nums.index(min(nums))
        max_indx = nums.index(max(nums))

        left = min(min_indx, max_indx)
        right = max(min_indx, max_indx)

        front = right + 1
        back = n - left
        both = (left + 1) + (n - right)

        return min(front, back, both)
