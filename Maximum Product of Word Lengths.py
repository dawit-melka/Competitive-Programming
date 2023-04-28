class Solution:
    def computeBit(self, word):
        val = 0

        for char in word:
            val |= 1 << (ord(char) - ord("a"))
        
        return val

    def maxProduct(self, words: List[str]) -> int:
        max_len = 0
        word_bit_map = []

        for word in words:
            word_bit_map.append(self.computeBit(word))


        for i in range(len(word_bit_map)):
            for j in range(i+1, len(word_bit_map)):
                if not(word_bit_map[i] & word_bit_map[j]):
                    max_len = max(len(words[i]) * len(words[j]), max_len)

        return max_len        
