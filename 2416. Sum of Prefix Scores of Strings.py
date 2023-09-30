class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        sortedWords = sorted(words)
        result = []
        def findAns(word):
            l = 0
            r = len(words)-1
            ans = 0
            for i in range(len(word)):
                while l <= r and(len(sortedWords[l]) <= i or sortedWords[l][i] != word[i]):
                    l += 1
                while r >= l and(len(sortedWords[r]) <= i or sortedWords[r][i] != word[i]):
                    r -= 1
                if r < l:
                    break
                else:
                    ans +=( r - l + 1)
            
            return ans
         
        for word in words:
            result.append(findAns(word))
            
        return result
