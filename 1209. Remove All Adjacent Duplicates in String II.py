class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for char in s:
            if not stack or stack[-1][0] != char:
                stack.append([char, 1])
            elif stack[-1][1] == k-1:
                stack.pop()
            else:
                stack[-1][1] += 1
        
        stack = [char*count for char, count in stack]
        
        return "".join(stack)
