
# Day 37 Notes — Relative Ranks

## Pattern
Sorting + Index Tracking

## Core Idea

Do NOT sort the original score array.

Create indices:

python
idx = list(range(n))

Sort the indices according to the scores:

idx.sort(key=lambda x: -score[x])
Important

In:

for i, j in enumerate(idx):

i = rank position

j = original index

Therefore:

ans[j]

is used to preserve original order.

Ranking
i = 0 → Gold Medal
i = 1 → Silver Medal
i = 2 → Bronze Medal
i >= 3 → str(i + 1)
Memory Trick

Sort indices → Preserve positions

Complexity

Time: O(n log n)

Space: O(n)
