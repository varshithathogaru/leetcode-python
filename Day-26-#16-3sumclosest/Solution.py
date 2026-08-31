from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        closest = nums[0] + nums[1] + nums[2]
        n = len(nums)

        for i in range(n - 2):
            j = i + 1
            k = n - 1

            while j < k:
                current = nums[i] + nums[j] + nums[k]

                if abs(current - target) < abs(closest - target):
                    closest = current

                if current < target:
                    j += 1
                elif current > target:
                    k -= 1
                else:
                    return target

        return closest
