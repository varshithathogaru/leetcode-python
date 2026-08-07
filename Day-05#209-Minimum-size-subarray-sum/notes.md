# Personal Notes

## Pattern

Sliding Window

## Why Sliding Window?

Since the problem asks for a **contiguous subarray** and all elements are positive, the Sliding Window technique allows us to efficiently expand and shrink the window while maintaining the required sum.

## Key Idea

- Expand the window until the sum reaches the target.
- Shrink the window to find the smallest valid subarray.
- Keep updating the minimum length.

## Common Mistakes

- Forgetting to update the minimum length before shrinking the window.
- Not handling the case where no valid subarray exists.
- Using nested loops instead of the optimized Sliding Window approach.

## Interview Tip

Whenever you see:
- Contiguous subarray
- Positive integers
- Minimum/Maximum window

Consider using the **Sliding Window** technique.
