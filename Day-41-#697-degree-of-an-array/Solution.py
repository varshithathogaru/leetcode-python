from typing import List

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count, first, last = {}, {}, {}

        for i, x in enumerate(nums):
            if x not in first:
                first[x] = i

            last[x] = i
            count[x] = count.get(x, 0) + 1

        degree = max(count.values())
        min_len = len(nums)

        for x in count:
            if count[x] == degree:
                min_len = min(min_len, last[x] - first[x] + 1)

        return min_len
