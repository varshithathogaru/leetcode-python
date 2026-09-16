# Day 42 Notes — Reverse Integer

## Core Pattern

TAKE → BUILD → REMOVE

```python
rem = x % 10
tot = tot * 10 + rem
x = x // 10
Important Operations
Get last digit
x % 10
Remove last digit
x // 10
Build reversed number
tot = tot * 10 + rem
Negative Numbers

Store the sign separately:

sign = -1 if x < 0 else 1
x = abs(x)

Restore it at the end:

tot = sign * tot
Overflow

Valid range:

-2^31 to 2^31 - 1

If outside the range:

return 0
Complexity

Time: O(d)

Space: O(1)

Memory Trick

%10 → TAKE last digit

*10 → SHIFT existing digits

+digit → ADD new digit

//10 → REMOVE last digit
