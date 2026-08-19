
---

# 📝 `notes.md`

```markdown
# Personal Notes

## Problem

LeetCode #557 - Reverse Words in a String III

## Pattern

Two Pointers + String Manipulation

## Core Idea

Reverse every word individually while keeping the word order unchanged.

For each word:

i → beginning
j → end

Swap:

chars[i], chars[j] = chars[j], chars[i]

Then move:

i += 1
j -= 1

Continue until the pointers meet.

## Important Python Concept

Strings are immutable in Python.

Therefore, convert the word into a list:

chars = list(word)

After reversing:

"".join(chars)

## Complexity

Time: O(n)

Space: O(n)
