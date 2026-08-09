# Personal Notes

## Pattern

Two Pointers

## Key Idea

Start with the widest possible container:

left = 0
right = len(height) - 1

Calculate the area and then move the pointer pointing to the shorter line.

## Area Formula

Area = min(height[left], height[right]) * (right - left)

## Why Move the Smaller Height?

The shorter line limits the amount of water.

If we move the taller line:

- Width decreases.
- The limiting height remains the same or may become smaller.

So there is no possibility of getting a better area by moving the taller pointer.

Moving the shorter pointer gives us a chance to find a taller boundary.

## Complexity

Time: O(n)
Space: O(1)

## Interview Tip

When a problem involves finding the best pair of elements while considering the distance between them, check whether a Two Pointer approach can eliminate unnecessary comparisons.
