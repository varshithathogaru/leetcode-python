
# 🚀 LeetCode #49 - Group Anagrams

## 🧩 Problem Statement

Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.

An anagram is a word or phrase formed by rearranging the letters of another word while using all the original letters exactly once.

🔗 **Problem Link:** https://leetcode.com/problems/group-anagrams/

---

## 💡 Approach

I solved this problem using a **Python Dictionary (HashMap)**.

The main idea is that two words are anagrams if their sorted characters are the same.

### Algorithm

1. Create an empty dictionary.
2. Traverse through each string in the input list.
3. Sort the characters of the current string.
4. Convert the sorted characters into a string and use it as the dictionary key.
5. If the key does not exist, create a new empty list.
6. Append the original string to the corresponding list.
7. Return all grouped values from the dictionary.

This approach efficiently groups all anagrams together.

---

## 🧠 Python Solution

```python
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for i in strs:
            key = "".join(sorted(i))

            if key not in d:
                d[key] = []

            d[key].append(i)

        return list(d.values())
```

---

## ⏱️ Complexity Analysis

| Complexity | Value |
|------------|-------|
| Time Complexity | **O(n × k log k)** |
| Space Complexity | **O(n × k)** |

Where:
- **n** = Number of strings
- **k** = Maximum length of a string

---

## 📚 Key Learnings

- A dictionary can efficiently group related elements.
- Sorting each string creates a unique identifier for all of its anagrams.
- Using the sorted string as a key simplifies the grouping process.
- Choosing the right data structure can make the solution clean and easy to understand.

---

## 🏷️ Topics

- HashMap (Dictionary)
- Strings
- Sorting
- Python
- LeetCode

---

## ⭐ Status

✅ Accepted

Part of my **#45DaysOfGrowth** challenge.
