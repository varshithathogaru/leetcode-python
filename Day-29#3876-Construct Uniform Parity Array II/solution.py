class Solution:
    def uniformArray(self, nums: list[int]) -> bool:
        minodd = float('inf')

        for num in nums:
            if num % 2 != 0:
                minodd = min(minodd, num)

        if minodd == float('inf'):
            return True

        for num in nums:
            if num % 2 == 0 and num <= minodd:
                return False

        return True
