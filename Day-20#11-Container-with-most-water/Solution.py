class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_len = 0

        while i < j:
            ans = min(height[i], height[j]) * (j - i)
            max_len = max(ans, max_len)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return max_len
