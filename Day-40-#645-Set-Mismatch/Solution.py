class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        n = len(nums)

        freq = {}
        dup = miss = -1

        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        for i in range(1, n + 1):
            if freq.get(i, 0) == 2:
                dup = i

            if freq.get(i, 0) == 0:
                miss = i

        return [dup, miss]
