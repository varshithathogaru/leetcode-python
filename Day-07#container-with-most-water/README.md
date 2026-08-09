# 🚀 LeetCode #11 - Container With Most Water

## 🧩 Problem Statement

Given an integer array `height` where each element represents the height of a vertical line, find two lines that together with the x-axis form a container that holds the most water.

Return the maximum amount of water the container can store.

🔗 Problem Link:
https://leetcode.com/problems/container-with-most-water/

---

## 💡 Approach

I solved this problem using the **Two Pointers** technique.

I started with one pointer at the beginning of the array and another at the end.

For every pair of pointers:

1. Calculate the area using the shorter line.
2. Update the maximum area found so far.
3. Move the pointer pointing to the shorter line.
4. Continue until both pointers meet.

### Area Formula

```text
Area = min(height[left], height[right]) × (right - left)
