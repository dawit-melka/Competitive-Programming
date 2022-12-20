class Solution:
    def similarPairs(self, words: List[str]) -> int:
        freq = {}
        total = 0

        for word in words:
            word = "".join(sorted(set(word)))
            prev = freq.get(word, 0)

            total += prev
            freq[word] = prev + 1

        return total
