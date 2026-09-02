# LeetCode #2091 - Removing Minimum and Maximum From Array

## 🧩 Problem Statement

Given an integer array `nums`, remove the minimum and maximum elements
using the minimum number of deletions.

In one deletion, we can remove an element from either the beginning or
the end of the array.

Return the minimum number of deletions required.

## 💡 Approach

I solved this problem using **Index Observation**.

First, I find the indices of the minimum and maximum elements.

Then I identify:

- `left` = earlier index
- `right` = later index

There are only three possible strategies.

### 1. Remove both from the front

We need to delete everything up to `right`.

```text
right + 1
