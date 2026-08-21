# LeetCode #921 - Minimum Add to Make Parentheses Valid

## 🧩 Problem Statement

Given a string containing parentheses, find the minimum number of
parentheses that must be added to make the string valid.

## 💡 Approach

I solved this problem using a Stack.

- Store unmatched opening parentheses in the stack.
- When a closing parenthesis is found:
  - If an opening parenthesis exists, remove it from the stack.
  - Otherwise, an opening parenthesis needs to be added.
- At the end, every remaining opening parenthesis needs a matching
  closing parenthesis.

Therefore:

answer = unmatched closing parentheses + unmatched opening parentheses

## 🧠 Python Solution

```python
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        addition = 0

        for ch in s:
            if ch == '(':
                stack.append(ch)
            else:
                if stack:
                    stack.pop()
                else:
                    addition += 1

        return addition + len(stack)
