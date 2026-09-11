# Day 37 - Relative Ranks

## 🚀 LeetCode #506

### Problem

Given the scores of athletes, return their relative ranks.

The athlete with the highest score gets:

- Gold Medal
- Silver Medal
- Bronze Medal

The remaining athletes receive their numerical rank.

The result must be returned in the original order of the athletes.

---

## 💡 Approach

I used an index-tracking approach.

Instead of sorting the original score array, I created an array containing the original indices.

Example:

```text
score = [10, 3, 8, 9, 4]

indices = [0, 1, 2, 3, 4]
