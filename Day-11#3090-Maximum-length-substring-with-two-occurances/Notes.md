
---

# 📝 `notes.md`

```markdown
# Personal Notes

## Problem

LeetCode #3090 - Maximum Length Substring With Two Occurrences

## Pattern

Sliding Window + Frequency Map

## Core Idea

Maintain a window where every character appears at most twice.

Use:

l → left pointer
r → right pointer

The dictionary stores the frequency of characters.

## Important Condition

If:

m[s[r]] > 2

the window becomes invalid.

So move the left pointer:

m[s[l]] -= 1
l += 1

until the window becomes valid again.

## Window Length

Current window length:

r - l + 1

Update the answer using:

ans = max(ans, r - l + 1)

## Complexity

Time: O(n)

Space: O(k)

where k is the number of distinct characters.

## Pattern to Remember

Expand → Check constraint → Shrink → Update answer

This is a common Sliding Window pattern used in many
string and subarray problems.
