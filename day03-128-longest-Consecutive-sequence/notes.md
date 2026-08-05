# Personal Notes

## Pattern

HashSet + Sequence Detection

## Why HashSet?

A HashSet allows constant-time lookups, making it possible to check whether consecutive numbers exist without sorting the array.

## Key Idea

Only start counting a sequence if:

num - 1 is NOT present.

This ensures every consecutive sequence is processed exactly once.

## Common Mistakes

- Sorting the array instead of using a HashSet.
- Starting the count from every element, leading to repeated work.
- Forgetting to handle duplicate values.

## Interview Tip

Whenever a problem asks for efficient lookup or consecutive elements in an unsorted array, consider using a HashSet before thinking about sorting.
