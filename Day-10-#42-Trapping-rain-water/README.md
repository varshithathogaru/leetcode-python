# 🚀 LeetCode #42 - Trapping Rain Water

## 🧩 Problem Statement

Given an array of non-negative integers representing an elevation map,
where the width of each bar is 1, calculate how much rainwater can be
trapped after raining.

🔗 Problem:
https://leetcode.com/problems/trapping-rain-water/

---

## 💡 Approach

I solved this problem using the **Two Pointer** technique.

Instead of creating separate arrays to store the maximum height from
the left and right for every position, I maintained two pointers and
tracked:

- `leftmax` → maximum height seen from the left
- `rightmax` → maximum height seen from the right

At each step, I processed the side with the smaller maximum height.

If `leftmax < rightmax`, the water trapped at the current left position
depends on `leftmax`.

Otherwise, the water trapped at the current right position depends on
`rightmax`.

### Water Calculation

```text
Water = max_height - current_height
