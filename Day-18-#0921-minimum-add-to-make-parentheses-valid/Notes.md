# Personal Notes

## Problem

LeetCode #921 - Minimum Add to Make Parentheses Valid

## Pattern

Stack

## Core Idea

We need to find the minimum number of parentheses that must be added
to make the string valid.

I use a stack to keep track of unmatched opening parentheses `(`.

## Algorithm

1. If the character is `(`:
   - Add it to the stack.

2. If the character is `)`:
   - If the stack is not empty, remove one `(` because they form a
     valid pair.
   - Otherwise, this `)` has no matching `(`, so increment `addition`.

3. After processing the complete string:
   - Any remaining `(` in the stack need a matching `)`.

Therefore:

answer = addition + len(stack)

## Example

Input:

s = "()))(("

Processing gives:

unmatched `)` = 2
unmatched `(` = 2

Answer:

2 + 2 = 4

## Important Insight

Every unmatched closing parenthesis requires an opening parenthesis.

Every unmatched opening parenthesis requires a closing parenthesis.

## Complexity

Time: O(n)

Space: O(n)

## Optimized Approach

A stack is not strictly necessary for this problem because we only need
to know the number of unmatched opening parentheses.

We can use an integer counter instead, giving:

Time: O(n)
Space: O(1)

## Key Learning

Stack problems often involve matching elements in the correct order.

For parentheses problems, think:

Opening → store/match later
Closing → match with an available opening
