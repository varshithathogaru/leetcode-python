
# Day 35 Notes

## LeetCode #1160 - Find Words That Can Be Formed by Characters

### Main Pattern

Frequency Map

---

## Core Idea

Count:

1. Characters available
2. Characters required by each word

Then compare them.

```text
AVAILABLE → Counter(chars)

REQUIRED → Counter(word)

REQUIRED <= AVAILABLE
        ↓
      VALID
