class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dict = {}

        for i in range(len(order)):
            dict[order[i]] = i
        
        def is_Greater(word1, word2):
            if word1 == word2:
                return False
            if word1.startswith(word2):
                return True

            n = min(len(word1), len(word2))

            for i in range(n):
                if word1[i] == word2[i]:
                    continue
                if dict[word1[i]] > dict[word2[i]]:
                    return True
                return False

        for i in range(len(words) - 1):
            if is_Greater(words[i], words[i + 1]):
                return False
        
        return True