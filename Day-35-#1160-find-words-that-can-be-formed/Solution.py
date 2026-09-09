from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_freq = Counter(chars)
        tot_length = 0

        for w in words:
            word_count = Counter(w)
            is_valid = True

            for c in word_count:
                if word_count[c] > char_freq.get(c, 0):
                    is_valid = False
                    break

            if is_valid:
                tot_length += len(w)

        return tot_length
