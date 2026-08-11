# Personal Notes

## Pattern

Sequential Prefix + HashSet

## Key Idea

First find the longest sequential prefix.

For example:

nums = [1, 2, 3, 5, 6]

Sequential prefix:

1 → 2 → 3

Sum:

1 + 2 + 3 = 6

Then check whether 6 exists in the array.

Since 6 exists, try 7.

If 7 does not exist, return 7.

## Important Conditions

A number belongs to the sequential prefix only when:

nums[i] == nums[i - 1] + 1

## Why HashSet?

A set allows efficient checking:

ans in seen

instead of repeatedly searching through the entire array.

## Complexity

Time: O(n)

Space: O(n)

## Interview Tip

When a problem asks you to repeatedly check whether values exist in an array, consider using a HashSet for faster membership checks.
