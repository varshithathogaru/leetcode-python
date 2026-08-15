
---

# 📝 `notes.md`

```markdown
# Personal Notes

## Problem

LeetCode #3 - Longest Substring Without Repeating Characters

## Pattern

Sliding Window + HashSet

## Core Idea

Maintain a window containing only unique characters.

The `seen` set stores the characters currently inside the window.

## Important Condition

If:

s[right] in seen

there is a duplicate.

So remove characters from the left:

seen.remove(s[left])
left += 1

Continue until the duplicate is removed.

## Window Length

Current window:

right - left + 1

Update:

max_len = max(max_len, right - left + 1)

## Example

s = "abcabcbb"

The longest valid substring is:

"abc"

Length = 3

## Complexity

Time: O(n)

Space: O(k)

## Pattern to Remember

Expand → Detect duplicate → Shrink → Restore valid window → Update answer
