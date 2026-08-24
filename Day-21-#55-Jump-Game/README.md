# LeetCode #55 - Jump Game

## 🧩 Problem Statement

Given an integer array `nums`, where each element represents the
maximum jump length from that position, determine whether you can
reach the last index.

## 💡 Approach

I solved this problem using a **Backward Greedy** approach.

Instead of starting from index `0`, I start from the last index and
work backwards.

I maintain a variable called `final`, which represents the current
target position.

For every index:

```text
i + nums[i] >= final
