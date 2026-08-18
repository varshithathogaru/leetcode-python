# LeetCode 3471 — Find the Largest Almost Missing Integer

## 🧩 Problem

Given an integer array `nums` and an integer `k`, consider every contiguous subarray of length `k`.

An integer is called **almost missing** if it appears in exactly one of these windows.

Return the **largest almost missing integer**. If no such integer exists, return `-1`.

---

## 💡 Approach

For every window of size `k`:

1. Create a `set` containing the elements of the current window.
2. Iterate through the unique elements of that window.
3. Increment their window-frequency in a dictionary.
4. After processing all windows, find the largest number whose frequency is exactly `1`.

### Why use a `set`?

We are interested in whether a number appears in a **window**, not how many times it occurs inside that window.

For example:

```text
nums = [1, 2, 2, 3]
k = 3
```

The first window is:

```text
[1, 2, 2]
```

Its set is:

```text
{1, 2}
```

Both `1` and `2` should receive only **one window occurrence**, even though `2` appears twice inside the window.

---

## 🔍 Example

```text
nums = [3, 4, 3, 2, 3]
k = 3
```

Windows:

```text
[3, 4, 3] → {3, 4}
[4, 3, 2] → {2, 3, 4}
[3, 2, 3] → {2, 3}
```

Window frequencies:

```text
2 → 2 windows
3 → 3 windows
4 → 2 windows
```

No element appears in exactly one window.

Therefore:

```text
Answer = -1
```

---

## 🧠 Key Observation

The important distinction is:

> **Count how many windows contain an element, not how many times the element occurs overall.**

Using a set for every window automatically handles duplicate values inside the same window.

---

## 💻 Python Solution

```python
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        count = {}

        for i in range(len(nums) - k + 1):
            window = set(nums[i:i+k])

            for x in window:
                count[x] = count.get(x, 0) + 1

        ans = -1

        for x, y in count.items():
            if y == 1:
                ans = max(ans, x)

        return ans
```

---

## ⏱️ Complexity

Let `n = len(nums)`.

There are approximately `n - k + 1` windows.

Creating each window using slicing and converting it to a set takes up to `O(k)` time.

### Time Complexity

```text
O((n - k + 1) × k)
≈ O(nk)
```

### Space Complexity

```text
O(k + u)
```

where `u` is the number of distinct integers stored in `count`.

---

## 📚 Concepts Practiced

* Sliding Window
* Sets
* Hash Maps / Dictionaries
* Frequency Counting
* Subarrays
* Duplicate Handling
* Array Traversal

---

## 🚀 Takeaway

This problem reinforces an important sliding-window idea:

**When counting occurrences across windows, first make each window unique using a set, then count how many different windows contain each value.**

Daily LeetCode streak continues! 🔥

