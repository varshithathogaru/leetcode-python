# LeetCode #557 - Reverse Words in a String III

## 🧩 Problem Statement

Given a string `s`, reverse the characters of each word in the
sentence while preserving the original word order and spaces.

🔗 Problem:
https://leetcode.com/problems/reverse-words-in-a-string-iii/

---

## 💡 Approach

I solved this problem using **String Manipulation + Two Pointers**.

### Steps

1. Split the sentence into individual words.
2. Reverse each word independently using two pointers.
3. Join the reversed words back together using spaces.

For each word, two pointers are used:

- `i` starts from the beginning.
- `j` starts from the end.

Characters are swapped while `i <= j`.

---

## 🧠 Python Solution

```python
class Solution:
    def reverseWords(self, s: str) -> str:

        def reverse_words(word):
            chars = list(word)
            i = 0
            j = len(chars) - 1

            while i <= j:
                chars[i], chars[j] = chars[j], chars[i]
                i += 1
                j -= 1

            return "".join(chars)

        words = s.split(" ")

        return " ".join(reverse_words(w) for w in words)
