# Day 35 - Find Words That Can Be Formed by Characters

## LeetCode #1160

### Problem

Given a list of words and a string `chars`, find the sum of lengths of all words that can be formed using the characters in `chars`.

Each character can be used only as many times as it appears in `chars`.

---

## Approach

Use `Counter` to store character frequencies.

1. Count the frequency of characters in `chars`.
2. For every word, create another frequency map.
3. Compare the required frequency with the available frequency.
4. If every character is available in sufficient quantity, add the word length to the answer.

---

## Example

```text
words = ["cat", "bt", "hat", "tree"]
chars = "atach"
