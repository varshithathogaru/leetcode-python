# Day 40 - Set Mismatch

## 🚀 LeetCode #645

### Problem

You are given an array containing numbers from `1` to `n`.

Due to an error:

- One number appears twice.
- One number is missing.

Return the duplicate number and the missing number.

---

## 💡 Approach

I used a frequency dictionary to count how many times each number occurs.

### Steps

1. Create a frequency dictionary.
2. Count the occurrence of every number in `nums`.
3. Iterate from `1` to `n`.
4. If a number has frequency `2`, it is the duplicate.
5. If a number has frequency `0`, it is the missing number.
6. Return `[duplicate, missing]`.

---

## 🔍 Example

### Input

```text
[1, 2, 2, 4]
The numbers should be:

[1, 2, 3, 4]

But:

2 → appears twice
3 → is missing
Output
[2, 3]
