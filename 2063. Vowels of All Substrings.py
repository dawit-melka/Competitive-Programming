class Solution:
    def countVowels(self, word: str) -> int:
        count = 0
        for i in range(len(word)):
            if word[i] in "aeiou":
                l = len(word) - i
                count += ((i+1) * l)
        
        return count
