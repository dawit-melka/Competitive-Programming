class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_word_len = 0
        answer = []

        for word in words:
            max_word_len = max(max_word_len, len(word))
        
        for c in range(max_word_len):
            col_word = []
            count_space = 0
            for r in range(len(words)):
                if c >= len(words[r]):
                    count_space += 1
                    continue
                
                while count_space:
                    col_word.append(" ")
                    count_space -= 1
                
                col_word.append(words[r][c])
            
            answer.append("".join(col_word))
        
        return answer
