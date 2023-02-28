class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        freq = Counter(s)
        stack = []
        visited = set()
        
        for char in s:
            freq[char] -= 1
            if char in visited:
                continue
            
            while stack and char <= stack[-1] and freq[stack[-1]] > 0:
                visited.remove(stack.pop())
                
            stack.append(char)
            visited.add(char)

        return "".join(stack)
