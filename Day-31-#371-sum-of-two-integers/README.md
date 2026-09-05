# Day 31 — Sum of Two Integers | LeetCode #371

## 🧩 Problem

Given two integers `a` and `b`, return their sum without using the `+` and `-` operators.

**LeetCode:** #371 — Sum of Two Integers

**Difficulty:** Medium

**Topic:** Bit Manipulation

---

## 💡 Approach

We can perform addition using bitwise operators.

Normal binary addition has two components:

1. Sum without carry
2. Carry

We can calculate both using bitwise operations.

### 1. XOR (`^`) — Sum Without Carry

python(XOR)
a ^ b

XOR gives the sum of two bits without considering the carry.

Truth table:

A	B	A ^ B
0	0	0
0	1	1
1	0	1
1	1	0

For 1 + 1, XOR produces 0, while the carry is handled separately.

2. AND (&) — Find Carry
a & b

A carry is generated when both corresponding bits are 1.

1 & 1 = 1

Therefore:

a & b

identifies the positions where a carry is generated.

3. Left Shift (<< 1) — Move Carry

The carry must be moved one position to the left because it belongs to the next higher bit.

(a & b) << 1

This gives the carry value that needs to be added.

🔄 Algorithm

Repeat the following steps until there is no carry:

sum   = a ^ b
carry = (a & b) << 1

Then:

a = sum
b = carry

When the carry becomes 0, a contains the final answer.

🧪 Example
Input
a = 5
b = 3

Binary representation:

5 = 0101
3 = 0011
Step 1

Calculate sum without carry:

0101
0011
----
0110

0110 = 6

Calculate carry:

0101
0011
----
0001

0001 << 1 = 0010

So:

a = 0110
b = 0010
Step 2
0110
0010
----
0100

Sum without carry = 0100

Carry:

0110
0010
----
0010

0010 << 1 = 0100

So:

a = 0100
b = 0100
Step 3
0100
0100
----
0000

Carry:

0100
0100
----
0100

0100 << 1 = 1000

So:

a = 0000
b = 1000
Step 4
0000
1000
----
1000

Carry:

0000 & 1000 = 0000

No carry remains.

Therefore:

1000 = 8
Output
8
