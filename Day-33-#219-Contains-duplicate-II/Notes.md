
# Day 33 Notes

## LeetCode #219 - Contains Duplicate II

### Main Pattern

Hash Map + Index Tracking

---

## Core Condition

We need:

nums[i] == nums[j]
and:

|i - j| <= k
Dictionary

Store:

value → latest index

Example:

d[5] = 3

means:

5 was most recently seen at index 3.
Algorithm
For every element:
        ↓
Is it already in dictionary?
        ↓
      YES
        ↓
Calculate index difference
        ↓
Difference <= k ?
        ↓
YES → True
NO  → Update index
