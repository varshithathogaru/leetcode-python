# Day 38 - Goat Latin

## 🚀 LeetCode #824

### Problem

Convert a sentence into Goat Latin according to the given rules.

### Goat Latin Rules

1. If a word begins with a vowel, append `"ma"` to the word.
2. If a word begins with a consonant, move the first letter to the end and then append `"ma"`.
3. Append one additional `"a"` for the first word, two for the second word, three for the third word, and so on.

---

## 💡 Approach

I split the sentence into individual words and processed each word one by one.

For every word:

1. Check whether the first character is a vowel.
2. If it is a vowel, append `"ma"`.
3. Otherwise, move the first character to the end and append `"ma"`.
4. Add `"a" * i`, where `i` represents the word position.
5. Store the transformed word.
6. Join all transformed words with spaces.

---

## 💻 Solution

```python
class Solution:
    def toGoatLatin(self, sentence: str) -> str:

        vowels = set("aeiouAEIOU")
        words = sentence.split()
        result = []

        for i, word in enumerate(words, start=1):
            if word[0] in vowels:
                goat_word = word + "ma"
            else:
                goat_word = word[1:] + word[0] + "ma"

            goat_word += "a" * i
            result.append(goat_word)

        return " ".join(result)
