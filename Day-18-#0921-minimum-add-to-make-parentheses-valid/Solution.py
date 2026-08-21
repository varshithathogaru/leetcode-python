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
