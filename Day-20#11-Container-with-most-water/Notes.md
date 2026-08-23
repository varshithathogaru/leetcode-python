
# Personal Notes

## Problem

LeetCode #11 - Container With Most Water

## Pattern

Two Pointers

## Core Formula

Area = min(height[left], height[right]) × (right - left)

## Approach

Start with two pointers:

left = 0
right = len(height) - 1

Calculate the current area and update the maximum.

Then move the pointer corresponding to the shorter height.

If:

height[left] < height[right]

move:

left += 1

Otherwise:

right -= 1

## Why Move the Shorter Pointer?

The shorter line limits the amount of water.

If we move the taller line, the width decreases while the limiting
height remains the shorter line.

Therefore, moving the taller line cannot improve the area.

Moving the shorter line gives us a chance to find a taller boundary.

## Example

Input:

[1,8,6,2,5,4,8,3,7]

Maximum area:

49

## Complexity

Time: O(n)

Space: O(1)

## Key Learning

When solving container/maximum-area problems, think:

Two Pointers → Calculate Area → Move Shorter Side
