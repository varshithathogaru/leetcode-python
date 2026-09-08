# Day 34 - Count Commas in Range

## LeetCode #3870

### Problem

Given an integer `n`, count the total number of commas used when writing all integers from `1` to `n` in standard number formatting.

---

## Observation

Numbers below `1000` contain no commas.

Numbers from `1000` onward contain one comma under the given constraints.

Therefore:

- `1 → 999` → 0 commas
- `1000 → n` → 1 comma each

---

## Formula


If:
n<1000

answer is:

0

Otherwise:

n - 1000 + 1

which simplifies to:

n - 999
n < 1000
