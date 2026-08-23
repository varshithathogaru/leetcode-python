# LeetCode #11 - Container With Most Water

## 🧩 Problem Statement

Given an integer array `height`, find two lines that together with
the x-axis form a container that can hold the maximum amount of water.

## 💡 Approach

I solved this problem using the **Two Pointer** technique.

### Steps

1. Place one pointer at the beginning of the array.
2. Place another pointer at the end.
3. Calculate the area between the two lines.
4. Update the maximum area.
5. Move the pointer pointing to the shorter line.
6. Continue until the pointers meet.

The area is calculated as:

```text
min(height[left], height[right]) × (right - left)
