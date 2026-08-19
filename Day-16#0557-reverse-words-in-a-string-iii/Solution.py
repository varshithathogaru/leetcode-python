from typing import List

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
