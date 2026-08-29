# LeetCode #290 - Word Pattern

## 🧩 Problem Statement

Given a pattern and a string `s`, determine whether `s` follows the
same pattern.

Each character in the pattern must correspond to exactly one word,
and each word must correspond to exactly one character.

## 💡 Approach

I solved this problem using **Two Hash Maps**.

I maintained:

1. `char_to_word` - maps each pattern character to a word.
2. `word_to_char` - maps each word back to its pattern character.

Both mappings are required to ensure a one-to-one relationship.

### Steps

1. Split the string into words.
2. Check whether the number of pattern characters equals the number
   of words.
3. Traverse both using `zip()`.
4. Validate the character-to-word mapping.
5. Validate the word-to-character mapping.
6. Return `True` if all mappings are consistent.

## 🧠 Python Solution

```python
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for c, w in zip(pattern, words):

            if c in char_to_word and char_to_word[c] != w:
                return False

            if w in word_to_char and word_to_char[w] != c:
                return False

            char_to_word[c] = w
            word_to_char[w] = c

        return True
