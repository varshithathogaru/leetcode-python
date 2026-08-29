
# Personal Notes

## Problem

LeetCode #290 - Word Pattern

## Pattern

Hash Map + Two-Way Mapping

## Core Idea

Each pattern character must map to exactly one word.

Each word must map back to exactly one pattern character.

Therefore, use two mappings:

char → word

word → char

## Why Two Dictionaries?

Consider:

pattern = "ab"
s = "dog dog"

If we only use:

char → word

we might get:

a → dog
b → dog

But this is invalid.

The reverse mapping detects the conflict:

dog → a

Then trying:

dog → b

is not allowed.

## Algorithm

1. Split the string into words.
2. Check if the lengths match.
3. Traverse pattern and words together.
4. Check character → word.
5. Check word → character.
6. Add the mappings if valid.
7. Return True if no conflict occurs.

## Example

pattern = "abba"

s = "dog cat cat dog"

Mapping:

a → dog
b → cat

Result:

True

## Important Python Concepts

### split()

Converts a string into words:

s.split()

### zip()

Pairs elements:

zip(pattern, words)

Example:

pattern = "ab"
words = ["dog", "cat"]

Pairs:

(a, dog)
(b, cat)

## Complexity

Time: O(n)

Space: O(n)

## Key Learning

When two different types of objects need to have a one-to-one
relationship, a two-way mapping can be useful.
