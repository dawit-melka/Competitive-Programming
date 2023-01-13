class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        commons = []
        frequency = [Counter(word) for word in words]

        for letter in words[0]:
            frequency[0][letter] -= 1
            foundInAll = True

            for i in range(1, len(words)):
                if letter not in frequency[i] or frequency[i][letter] == 0:
                    foundInAll = False
                    break
                frequency[i][letter] -= 1
                
            if foundInAll:
                commons.append(letter)

        return commons
